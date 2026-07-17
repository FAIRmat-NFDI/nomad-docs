# How to write a dashboard

## What is a dashboard?

A **dashboard** is a custom web interface that a NOMAD plugin contributes
to the NOMAD GUI. Users discover installed dashboards on the *Dashboards*
page of the GUI and can open each one either **embedded** (inside an iframe
on a dedicated viewer page in the GUI) or in a **new browser tab**.

Dashboards can be used for a wide variety of purposes:

- A small interactive search or filtering UI tailored to a specific
  domain or community.
- A custom data-viewer or analysis tool (e.g. a Jupyter-like notebook,
  a plotting tool, a chemistry-specific 3D viewer).
- A landing page or guided workflow for a particular user group.
- A bridge to an existing internal tool that should be reachable from
  within NOMAD without forcing users to remember a separate URL.

### How do dashboards differ from APIs?

[API plugin entry points](./apis.md) and dashboards are technically
similar (both can mount a FastAPI app inside NOMAD), but their audience
is different:

- **Audience.** APIs target other programs (clients, scripts, integrations),
  while dashboards target end users working in a browser.
- **How they surface in the GUI.** APIs are listed on the *APIs* page, with
  links to reach each mounted API. Dashboards are listed on the *Dashboards*
  page, with embedded and new-tab launchers, icons and descriptions.
- **Typical content.** APIs serve JSON endpoints, whereas dashboards serve
  HTML and JS, optionally a full SPA.

You should read the [introduction to plugins](../plugins.md) to have a
basic understanding of how plugins and plugin entry points work in the
NOMAD ecosystem.

!!! note
    Dashboards are only available in the new NOMAD GUI. The old GUI is
    not aware of dashboard entry points.

## Getting started

You can use our
[template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template){:target="_blank" rel="noopener"}
to create an initial structure for a plugin containing a dashboard.
The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── dashboards
   │   │   │   ├── __init__.py
   │   │   │   ├── hello.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

