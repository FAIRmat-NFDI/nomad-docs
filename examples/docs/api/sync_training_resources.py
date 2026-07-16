import argparse
import json
import os
import re
from datetime import datetime, timezone
from getpass import getpass
from pathlib import Path
from typing import Any

import requests


_HTML_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(s: str) -> str:
    return _HTML_TAG_RE.sub("", s or "").replace("\n", " ").strip()


def _auth_headers(token: str | None) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"} if token else {}


def _clean_token(token: str) -> str:
    t = (token or "").strip().replace("\r", "").replace("\n", "")
    if t.lower().startswith("bearer "):
        t = t[7:].strip()
    t = t.strip('"').strip("'").strip()
    return t


def get_access_token(api_base: str, username: str, password: str) -> str:
    r = requests.post(
        f"{api_base}/auth/token",
        data={"username": username, "password": password, "grant_type": "password"},
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()
    token = data.get("access_token")
    if not token:
        raise ValueError("No access_token in response.")
    return token


def get_app_token(api_base: str, access_token: str, expires_in: int) -> str:
    r = requests.get(
        f"{api_base}/auth/app_token",
        params={"expires_in": expires_in},
        headers=_auth_headers(access_token),
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()
    token = data.get("token") or data.get("app_token") or data.get("access_token")
    if not token:
        raise ValueError("No app token in response.")
    return token


def read_token(token_path: Path) -> str | None:
    if not token_path.exists():
        return None
    token = _clean_token(token_path.read_text(encoding="utf-8"))
    return token or None


def write_token(token_path: Path, token: str) -> None:
    token_path.parent.mkdir(parents=True, exist_ok=True)
    token_path.write_text(_clean_token(token), encoding="utf-8")
    try:
        os.chmod(token_path, 0o600)
    except Exception:
        pass


def _parse_dt(s: str | None) -> datetime:
    if not s:
        return datetime.min.replace(tzinfo=timezone.utc)
    t = s.strip()
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(t)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return datetime.min.replace(tzinfo=timezone.utc)


def fetch_training_resources(
    api_base: str,
    token: str,
    tag: str,
    owner: str,
    page_size: int = 200,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    page_after_value: str | None = None

    while True:
        body: dict[str, Any] = {
            "owner": owner,
            "query": {"results.eln.tags": tag},
            "pagination": {"page_size": page_size, "order_by": "entry_id", "order": "asc"},
            "required": {
                "metadata": {"entry_id": "*", "upload_id": "*", "entry_name": "*"},
                "data": {
                    "title": "*",
                    "description": "*",
                    "date_created": "*",
                    "identifier": "*",
                    "tags": "*",
                    "keyword": "*",
                    "subject": "*",
                    "educational_level": "*",
                    "instructional_method": "*",
                    "learning_resource_type": "*",
                },
                "results": {"eln": {"tags": "*"}},
            },
        }
        if page_after_value:
            body["pagination"]["page_after_value"] = page_after_value

        r = requests.post(
            f"{api_base}/entries/archive/query",
            json=body,
            headers=_auth_headers(token),
            timeout=120,
        )
        r.raise_for_status()
        resp = r.json()

        hits = resp.get("data") or []
        for hit in hits:
            archive = hit.get("archive") or {}
            meta = archive.get("metadata") or {}
            d = archive.get("data") or {}
            res_eln_tags = (((archive.get("results") or {}).get("eln") or {}).get("tags")) or []
            tags = d.get("tags") or []

            if tag not in tags and tag not in res_eln_tags:
                continue

            entry_id = meta.get("entry_id") or hit.get("entry_id")
            upload_id = meta.get("upload_id") or hit.get("upload_id")

            identifier = (d.get("identifier") or "").strip() or None
            title = (d.get("title") or meta.get("entry_name") or "").strip() or entry_id
            description = _strip_html(d.get("description") or "")
            date_created = d.get("date_created")

            out.append(
                {
                    "entry_id": entry_id,
                    "upload_id": upload_id,
                    "title": title,
                    "identifier": identifier,
                    "date_created": date_created,
                    "description": description,
                    "tags": tags,
                    "keyword": d.get("keyword") or [],
                    "subject": d.get("subject") or [],
                    "educational_level": d.get("educational_level") or [],
                    "instructional_method": d.get("instructional_method") or [],
                    "learning_resource_type": d.get("learning_resource_type") or [],
                }
            )

        page_after_value = (resp.get("pagination") or {}).get("next_page_after_value")
        if not page_after_value:
            break

    out.sort(key=lambda x: _parse_dt(x.get("date_created")), reverse=True)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--api-base", default="http://141.20.184.181/nomad-oasis/api/v1")
    p.add_argument("--tag", default="YouTube Playlist")
    p.add_argument("--owner", default="visible")
    p.add_argument("--out", default="src/nomad_docs/data/training_resources_youtube_playlist.json")
    p.add_argument(
        "--token-path",
        default=str(Path.home() / ".config" / "nomad-docs" / "oasis_app_token"),
    )
    p.add_argument("--app-token-expires-in", type=int, default=7 * 24 * 3600)
    args = p.parse_args()

    token_path = Path(args.token_path)
    token = read_token(token_path)

    def _prompt_new_app_token() -> str:
        username = os.getenv("NOMAD_USERNAME") or input("NOMAD username: ").strip()
        password = os.getenv("NOMAD_PASSWORD") or getpass("NOMAD password: ")
        access = get_access_token(args.api_base, username, password)
        app_token = get_app_token(args.api_base, access, args.app_token_expires_in)
        write_token(token_path, app_token)
        return app_token

    if not token:
        token = _prompt_new_app_token()

    try:
        items = fetch_training_resources(
            api_base=args.api_base,
            token=token,
            tag=args.tag,
            owner=args.owner,
        )
    except requests.HTTPError as e:
        status = getattr(getattr(e, "response", None), "status_code", None)
        if status == 401:
            try:
                token_path.unlink(missing_ok=True)  # type: ignore[arg-type]
            except TypeError:
                if token_path.exists():
                    token_path.unlink()
            token = _prompt_new_app_token()
            items = fetch_training_resources(
                api_base=args.api_base,
                token=token,
                tag=args.tag,
                owner=args.owner,
            )
        else:
            raise

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "api_base": args.api_base,
        "tag": args.tag,
        "count": len(items),
        "items": items,
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(items)} items to {out_path}")


if __name__ == "__main__":
    main()