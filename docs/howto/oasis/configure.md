# How to configure a NOMAD Oasis

## Configuration files

The [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"}
provides all the necessary configuration files. We strongly recommend to create your own distribution
project based on the template. This will allow you to version your configuration, build custom
images with plugins, and much more.

In this section, you can learn about settings that you might need to change. The most relevant config files are:

- `docker-compose.yaml`
- `configs/nomad.yaml`
- `configs/nginx_http.conf` and `configs/nginx_https.conf`
- `configs/nginx_base_conf` and `configs/nginx_maps_conf`
- `.env` and `.env.north`

Docker Compose configures the containers. The NOMAD image includes `configs/nomad.yaml`;
nginx configuration and environment files are supplied at runtime. Follow the
[template quick-start](https://github.com/FAIRmat-NFDI/nomad-distro-template#quick-start-for-a-local-oasis){:target="_blank" rel="noopener"}
to generate the required secrets and prepare these files before starting services.

### docker-compose.yaml

Use the template's maintained
[`docker-compose.yaml`](https://github.com/FAIRmat-NFDI/nomad-distro-template/blob/main/docker-compose.yaml){:target="_blank" rel="noopener"}
as the baseline for your distribution, together with its configuration files and scripts.
Do not combine it with configuration files from older NOMAD releases.

The current template uses:

- MongoDB 8.0 for metadata and processing state.
- Elasticsearch 9.5.0 for search.
- Temporal with PostgreSQL persistence for processing and Actions, including one-off
  jobs to initialize the database and create the namespace.
- The distribution's NOMAD image from GHCR for the `app` and `worker` services.
- A separate `nomad-north` image for the `north` service.
- nginx as the `proxy`, exposing ports 80 and 443. Enabling HTTPS also requires
  configuring a certificate and the HTTPS nginx configuration.

Image overrides are defined in `x-images`, including `APP_IMAGE` and `IMAGE_TAG`.
Choose images compatible with your distribution's configuration and plugins.
The default `main` tag tracks development builds; pin a suitable release for production.

Database data is stored in named volumes; NOMAD files are bind-mounted from
`./.volumes/fs`. Keep `PWD` set to your distribution directory so NORTH can resolve
host paths. NORTH also needs access to the host Docker socket.

!!! warning
    Upgrading an existing Oasis is not just an image-tag change. Follow the
    [migration guides](migrate.md) before changing database versions or reusing volumes.

### nomad.yaml

The app and workers read `nomad.yaml`. Start with the template's
[`configs/nomad.yaml`](https://github.com/FAIRmat-NFDI/nomad-distro-template/blob/main/configs/nomad.yaml){:target="_blank" rel="noopener"}.

- Set `services.api_host` to the hostname users can reach, without a scheme or path.
- Set `meta.deployment` and `meta.maintainer_email` for your installation.
- The template uses `services.api_base_path: /backend`; the GUI is served at `/`.
  Changing this prefix also requires corresponding proxy and NORTH changes.
- `mongo.db_name` and `elastic.entries_index` select the database and search index.
- Keep Temporal enabled and use the Compose-provided `NOMAD_TEMPORAL_HOST` setting.
- Configure the separate NORTH service through `.env.north` and its Compose
  environment, including `OAUTH_CALLBACK_URL`. Follow the template instructions for
  matching the NORTH service API tokens and generating secrets.

The Docker build includes `configs/nomad.yaml` in the image. After editing it, either
build and deploy a new image or uncomment the local configuration mount in
`x-nomad-base.volumes` to supply it to all NOMAD app and worker containers.

### nginx.conf

The separate `proxy` service runs nginx. Use the template's maintained
[nginx configuration files](https://github.com/FAIRmat-NFDI/nomad-distro-template/tree/main/configs){:target="_blank" rel="noopener"}
together: `nginx_http.conf` (or `nginx_https.conf`), `nginx_base_conf`, and
`nginx_maps_conf`. They serve the GUI at `/` and route backend requests under `/backend`.

`client_max_body_size` limits upload size. You can add additional locations for other
services, but preserve the template's routing and streaming settings.

Before exposing your Oasis publicly, follow the template's
[production and HTTPS instructions](https://github.com/FAIRmat-NFDI/nomad-distro-template#steps-before-entering-production){:target="_blank" rel="noopener"}.
You can also place an additional reverse proxy in front.
If you operate the Oasis proxy behind another reverse proxy, keep in mind that it should
not buffer requests/responses to allow streaming of large requests/responses for `api/v1/uploads` and `api/v1/.*/download`.
An `nginx` reverse proxy location on an additional reverse proxy, could have these directives
to ensure the correct HTTP headers and allow the download and upload of large files:

```nginx
location / {
    client_max_body_size 35g;
    proxy_set_header Host $host;
    proxy_pass_request_headers on;
    proxy_buffering off;
    proxy_request_buffering off;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_pass http://<your-oasis-host>;
}
```

## Starting and stopping NOMAD services

Run these commands from your distribution directory after completing the template's
quick-start setup, including secret generation.

To make sure you have the latest docker images for everything, run this first:

```sh
docker compose pull
```

Start the complete stack so Compose can start dependencies and run Temporal's
initialization jobs in the correct order:

```sh
docker compose up -d
```

The `-d` option runs containers in the background. Inspect startup and logs with:

```sh
docker compose ps -a
docker compose logs -f app worker temporal proxy north
```

The `temporal-setup-db` and `temporal-create-namespace` jobs should finish successfully;
they are not long-running services.

Running all services also contains NORTH. When you use a tool in NORTH for the first time,
your docker needs to pull the image that contains this tool. Be aware that this might take longer
than timeouts allow and starting a tool for the very first time might fail.

You can also use docker to stop and remove faulty containers that run as *daemons*:

```sh
docker stop nomad_oasis_app
docker rm nomad_oasis_app
```

Check the app through the proxy using its `alive` endpoint:

```sh
curl http://<your-host>/backend/alive
```

If everything works, the GUI should be available under:

```none
http://<your-host>/
```

If you run into problems, use the dev-tools of your browser to check the javascript logs
or monitor the network traffic for HTTP 500/400/404/401 responses.

To see if at least the api works, check

```none
http://<your-host>/backend/alive
http://<your-host>/backend/api/v1/info
```

To see logs or "go into" a running container, you can access the individual containers
with their names and the usual docker commands:

```sh
docker logs nomad_oasis_app
```

```sh
docker exec -ti nomad_oasis_app /bin/bash
```

When reporting problems, provide relevant service logs, for example:

```sh
docker compose logs app worker temporal proxy north
```

Use Compose service names rather than fixed container names, since workers can have
multiple replicas.

## Plugins

[Plugins](../plugins/plugins.md) allow the customization of a NOMAD deployment in terms of
which search apps, normalizers, parsers and schema packages are available. In order for these
customization to be activated, they have to be configured and installed into an Oasis.
The basic template does not include plugins by default. If you want to configure
your own set of plugins, using the template and creating your own distro project
is mandatory.

Plugins are configured via the `pyproject.toml` file. Based on this file
the distro project CI pipeline creates the NOMAD docker image that is used by your installation.
Only plugins configured in the `pyproject.toml` files, will be installed into the docker
image and only those plugins installed in the used docker image are available in your
Oasis.

Please refer to the [template README](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#adding-a-plugin){:target="_blank" rel="noopener"}
to learn how to add your own plugins.

## Configuring for performance

If you run the Oasis on a single computer, like described here (either with docker or bare
Linux), you might run into problems with processing large uploads. If the NOMAD worker
and app are run on the same computer, the app might become unresponsive, when the worker
consumes all system resources.

NOMAD is designed to efficiently process a wide variety of materials science data out of the box. For most standard deployments, **the default configurations will work perfectly fine** and provide a stable, high-throughput environment.

However, depending on your specific hardware architecture or the unique shape of your data (e.g., massive bursts of tiny files, highly computationally expensive parsers, or massive memory-heavy datasets), you may want to optimize your setup.

Here is a guide on how to tune NOMAD's orchestration engine (Temporal) and worker configurations for specialized workloads.

---

### 1. Scaling Strategy: Replicas vs. Pool Size

When you need to increase your processing throughput, you have two primary choices: add more containers (Horizontal Scaling via Replicas) or increase the capacity of your existing containers (Vertical Scaling via Pool Size).

#### `pool_size` (Vertical Scaling)

In NOMAD, worker pools rely on Python process executors to bypass the Global Interpreter Lock (GIL). This means that increasing the `pool_size` will spawn entirely separate Python processes inside a single container.

You can configure this in your `nomad.yaml` for different worker types (`internal_worker`, `cpu_worker`, `gpu_worker`):

```yaml
temporal:
  internal_worker:
    # Number of Python processes running in this container
    pool_size: 1
    # Restart the process after 100 tasks to clear memory leaks
    max_tasks_per_child: 100
```

* **Recommended baseline:** Start with the current default (`pool_size: 1`) and scale replicas first.
* **When to increase `pool_size`:** Increase it gradually (up to the number of CPU cores allocated to the container) only if a single process is not already saturating your available CPU and you still have memory headroom. This typically applies to workloads with idle time (I/O waits) rather than processes that already run heavily in compiled code paths (e.g., heavy NumPy workloads that already bypass the GIL).
* **Memory impact:** Each extra process consumes additional memory. A container with `pool_size: 10` can use roughly similar memory to ten separate containers with `pool_size: 1`.

#### Worker Replicas (Horizontal Scaling)

Deploying more replicas (via Docker Compose or Kubernetes) adds completely isolated containers to your cluster. This is configured in your deployment manifests, not in `nomad.yaml`.

* **The Isolation Advantage:** We generally recommend relying on replicas for scaling rather than massive `pool_size` values. If a malformed file triggers a severe crash in a Python C-extension (like a segfault), it can bring down the entire container. If you have a high `pool_size`, that single bad file just killed the processing for all other parallel tasks sharing that pod. Replicas isolate this "blast radius," ensuring only the offending container dies and is rescheduled.

*Recommendation: Prefer scaling replicas first for throughput and fault tolerance. If replicas still do not saturate your available CPU, then gradually increase `pool_size` while monitoring memory usage.*

---

### 2. Resource Management & Guardrails

To keep your cluster healthy, you must combine infrastructure constraints with NOMAD's application-aware guardrails.

* **Hard Limits (Infrastructure):** Your Kubernetes or Docker pod resource limits (`resources.limits.memory` and `resources.limits.cpu`) are the ultimate guardrails. They protect your host node from being completely consumed by a runaway worker.
* **Soft Limits (NOMAD `WorkerConfig`):** Settings like `target_memory_usage` and `target_cpu_usage` act as an early-warning system. They allow the worker to gracefully pause accepting new tasks from the queue *before* the container hits the hard Kubernetes limit. This prevents aggressive and disruptive Out-Of-Memory (OOM) kills.

For Docker Compose deployments, you can set CPU hard limits directly in the worker service:

```yml
services:
    worker:
        ...
        deploy:
            resources:
                limits:
                    cpus: '0.50'
```

The value refers to the number of CPU cores the container can use (for example `0.50` means half a CPU core). See also the [docker-compose documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#resources){:target="_blank" rel="noopener"}.

```yaml
temporal:
  internal_worker:
    # Stop accepting new tasks if container CPU hits 80%
    target_cpu_usage: 0.8
    # Stop accepting new tasks if container RAM hits 80%
    target_memory_usage: 0.8
```

---

### 3. Orchestration Concurrency & Backpressure

Beyond how many workers you have, you can also control the orchestration logic that dictates how aggressively Temporal dispatches tasks.

Configurations like `entry_workflow_batch_concurrency` and `entry_concurrency_target` act as traffic lights. **Crucially, these limits apply *per upload*, not globally.**

```yaml
temporal:
  # Max concurrent batches processed simultaneously per upload
  entry_workflow_batch_concurrency: 5
  # Max concurrent entries processed within a single batch per upload
  entry_concurrency_target: 50
  # Entries grouped into one process-entry activity invocation
  entry_activity_batch_size: 5
```

* **Defaults are usually sufficient:** For most workloads, these limits keep workers well-saturated.
* **Tuning for Backpressure:** Because these limits multiply by the number of active uploads, they can quickly scale. If 100 users upload data simultaneously with the default settings, Temporal could attempt to run roughly 25,000 concurrent entries (`100 uploads * 5 batch workflows * 50 entry target`). If this massive spike causes your downstream infrastructure (like MongoDB, Elasticsearch, or your network) to timeout or crash, you should **decrease** these concurrency values. Lowering them forces tasks to wait safely in the queue, applying backpressure and keeping the overall system stable.
* **Batch size tradeoff:** `entry_activity_batch_size` controls how much work is grouped into each activity. Larger values reduce Temporal scheduling overhead, but make each activity heavier and increase retry blast radius if it fails.

---

### 4. Tuning for Specific Workloads

#### Scenario A: High Volume of Tiny Files (I/O Bound)

Processing thousands of tiny files is typically very fast computationally, but tasks spend most of their time waiting on database reads/writes or network latency.

* **Behavior:** Worker CPUs sit mostly idle while waiting for I/O.
* **How to tune:** The default configurations will usually keep workers saturated. If you want to increase throughput, benchmark adding more replicas to widen your I/O pipeline. If your backend databases (Mongo/Elasticsearch) start timing out under the load of many parallel uploads, **lower** `entry_workflow_batch_concurrency` and `entry_concurrency_target` to throttle the system.

#### Scenario B: Computationally Heavy Processing (CPU Bound)

Dense calculations, heavy parsers, or complex normalizers will quickly peg a CPU core to 100%.

* **Behavior:** The worker machine's CPU becomes the absolute bottleneck.
* **How to tune:** Rely on the `target_cpu_usage: 0.8` setting so the worker naturally backs off when busy. Keep `pool_size` conservative (often `1`) and scale horizontally with replicas first. Increase `pool_size` only if a single worker process is not already saturating CPU and you have enough memory headroom. If CPU-heavy tasks are unstable, timing out, or causing long retries, also try decreasing `entry_activity_batch_size` so each activity does less work.

#### Scenario C: Memory-Intensive Processing

Workloads involving large datasets or trajectories that must be loaded entirely into RAM.

* **Behavior:** High risk of sudden Out-Of-Memory (OOM) crashes.
* **How to tune:** This scenario requires strict isolation. Favor higher replica counts with very low `pool_size` limits (even a `pool_size: 1`). This ensures that if a massive dataset causes an unavoidable OOM spike, it only kills one isolated replica rather than a pooled worker that is concurrently processing other users' data. Rely heavily on strict Kubernetes memory limits combined with NOMAD's `target_memory_usage: 0.7` to reject tasks gracefully when RAM gets tight.

### Limiting the use of threads

You can also reduce the usable threads that Python packages based on OpenMP could use to
reduce the threads that might be spawned by a single worker process. Simply set the `OMP_NUM_THREADS`
environment variable in the worker container in your `docker-compose.yml`:

```yml
services:
    worker:
        ...
        environment:
            ...
            OMP_NUM_THREADS: 1
```

## Controlling access to your Oasis

By default, a NOMAD Oasis mirrors the configuration of the central NOMAD service: it is designed for open data sharing.
While network-level access depends on your firewall and hosting setup,
the application itself allows users to interact with the API according to a configurable scope-based authorization system.

Access control can therefore be configured on several levels:

1. Network level — restrict access via firewall, VPN, or private network.
2. Authentication level — require users to log in before accessing the API.
3. Authorization level — control which operations users are allowed to perform after login.

You can learn more about [authentication and authorization in our explanation-section](../../explanation/auth.md#authentication-and-authorization).

The authentication and authorization settings for individual NOMAD deployments are configurable through the [auth configuration section](../../reference/config.md#auth)  in `nomad.yaml` and the following sections demonstrate its usage.

### Require authentication

By default, authentication is **not required**.
This means anonymous users can still access the API with [limited and configurable permissions](#configure-unauthenticated-user-permissions).
To require authentication for all API requests, enable the following option:

```yaml
auth:
  require_authentication: true
```

When this option is enabled, all requests must include a valid authentication token.
Otherwise the API will return:

```text
HTTP 401 Unauthorized
```

#### Restricting access to specific users

The `authorized_users` is a list of usernames (case-insensitive).
If specified, only these users are considered to be fully authorized for access.

```yaml
auth:
  authorized_users:
    - alice
    - bob
```

If this option is set, only the listed users are considered fully authorized.
You could [configure how unauthorized users are handled](#configure-unauthorized-user-permissions).

### Configure scope-based authorization

After authentication, NOMAD determines **which actions the user is allowed to perform** using scopes.

Scopes support glob-style configuration with wildcards support:

```text
*:read  # read-only access to all resources
*:*     # full access
```

```yaml
auth:
  unauthenticated_user_scopes:
    include:
      - "*:read"
    exclude:
      - "uploads:read"
```

Semantics:

- `include` defines the baseline scopes
- `exclude` removes scopes from that baseline (with higher precedence than `include`)
- wildcards are supported

!!! note
    Partial wildcard patterns such as `u*:read` are **not** supported.

[All available scopes](../../explanation/auth.md#authorization-via-scopes) are defined in the `nomad.auth.scopes.Scope` enum.

When an API endpoint is called, the backend checks whether the user has the required scopes.
If required scopes are missing, the API returns:

```text
HTTP 403 Forbidden
Missing scopes: [...]
```

#### Configure unauthenticated user permissions

When authentication is not required, anonymous users receive a configurable set of scopes.

By default this is read-only access:

```yaml
auth:
  unauthenticated_user_scopes:
    include:
      - "*:read"
```

This allows anonymous users to browse published data but prevents modifications.

#### Configure unauthorized user permissions

Users who successfully authenticate but are not in the `authorized_users` whitelist
are handled according to the `reject_unauthorized_users` setting.

When enabled (`reject_unauthorized_users: true`), unauthorized users will be rejected with:

```text
HTTP 403 Forbidden
```

Otherwise (`reject_unauthorized_users: false`), unauthorized users can still access
the Oasis but only with restricted access, configurable via:

```yaml
auth:
  unauthorized_user_scopes:
    include:
      - "*:read"
```

### Example configurations

#### Read-only public Oasis (default)

Anyone can access read-only endpoints without logging in.
Logged-in users can still use whatever scopes their token grants.

```yaml
auth:
  require_authentication: false
  unauthenticated_user_scopes:
    include:
      - "*:read"
```

#### Public read-only Oasis with privileged whitelist

Anyone can read, but only specific whitelisted users can use their full authenticated scopes.

```yaml
auth:
  require_authentication: false
  reject_unauthorized_users: false
  unauthenticated_user_scopes:
    include:
      - "*:read"
  unauthorized_user_scopes:
    include:
      - "*:read"
  authorized_users:
    - alice
    - bob
```

#### Fully Restricted Oasis

Only explicitly whitelisted users can access the system, and login is mandatory.

```yaml
auth:
  require_authentication: true
  reject_unauthorized_users: true
  authorized_users:
    - alice
    - bob
```

## User management

### Using the central user management

Our recommendation is to use the central user management provided by `nomad-lab.eu`. We
simplified its use and you can use it out-of-the-box. You can even run your system
from `localhost` (e.g. for initial testing). The central user management system is not
communicating with your Oasis directly. Therefore, you can run your Oasis without
exposing it to the public internet.

There are two requirements. First, your users must be able to reach the Oasis. If a user is
logging in, she/he is redirected to the central user management server and after login,
she/he is redirected back to the Oasis. These redirects are executed by your user's browser
and do not require direct communication.

Second, your Oasis must be able to request (via HTTP) the central user management and central NOMAD
installation. This is necessary for non JWT-based authentication methods and to
retrieve existing users for data-sharing features.

The central user management will make future synchronizing data between NOMAD installations easier
and generally recommend to use the central system.
But in principle, you can also run your own user management. See the section on
[your own user management](#provide-and-connect-your-own-user-management).

### Provide and connect your own user management

NOMAD uses [keycloak](https://www.keycloak.org/){:target="_blank" rel="noopener"} for its user management. NOMAD uses
keycloak in two ways. First, the user authentication uses the OpenID Connect/OAuth interfaces provided by keycloak.
Second, NOMAD uses the keycloak realm-management API to get a list of existing users.
Keycloak is highly customizable and numerous options to connect keycloak to existing
identity providers exist.

This tutorial assumes that you have some understanding of what keycloak is and
how it works.

Start with the current distribution template, not a separate full Compose example.
You can connect an existing Keycloak deployment or add a service to your distribution.
For hosting Keycloak, follow the
[Keycloak server guides](https://www.keycloak.org/guides#server){:target="_blank" rel="noopener"}
for your chosen version, including production database, hostname, TLS, and proxy settings.

#### Configure a realm and client

- Create a realm for your Oasis and a client matching `keycloak.client_id`
  (`nomad_public` by default).
- Configure the client's valid redirect URIs and web origins for your Oasis URL.
  Enable the authentication flows required by your users and API clients.
- Create a user for NOMAD's realm-management operations with the `view-users` role
  from `realm-management`, so NOMAD can retrieve users for sharing data.
- Use unique credentials and require HTTPS in production.

#### Configure NOMAD

Merge the following into `configs/nomad.yaml`, replacing the example values:

```yaml
oasis:
  uses_central_user_management: false

keycloak:
  server_url: https://auth.example.org
  public_server_url: https://auth.example.org
  realm_name: oasis
  client_id: nomad_public
  username: nomad-service-user
```

`server_url` must be reachable from the NOMAD containers. `public_server_url` must
be reachable from users' browsers. Include any path prefix your Keycloak server
actually uses; modern Keycloak deployments do not use `/auth` by default.

Supply the realm-management user's password through `NOMAD_KEYCLOAK_PASSWORD` in
`.env` rather than committing it to your repository. Ensure this environment file
is passed to the app and worker services. Set `NOMAD_KEYCLOAK_CLIENT_SECRET` as well
if your client requires a secret. Rebuild the image or enable the local
`nomad.yaml` mount as described above, then recreate affected services.

#### Configure NORTH

The separate NORTH service has its own OAuth configuration. Update `.env.north`
to use your Keycloak deployment:

```sh
KEYCLOAK_URL="https://auth.example.org"
KEYCLOAK_REALM="oasis"
OAUTH_CLIENT_ID="nomad_public"
```

Set `OAUTH_CLIENT_SECRET` if required by the client. Keep the `north` service's
`OAUTH_CALLBACK_URL` aligned with your public Oasis URL, for example
`https://oasis.example.org/backend/north/hub/oauth_callback`, and allow that exact
callback in Keycloak. Both NORTH and users' browsers must be able to reach Keycloak.

If you proxy Keycloak through the Oasis nginx service, add the required location to
your template-based proxy configuration and configure Keycloak's hostname and proxy
headers accordingly. An independently hosted Keycloak does not require such a location.

## Further steps

This is an incomplete list of potential things to customize your NOMAD experience.

- Learn [how to develop plugins](../plugins/plugins.md) that can be installed in an Oasis
- Write YAML based [schemas](../schemas/define.md) and [ELNs](../schemas/define.md#annotate-for-the-gui)
- Learn how to use the [tabular parser](../schemas/tabular.md) to manage data from XLS or CSV
- Add specialized [NORTH tools](../plugins/types/north_tools.md)
