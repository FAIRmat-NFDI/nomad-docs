# How to configure an Oasis

## Configuration files

The [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"}
provides all the neccessary configuration files. We strongly recommend to create your own distribution
project based on the template. This will allow you to version your configuration, build custom
images with plugins, and much more.

In this section, you can learn about settings that you might need to change. The most relevant config files are:

- `docker-compose.yaml`
- `configs/nomad.yaml`
- `configs/nginx.conf`

All docker containers are configured via docker-compose and the respective `docker-compose.yaml` file.
The other files are mounted into the docker containers.

### docker-compose.yaml

The most basic `docker-compose.yaml` to run an Oasis looks like this:

```yaml
--8<-- "docs/howto/oasis/data/docker-compose/nomad-oasis/docker-compose.yaml"
```

Changes necessary:

- The group in the value of the hub's user parameter needs to match the docker group
  on the host. This should ensure that the user which runs the hub, has the rights to access the host's docker.
- On Windows or macOS computers you have to run the `app` and `worker` container without `user: '1000:1000'` and the `north` container with `user: root`.

A few things to notice:

- The app, worker, and north service use the NOMAD docker image. Here we use the `latest` tag, which
  gives you the latest *beta* version of NOMAD. You might want to change this to `stable`,
  a version tag (format is `vX.X.X`, you find all releases at [nomad-FAIR > tags](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/tags){:target="_blank" rel="noopener"}), or a specific [nomad-FAIR > branches](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/branches){:target="_blank" rel="noopener"}.
- All services use docker volumes for storage. This could be changed to host mounts.
- It mounts two configuration files that need to be provided (see below): `nomad.yaml`, `nginx.conf`.
- The only exposed port is `80` (proxy service). This could be changed to a desired port if necessary.
- The NOMAD images are pulled from our GitLab at MPCDF, the other services use images from a public registry (*dockerhub*).
- All containers will be named `nomad_oasis_*`. These names can be used later to reference the container with the `docker` cmd.
- The services are setup to restart `always`, you might want to change this to `no` while debugging errors to prevent indefinite restarts.
- Make sure that the `PWD` environment variable is set. NORTH needs to create bind mounts that require absolute paths and we need to pass the current working directory to the configuration from the PWD variable (see hub service in the `docker-compose.yaml`).
- The `north` service needs to run docker containers. We have to use the systems docker group as a group. You might need to replace `991` with your
  systems docker group id.

### nomad.yaml

NOMAD app and worker read the `nomad.yaml` for configuration.

```yaml
--8<-- "docs/howto/oasis/data/docker-compose/nomad-oasis/configs/nomad.yaml"
```

You should change the following:

- Replace `localhost` with the hostname of your server, and user-management will redirect your
  users back to this host. Make sure this is the hostname that your users can access.
- Replace `deployment`, `deployment_url`, and `maintainer_email` with representative values.
  The `deployment_url` should be the URL to the deployment's api (should end with `/api`).
- To enable the *log transfer* set `logtransfer.enable: true` ([data privacy notice above](#sharing-data-through-log-transfer-and-data-privacy-notice)).
- You can change `api_base_path` to run NOMAD under a different path prefix.
- You should generate your own `north.jupyterhub_crypt_key`. You can generate one
  with `openssl rand -hex 32`.
- On Windows or macOS, you have to add `hub_connect_ip: 'host.docker.internal'` to the `north` section.

A few things to notice:

- Under `mongo` and `elastic` you can configure database and index names. This might
  be useful, if you need to run multiple NOMADs with the same databases.
- All managed files are stored under `.volumes` of the current directory.

### nginx.conf

The GUI container serves as a proxy that forwards requests to the app container. The
proxy is an nginx server and needs a configuration similar to this:

```none
--8<-- "docs/howto/oasis/data/docker-compose/nomad-oasis/configs/nginx.conf"
```

A few things to notice:

- It configures the base path (`nomad-oasis`). It needs to be changed, if you use a different base path.
- You can use the server for additional content if you like.
- `client_max_body_size` sets a limit to the possible upload size.

You can add an additional reverse proxy in front or modify the `nginx` in the `docker-compose.yaml`
to [support https](http://nginx.org/en/docs/http/configuring_https_servers.html){:target="_blank" rel="noopener"}.
If you operate the GUI container behind another proxy, keep in mind that your proxy should
not buffer requests/responses to allow streaming of large requests/responses for `api/v1/uploads` and `api/v1/.*/download`.
An `nginx` reverse proxy location on an additional reverse proxy, could have these directives
to ensure the correct HTTP headers and allow the download and upload of large files:

```nginx
client_max_body_size 35g;
proxy_set_header Host $host;
proxy_pass_request_headers on;
proxy_buffering off;
proxy_request_buffering off;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_pass http://<your-oasis-host>/nomad-oasis;
```

## Starting and stopping NOMAD services

If you prepared the above files, simply use the usual `docker compose` commands to start everything.

To make sure you have the latest docker images for everything, run this first:

```sh
docker compose pull
```

In the beginning and to simplify debugging, it is recommended to start the services separately:

```sh
docker compose up -d mongo elastic rabbitmq
docker compose up app worker gui
```

The `-d` option runs container in the background as *daemons*. Later you can run all at once:

```sh
docker compose up -d
```

Running all services also contains NORTH. When you use a tool in NORTH for the first time,
your docker needs to pull the image that contains this tool. Be aware that this might take longer
than timeouts allow and starting a tool for the very first time might fail.

You can also use docker to stop and remove faulty containers that run as *daemons*:

```sh
docker stop nomad_oasis_app
docker rm nomad_oasis_app
```

You can wait for the start-up with `curl` using the apps `alive` endpoint:

```sh
curl http://<your host>/nomad-oasis/alive
```

If everything works, the GUI should be available under:

```none
http://<your host>/nomad-oasis/gui/
```

If you run into problems, use the dev-tools of your browser to check the javascript logs
or monitor the network traffic for HTTP 500/400/404/401 responses.

To see if at least the api works, check

```none
http://<your host>/nomad-oasis/alive
http://<your host>/nomad-oasis/api/info
```

To see logs or "go into" a running container, you can access the individual containers
with their names and the usual docker commands:

```sh
docker logs nomad_oasis_app
```

```sh
docker exec -ti nomad_oasis_app /bin/bash
```

If you want to report problems with your Oasis. Please provide the logs for

- nomad_oasis_app
- nomad_oasis_worker
- nomad_oasis_gui

## Plugins

[Plugins](../plugins/plugins.md) allow the customization of a NOMAD deployment in terms of
which search apps, normalizers, parsers and schema packages are available. In order for these
customization to be activated, they have to be configured and installed into an Oasis.
The basic template comes with a core set of plugins. If you want to configure
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

The NOMAD Oasis installation with your own keyloak is very similar to the regular docker-compose
installation above. There are just a three changes.

- The `docker-compose.yaml` has an added keycloak service.
- The `nginx.conf` is also modified to add another location for keycloak.
- The `nomad.yaml` has modifications to tell Oasis to use your and not the official NOMAD keycloak.

You can start with the regular installation above and manually adopt the config or
download the already updated configuration files: [nomad-oasis-with-keycloak.zip](./data/nomad-oasis-with-keycloak.zip).
The download also contains an additional `configs/nomad-realm.json` that allows you
to create an initial keycloak realm that is configured for NOMAD automatically.

First, the `docker-compose.yaml`:

```yaml
--8<-- "docs/howto/oasis/data/docker-compose/nomad-oasis-with-keycloak/docker-compose.yaml"
```

A few notes:

- You have to change the `KEYCLOAK_FRONTEND_URL` variable to match your host and set a path prefix.
- The environment variables on the keycloak service allow to use keycloak behind the nginx proxy with a path prefix, e.g. `keycloak`.
- By default, keycloak will use a simple H2 file database stored in the given volume. Keycloak offers many other options to connect SQL databases.
- We will use keycloak with our nginx proxy here, but you can also host-bind the port `8080` to access keycloak directly.
- We mount and use the downloaded `configs/nomad-realm.json` to configure a NOMAD compatible realm on the first startup of keycloak.

Second, we add a keycloak location to the nginx config:

```nginx
--8<-- "docs/howto/oasis/data/docker-compose/nomad-oasis-with-keycloak/configs/nginx.conf"
```

A few notes:

- Again, we are using `keycloak` as a path prefix. We configure the headers to allow
  keycloak to pick up the rewritten url.

Third, we modify the keycloak configuration in the `nomad.yaml`:

```yaml
--8<-- "docs/howto/oasis/data/docker-compose/nomad-oasis-with-keycloak/configs/nomad.yaml"
```

You should change the following:

- There are two urls to configure for keycloak. The `server_url` is used by the NOMAD
  services to directly communicate with keycloak within the docker network. The `public_server_url`
  is used by the UI to perform the authentication flow. You need to replace `localhost`
  in `public_server_url` with `<yourhost>`.

A few notes:

- The particular `admin_user_id` is the Oasis admin user in the provided example realm
  configuration. See below.

If you open `http://<yourhost>/keycloak/auth` in a browser, you can access the admin
console. The default user and password are `admin` and `password`.

Keycloak uses `realms` to manage users and clients. A default NOMAD compatible realm
is imported by default. The realm comes with a test user and password `test` and `password`.

A few notes on the realm configuration:

- Realm and client settings are almost all default keycloak settings.
- You should change the password of the admin user in the NOMAD realm.
- The admin user in the NOMAD realm has the additional `view-users` client role for `realm-management`
  assigned. This is important, because NOMAD will use this user to retrieve the list of possible
  users for managing co-authors and reviewers on NOMAD uploads.
- The realm has one client `nomad_public`. This has a basic configuration. You might
  want to adapt this to your own policies. In particular you can alter the valid redirect URIs to
  your own host.
- We disabled the https requirement on the default realm for simplicity. You should change
  this for a production system.

## Sharing data through log transfer and data privacy notice

NOMAD includes a *log transfer* functions. When enabled this automatically collects
and transfers non-personalized logging data to us. Currently, this functionality is experimental
and requires opt-in. However, in upcoming versions of NOMAD Oasis, we might change to opt-out.

To enable this functionality add `logtransfer.enabled: true` to you `nomad.yaml`.

The service collects log-data and aggregated statistics, such as the number of users or the
number of uploaded datasets. In any case this data does not personally identify any users or
contains any uploaded data. All data is in an aggregated and anonymized form.

The data is solely used by the NOMAD developers and FAIRmat, including but not limited to:

- Analyzing and monitoring system performance to identify and resolve issues.
- Improving our NOMAD software based on usage patterns.
- Generating aggregated and anonymized reports.

We do not share any collected data with any third parties.

We may update this data privacy notice from time to time to reflect changes in our data practices.
We encourage you to review this notice periodically for any updates.

## Further steps

This is an incomplete list of potential things to customize your NOMAD experience.

- Learn [how to develop plugins](../plugins/plugins.md) that can be installed in an Oasis
- Write YAML based [schemas](../manage/gui/yaml.md) and [ELNs](../manage/gui/elns.md)
- Learn how to use the [tabular parser](../manage/gui/tabular.md) to manage data from XLS or CSV
- Add specialized [NORTH tools](../manage/gui/north.md)