See the documentation on
[plugin development guidelines](../plugins.md#plugin-development-guidelines)
for more details on the best development practices for plugins, including
linting, testing and documenting.

## Dashboard entry point

The entry point defines basic information about your dashboard and is used
to automatically load it into a NOMAD distribution. It is an instance of a
`DashboardEntryPoint` or its subclass. The entry point is typically defined
in `*/dashboards/__init__.py`:

```python
from nomad.config.models.plugins import DashboardEntryPoint


class HelloDashboardEntryPoint(DashboardEntryPoint):

    def load(self):
        from nomad_example.dashboards.hello import app

        return app


hello_dashboard = HelloDashboardEntryPoint(
    name='Hello, NOMAD',
    description='A minimal hello-world dashboard.',
    launch_modes=['embedded', 'tab'],
)
```

In the reference you can see all of the available
[configuration options for a `DashboardEntryPoint`](../../../reference/plugins.md#dashboardentrypoint).

The entry point instance must then be added to the
`[project.entry-points.'nomad.plugin']` table in `pyproject.toml` in order
for it to be automatically detected:

```toml
[project.entry-points.'nomad.plugin']
hello_dashboard = "nomad_example.dashboards:hello_dashboard"
```

## URL slug (`id_url_safe`)

NOMAD mounts your dashboard at `{api_base_path}/dashboards/{id_url_safe}/`,
where `id_url_safe` is the URL-safe identifier of the entry point. If you
do not set it explicitly, it is automatically derived from the entry-point
id (which is the full Python entry-point name, e.g.
`nomad_example.dashboards-hello_dashboard`). For a shorter, friendlier URL
you can override it on the entry point:

```python hl_lines="3"
hello_dashboard = HelloDashboardEntryPoint(
    name='Hello, NOMAD',
    id_url_safe='hello',
    launch_modes=['embedded', 'tab'],
)
```

With this, the dashboard becomes reachable at
`{api_base_path}/dashboards/hello/`, and the NOMAD GUI links to
`/dashboards/hello`. `id_url_safe` is checked for URL safety and for
collisions with other entry points within the deployment, so two plugins
cannot accidentally claim the same slug.

## Hosting: FastAPI mount vs. external URL

A dashboard entry point can be served in one of two ways. The choice is
exclusive — set exactly one of the two.

### FastAPI-hosted (recommended)

Override `load()` to return a `fastapi.FastAPI` instance. NOMAD mounts
it same-origin under `{api_base_path}/dashboards/{id_url_safe}/`. This
is the recommended path for most dashboards, because it unlocks:

- **No CORS plumbing** — your dashboard can `fetch` `/api/v1/...`
  directly.
- **Authentication for free** — the NOMAD GUI's `Authorization` cookie
  is sent automatically with same-origin requests (see
  [Authentication](#authentication) below).
- **Easy styling integration** — your dashboard can read the parent
  GUI's theme colors at runtime (see [Styling](#styling) below).
- **Single distribution unit** — the dashboard ships inside your Python
  package; no separate process to deploy or maintain.

The `load`-method is called by NOMAD at startup with no arguments. A
minimal hello-world `*/dashboards/hello.py` could look like this:

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

_PAGE = """<!doctype html>
<html>
<body>
  <h1>Hello, NOMAD!</h1>
</body>
</html>
"""


@app.get('/', response_class=HTMLResponse)
async def index():
    return _PAGE
```

If you run NOMAD with this plugin following our
[Oasis configuration documentation](../../oasis/configure.md) with the
default configuration, you can curl the dashboard and should receive the
HTML page:

```sh
curl localhost:8000/nomad-oasis/dashboards/hello/
```

Read the official
[FastAPI documentation](https://fastapi.tiangolo.com/tutorial/){:target="_blank" rel="noopener"}
to learn how to build apps with FastAPI.

#### Static files and single-page applications

For richer dashboards built with React, Vue, Svelte, etc., ship the
pre-built bundle inside your package and serve it with FastAPI's
`StaticFiles`. The typical SPA layout — `dist/` containing `index.html`
plus an `assets/` folder — is supported via a small catch-all fallback so
client-side routing keeps working on deep-links:

```python
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

_DIST = Path(__file__).parent / 'dist'

app = FastAPI()
app.mount('/assets', StaticFiles(directory=_DIST / 'assets'), name='assets')

@app.get('/{_full_path:path}')
async def spa_fallback(_full_path: str):
    return FileResponse(_DIST / 'index.html')
```

!!! note
    If you ship static files inside your Python package distribution
    (e.g. to publish on PyPI), include them in the package data of your
    `pyproject.toml`. See the
    [setuptools guide](https://setuptools.pypa.io/en/latest/userguide/datafiles.html){:target="_blank" rel="noopener"}
    for the available options.

### Externally hosted (`external_url`)

If your dashboard is served by a separate service (a Streamlit app, a
standalone Next.js deployment, an existing internal tool, …), set
`external_url` instead of overriding `load()`. NOMAD will not mount
anything and will simply link/iframe to the configured URL:

```python
external_dashboard = DashboardEntryPoint(
    name='My external dashboard',
    description='Served by a separate process.',
    external_url='https://my-dashboard.example.com',
    launch_modes=['tab', 'embedded'],
)
```

`external_url` must be an absolute `http(s)://` URL. The external
service is responsible for everything: serving content, authenticating
users, allowing itself to be iframed (no `X-Frame-Options: DENY` or
restrictive `Content-Security-Policy: frame-ancestors`), and matching
the NOMAD look-and-feel.

The trade-offs compared to FastAPI hosting are:

- **No automatic authentication** with the NOMAD GUI session — see
  [Authentication](#authentication) below.
- **No same-origin shortcuts** — cross-origin requests need CORS support
  on the NOMAD side and explicit handling on yours.
- **No automatic styling** — your service must implement its own look,
  and cannot read the parent GUI's theme variables at runtime (see
  [Styling](#styling) below).
- **Separate deployment** — your service has its own lifecycle, scaling
  and TLS story to think about.

## Launch modes

The `launch_modes` list controls how a user can open the dashboard from
the NOMAD GUI:

- **`embedded`** — opens the dashboard inside an iframe on a dedicated
  *Dashboard viewer* page within the GUI. Best for dashboards that
  should feel like a native part of NOMAD.
- **`tab`** — opens the dashboard in a new browser tab. Best for
  dashboards that benefit from being full-window, or that the user
  wants to keep open alongside the rest of the GUI.

The **order matters**: the first entry is the default action when the
user clicks the dashboard's row in the *Dashboards* table. The other
mode is still available as a secondary action. Listing only one mode
hides the other action button entirely.

```python
# Embedded is the primary action; clicking the row opens the iframe view.
launch_modes=['embedded', 'tab']

# Tab is the primary action; the iframe option is still offered.
launch_modes=['tab', 'embedded']

# Embedded only — no "open in new tab" action will be shown.
launch_modes=['embedded']
```

## Authentication

### FastAPI-hosted dashboards

When a user is logged in to the NOMAD GUI, the GUI sets an
`Authorization` cookie scoped to `api_base_path`. Because a FastAPI-hosted
dashboard is mounted *under* that same path, the cookie is sent
automatically with both:

- **Server-side requests** that hit your dashboard's own FastAPI
  endpoints (e.g. when the user navigates to `/dashboards/hello/`), and
- **Client-side `fetch` calls** to `{api_base_path}/api/v1/...` from
  inside the dashboard page (provided you use
  `credentials: 'same-origin'`).

This means **you don't have to think about token handoff**. You write
ordinary FastAPI routes and add the standard NOMAD auth dependency to
capture the authenticated user — exactly the same as for an
[API entry point](./apis.md#protecting-the-api-with-auth):

```python
from typing import Annotated
from fastapi import FastAPI, Depends
from nomad.app.v1.routers.auth import get_current_user
from nomad.auth.scopes import Scope
from nomad.app.v1.models import User

app = FastAPI()


@app.get('/whoami')
async def whoami(
    user: Annotated[
        User,
        Depends(get_current_user([Scope.USERS_READ], allow_anonymous=False)),
    ],
):
    return {'user_id': user.user_id, 'username': user.username}
```

If the visitor is not logged in, the dependency returns `401` and you
can let your frontend render a "please log in via the NOMAD GUI" prompt.

You can attach the dependency app-wide if every endpoint requires the
same access, or per-route if different endpoints need different scopes.
See the [API auth section](./apis.md#protecting-the-api-with-auth) for
both patterns.

The same applies when the dashboard's JavaScript calls NOMAD's main
API directly from the browser:

```js
// Derive api_base_path from the dashboard's mount path, so this works
// under any deployment prefix.
var apiBase = window.location.pathname
  .replace(/\/dashboards\/[^/]+\/?$/, '') + '/api/v1';

fetch(apiBase + '/users/me', {credentials: 'same-origin'})
  .then(function (r) {
    if (r.status === 401) {
      // Visitor is not logged in — render a graceful fallback.
      return;
    }
    return r.json();
  });
```

### Externally hosted dashboards

For externally hosted dashboards there is **currently no robust
authentication handoff** from NOMAD. The NOMAD GUI's session cookie is
scoped to NOMAD's own origin and is not visible cross-origin to your
service, so an external dashboard cannot tell whether the visitor is
logged in to NOMAD or who they are.

If your external service needs an authenticated user identity, you
have to handle that yourself — typically by running your own auth
(e.g. its own Keycloak client) and asking the user to sign in there
separately. A proper out-of-the-box mechanism (e.g. short-lived
launch-token handoff) is on the roadmap but is not implemented yet.

## Styling

Dashboards live inside the new NOMAD GUI, so it's worth a little effort
to make them feel native. The available approaches differ between
FastAPI-hosted and externally hosted dashboards.

### Styling a FastAPI-hosted dashboard

The NOMAD GUI uses [Material UI](https://mui.com){:target="_blank" rel="noopener"}
with the `cssVariables: true` option, which means the active theme is
exposed as CSS custom properties (`--mui-palette-primary-main`,
`--mui-palette-background-default`, `--mui-palette-text-primary`, …) on
the GUI's root element. Because a FastAPI-hosted dashboard is mounted
same-origin with the GUI, the embedded iframe **can read those
variables from its parent** at runtime and apply them locally:

```html
<style>
  :root {
    --bg: #fff;
    --text: #000;
    --primary: #2a4cdf;
  }
  body { background: var(--bg); color: var(--text); }
  a { color: var(--primary); }
</style>

<script>
  (function () {
    // Same-origin: we can reach into the parent document.
    if (window.parent === window) return; // open in a new tab → no parent
    try {
      var parentRoot = window.parent.document.documentElement;
      var parentStyle = window.parent.getComputedStyle(parentRoot);
      var root = document.documentElement;
      ['--mui-palette-background-default',
       '--mui-palette-text-primary',
       '--mui-palette-primary-main'].forEach(function (name) {
        var value = parentStyle.getPropertyValue(name);
        if (value) root.style.setProperty(name, value);
      });
      // Inherit light/dark mode.
      var scheme = parentRoot.getAttribute('data-mui-color-scheme');
      if (scheme) root.setAttribute('data-mui-color-scheme', scheme);
    } catch (e) {
      // Parent unavailable (e.g. opened in a new tab) — keep our fallback.
    }
  })();
</script>
```

If the user toggles between light and dark mode in the GUI, you can
follow that change with a `MutationObserver` on the parent root's
`data-mui-color-scheme` attribute.

When the dashboard is launched in `tab` mode there is no parent to read
from, so design your CSS with sensible fallbacks (a `:root { --bg: …; }`
declaration is enough — the JS above only overrides what is available).

The authoritative list of theme colors lives in the NOMAD GUI's theme
file. Use it as the source of truth when you need to hard-code values
or extend the palette:
[`src/components/theme/themeOptions.ts`](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-gui/-/blob/develop/src/components/theme/themeOptions.ts){:target="_blank" rel="noopener"}.

### Styling an externally hosted dashboard

For externally hosted dashboards, **browser same-origin policy
prevents reading the parent's CSS variables or any other DOM state**
from inside the iframe. Until a postMessage-based theme handoff is
implemented, your options are:

- Hard-code colors that approximate the NOMAD palette — use
  [`themeOptions.ts`](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-gui/-/blob/develop/src/components/theme/themeOptions.ts){:target="_blank" rel="noopener"}
  as your reference.
- Detect the user's OS-level preference with
  `@media (prefers-color-scheme: dark)` and render a matching theme.
  This won't follow the GUI's explicit light/dark toggle, but is a
  reasonable approximation in practice.

## Icons

You can attach an icon that is shown in the NOMAD GUI's dashboards table
and on pinned-dashboards widgets. The icon is an absolute URL that the
plugin author is responsible for serving — either alongside the
dashboard itself, or via any public CDN:

```python
hello_dashboard = HelloDashboardEntryPoint(
    name='Hello, NOMAD',
    icon='https://cdn.example.com/icons/hello.svg',
    launch_modes=['embedded', 'tab'],
)
```

Use a square SVG or PNG of modest size (the GUI renders it at 20–30 px).
If you don't set an icon, the GUI falls back to a generic web icon.

## Embedding (CSP `frame-ancestors`)

When a dashboard is launched in `embedded` mode, the NOMAD GUI loads it
in an iframe. For FastAPI-hosted dashboards, NOMAD adds a
`Content-Security-Policy: frame-ancestors …` header to responses from
`{api_base_path}/dashboards/` to restrict who is allowed to embed it.

By default the policy is `'self'` (only the NOMAD GUI on the same
origin). Operators can broaden it via the deployment config — for
example to allow the GUI dev server on `localhost:3000` to embed
dashboards during local development:

```yaml
services:
  dashboard_frame_ancestors:
    - "'self'"
    - 'http://localhost:3000'
```

See the [configuration reference](../../../reference/config.md#services)
for the full list of `services` options.

For externally hosted dashboards the framing policy is controlled
entirely by your external service.

## Dev-mode caveat

In a deployed NOMAD instance the GUI and the backend share the same
origin, so cookies are sent transparently to FastAPI-hosted dashboards.

In a separated dev setup — typically the GUI running on
`localhost:3000` and the backend on `localhost:8000` — cookies do
**not** cross origins, so a dashboard loaded from the backend will not
see the GUI's session cookie and authenticated endpoints will return
`401`. This is a same-origin policy constraint, not a NOMAD limitation.
Either:

- Test the authenticated paths in a deployed (same-origin) NOMAD
  instance, or
- Implement a graceful 401 fallback in your dashboard so it remains
  usable when the visitor is not logged in.

## Sample use cases

### Running highly customized code on NOMAD

A dashboard is one way to bring highly customized or personalized code onto
NOMAD infrastructure. There are two routes for this:

1. **A NORTH tool** — package the code as a containerized, interactive tool
   launched through the [NORTH tools plugin](./north_tools.md). Best when the
   application needs its own runtime environment (for example a full Jupyter
   or desktop environment running in a container).
2. **A dashboard plus actions** — serve the code as a dashboard and implement
   its server-side behaviour with the [actions plugin](./actions.md). Best
   when a lightweight web UI backed by NOMAD's API is enough.
