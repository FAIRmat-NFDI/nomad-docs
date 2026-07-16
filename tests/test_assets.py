#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os


def find_unused_assets():
    """
    Finds unused assets in the docs/ directory.

    An asset is considered unused if its filename does not appear in any
    Markdown file in the same section of the docs (the parent folder and its
    subfolders), ignoring the images/ and data/ folders.
    """
    docs_dir = os.path.join(os.path.dirname(__file__), "..", "docs")
    asset_dirs = ["images", "data"]
    unused_assets = []

    for asset_subdir in asset_dirs:
        for root, _, _ in os.walk(docs_dir):
            if os.path.basename(root) != asset_subdir:
                continue

            parent_dir = os.path.dirname(root)

            md_text_parts = []
            for md_root, md_dirs, md_files in os.walk(parent_dir):
                md_dirs[:] = [d for d in md_dirs if d not in asset_dirs]
                for fn in md_files:
                    if fn.endswith(".md"):
                        path = os.path.join(md_root, fn)
                        with open(path, "r", encoding="utf-8") as f:
                            md_text_parts.append(f.read())

            md_text = "\n".join(md_text_parts)

            for asset_file in os.listdir(root):
                full_path = os.path.join(root, asset_file)
                if os.path.isdir(full_path):
                    continue

                if asset_file not in md_text:
                    rel_path = os.path.relpath(full_path, docs_dir)
                    unused_assets.append(rel_path)

    return unused_assets


def test_no_unused_assets():
    """
    Tests that there are no unused assets in the docs directory.
    """
    unused_assets = find_unused_assets()
    if unused_assets:
        message = f"Found {len(unused_assets)} unused assets:\n" + "\n".join(
            f"- {asset}" for asset in unused_assets
        )
        assert not unused_assets, message
