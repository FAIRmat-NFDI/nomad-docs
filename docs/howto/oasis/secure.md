# Secure your Oasis

NOMAD provides a comprehensive set of security features to protect your Oasis. However, properly enabling and configuring these features is the responsibility of the deployment administrator. This guide outlines the key security measures available and best practices for implementing them.

## Authentication and access control

### Single-sign-on

NOMAD uses [Keycloak](https://www.keycloak.org/){:target="_blank" rel="noopener"} as its identity and access management solution. Keycloak provides single-sign-on (SSO) capabilities through the OpenID Connect/OAuth 2.0 protocol. By default, an Oasis can use the central user management provided by nomad-lab.eu, meaning users authenticate against a shared Keycloak instance without requiring an additional local setup. Alternatively, administrators can [deploy their own Keycloak instance](configure.md#provide-and-connect-your-own-user-management) alongside the Oasis, enabling integration with existing institutional identity providers (e.g. LDAP, SAML, or social logins).

### Multi-factor authentication

NOMAD deployments can set up multi-factor authentication (MFA) through a custom Keycloak configuration. When running [your own Keycloak instance](configure.md#provide-and-connect-your-own-user-management), you can enable MFA policies such as time-based one-time passwords (TOTP) or WebAuthn in the Keycloak admin console. Refer to the [Keycloak documentation on MFA](https://www.keycloak.org/docs/latest/server_admin/#authentication-flows){:target="_blank" rel="noopener"} for detailed setup instructions. Note that MFA is not available when using the central nomad-lab.eu user management, as the central instance's authentication policies are managed by FAIRmat.

### Access control

By default, an Oasis works like the official NOMAD: published data is openly accessible and anybody with a NOMAD account can upload and view the data. For deployments that require restricted access, NOMAD provides several mechanisms. To summarize:

- Custom Keycloak: You can [host your own Keycloak instance](configure.md#provide-and-connect-your-own-user-management) which provides you full control over the allowed users, and zero-downtime modifications to user access.
- Network-level restriction: Do not expose the Oasis to the public internet by making it only available on an intranet or through a VPN.
- Setup Oasis-specific rules: See the section on [restricting access to your Oasis](configure.md#restricting-access-to-your-oasis).

## Network security

### HTTPS / TLS

All production Oasis deployments must use HTTPS to protect data that is transmitted during external communication. Without TLS, credentials and other sensitive data such as authentication tokens are transmitted in plaintext and can be intercepted. Such external communication covers:

- User to Oasis communication: User interactions with the GUI and API.
- Authentication flows: OAuth 2.0 token exchange between the browser, Oasis, and Keycloak.

See [Secured connections using HTTPS](deploy.md#secured-connections-using-https) for step-by-step instructions on obtaining a TLS certificate and configuring the reverse proxy to use it.

By default, communication between Docker containers/kubernetes pods within the same network is not encrypted, as it does not traverse external networks. If your threat model requires encrypted inter-service communication, consider using overlay networks with encryption enabled or a service mesh.

### Reverse proxy

NOMAD uses [nginx](https://nginx.org/){:target="_blank" rel="noopener"} as a reverse proxy to direct external traffic to the correct internal service. The nginx proxy is the only component that should be exposed to external traffic. All other services (app, worker, Elasticsearch, MongoDB, Keycloak) should only be reachable from within the Docker/Kubernetes network. Review your `docker-compose.yaml` to ensure that only the nginx service binds to host ports.

### Firewall rules

Administrators should configure the host firewall (e.g. `ufw`, `iptables`, or cloud security groups) to allow only the minimum required inbound traffic:

- TCP 443 (HTTPS) — required
- TCP 80 (HTTP) — only if redirecting to HTTPS
- TCP 22 (SSH) — for server administration, restrict to known IP ranges

All other ports should be blocked from external access.

## Encryption at rest

For data encryption on disks, we recommend using full-disk or volume-level encryption provided by the host operating system or cloud provider (e.g. LUKS on Linux, AWS EBS encryption, Azure Disk Encryption). NOMAD itself stores data in the filesystem (raw files and archive files), MongoDB, and Elasticsearch — all of which write to disk volumes defined in the `docker-compose.yaml`. Enabling encryption at the storage layer ensures that all persisted data is encrypted transparently.

## Secrets management

The `nomad.yaml` file and the Docker/Kubernetes configuration contains values that are sensitive and should not be exposed. The following rules should be followed to prevent such secrets from leaking:

- Do not commit any secrets to version control.
- Always use secrets that are strong against brute-force attacs or X.
- Do not store secrets on disk. Instead use environment variables to pass any secrets to the NOMAD application, and use Docker/Kubernetes secrets.

## Container security

NOMAD runs as a set of Docker containers. To harden your deployment:

- Run containers as non-root: The default NOMAD `docker-compose.yaml` runs the app and worker containers with `user: '1000:1000'`. Avoid running containers as root in production.
- Keep images up to date: Regularly pull updated base images to include the latest security patches.
- Limit container capabilities: Avoid granting unnecessary Linux capabilities or using `--privileged` mode.
- Use read-only filesystems: Where possible, mount container filesystems as read-only and use named volumes only for data that must be written.

## Activity logging

In order to audit activity on the server, NOMAD uses [structlog](https://www.structlog.org/en/stable/){:target="_blank" rel="noopener"} for structured logging across all services. Logs capture system-level events such as processing operations, API requests, and errors.

In a production setting you may want to store and search these logs for later inspection. There are two primary ways for achieving this:

- You can connect the [Elastic stack](https://www.elastic.co/guide/index.html){:target="_blank" rel="noopener"} (ELK) for centralized log collection, search, and monitoring.
- You can also collect server log messages via Docker/Kubernetes logging drivers.

Through these logs you can monitor logs for unusual access patterns or errors.

## Vulnerability detection

NOMAD is composed of several components, each with a separate update and vulnerability lifecycle:

- Python: Dependencies for deployments are managed via `pyproject.toml`. Administrators should regularly check for known vulnerabilities in Python dependencies using tools such as [`pip-audit`](https://pypi.org/project/pip-audit/){:target="_blank" rel="noopener"} or [`safety`](https://pypi.org/project/safety/){:target="_blank" rel="noopener"}.
- Javascript: The NOMAD front-end dependencies are managed via the `package.json` file. These dependencies are regularly checked for known vulnerabilities using [`npm-audit`](https://docs.npmjs.com/cli/v8/commands/npm-audit){:target="_blank" rel="noopener"}.
- Docker images: Docker images are used to deploy different parts of the NOMAD infrastructure. Use container scanning tools such as [Trivy](https://trivy.dev/){:target="_blank" rel="noopener"} or [Grype](https://github.com/anchore/grype){:target="_blank" rel="noopener"} to detect vulnerabilities in the image layers.

The NOMAD team communicates important security updates through the following channels:

- Discord: Security-relevant notifications are found in the `software-updates` channel on our Discord server.
- GitHub repository: Follow the [NOMAD distribution template repository](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"} for update notifications.
- Oasis registration: If you have [registered your Oasis](install.md) with FAIRmat, you may be contacted directly for critical security updates.

## Resiliency and availability

### Backup and disaster recovery

The Oasis administrator is responsible for maintaining a backup of the data. The section on [administering an Oasis](administer.md#backups) contains documentation on creating backups of file data and MongoDB, as well as restoring from backups.

### Service level agreement (SLA)

An individual Oasis can agree on a service level agreement. The NOMAD deployments hosted by FAIRmat are provided as-is without an explicit SLA.
