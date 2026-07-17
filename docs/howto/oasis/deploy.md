# How to deploy an Oasis

Once you have configured your NOMAD Oasis through a distribution project as described in the [configuration how-to](./configure.md), it is time to deploy it. An instance of a NOMAD distribution that is running on a particular machine is called a [deployment](../../reference/glossary.md#deployment-nomad-oasis). This document contains information about the basic requirements and available alternatives for deploying your NOMAD Oasis.

## Hardware considerations

The hardware requirements depend on the volume of data you need to manage and process, the number of concurrent users you have, and how many concurrent remote tools you are running. The following subsections go more into detail about the hardware choices but the minimum recommended hardware is:

- 4 CPU cores
- 8 GB RAM
- 30 GB disk space

### CPU

The amount of compute resource (e.g. processor cores) is a matter of convenience (and amount of expected users). Four CPU cores are typically sufficient to support a research group and run application, processing, and databases in parallel. Smaller systems still work, e.g. for testing.

### RAM

There should be enough RAM to run databases, application, and processing at the same time. The minimum requirements here can be quite low, but for processing the metadata for individual files is kept in memory. For large DFT geometry-optimizations this can add up quickly, especially if many CPU cores are available for processing entries in parallel. We recommend at least 2GB per core and a minimum of 8GB. You also need to consider RAM and CPU for running tools like Jupyter, if you opt to use NOMAD NORTH.

### Storage

NOMAD keeps all files that it manages as they are. The files that NOMAD processes in addition (e.g. through parsing) are typically smaller than the original raw files. Therefore, you can base your storage requirements based on the size of the data files that you expect to manage. The additional MongoDB database and Elasticsearch index is comparatively small. A minimum storage size of 30GB is enough to host the required docker images and also to run the databases without hitting any [disk-usage watermark errors](https://www.elastic.co/guide/en/elasticsearch/reference/current/fix-watermark-errors.html){:target="_blank" rel="noopener"}.

Storage speed is another consideration. NOMAD can work with NAS systems. All that NOMAD needs is a POSIX-compliant filesystem as an interface. So everything you can (e.g. Docker host) mount should be compatible. For processing data obviously relies on read/write speed, but this is just a matter of convenience. The processing is designed to run as managed asynchronous tasks. Local storage might be favorable for MongoDB and Elasticsearch operation, but it is not a must.

## Deployment alternatives

NOMAD is designed so that it can be run either on a single machine using `docker-compose` or then can be scaled to using several virtual machines using `kubernetes`. The single machine setup with `docker-compose` is more typical for an Oasis as it is easier to get running and in many cases a single machine can deal with the computational load. The setup with `kubernetes` requires a bit more work but becomes important once you need to scale the service to deal with more processing, more simultaneous remote tools and so on.

### `docker-compose`

For the single-machine setup with `docker-compose`, the [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"} provides a basic `docker-compose.yaml` file and a set of instructions in `README.md` for booting up all of the service.

### `Kubernetes`

NOMAD can be deployed on Kubernetes using the official [Helm](https://helm.sh/){:target="_blank" rel="noopener"} chart from [nomad-helm-charts](https://github.com/FAIRmat-NFDI/nomad-helm-charts){:target="_blank" rel="noopener"}. The [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"} provides a ready-to-use `kubernetes/values.yaml` as a starting point for single-node clusters (Minikube, Kind, k3s, etc.).

#### Prerequisites

[Helm](https://helm.sh/docs/intro/install/){:target="_blank" rel="noopener"} >= 3.x, [kubectl](https://kubernetes.io/docs/tasks/tools/){:target="_blank" rel="noopener"}, and a running Kubernetes cluster.

#### Installation

1. Add the NOMAD Helm repository:

    ```sh
    helm repo add nomad https://fairmat-nfdi.github.io/nomad-helm-charts
    helm repo update
    ```

2. Install using the values file provided in the distro template:

    ```sh
    helm install nomad-oasis nomad/default -f kubernetes/values.yaml --timeout 15m
    ```

3. Watch the pods come up and wait until all are ready:

    ```sh
    kubectl get pods -w
    ```

4. Access the Oasis via port-forward:

    ```sh
    kubectl port-forward svc/nomad-oasis-proxy 80:80
    ```

    Then open `http://localhost/nomad-oasis` in your browser.

#### Configuration

All configuration lives under the `nomad` key in your values file. See the [`nomad-helm-charts` documentation](https://github.com/FAIRmat-NFDI/nomad-helm-charts#configuration){:target="_blank" rel="noopener"} for a detailed breakdown of available options.

**Example values files**

Rather than writing a values file from scratch, you can use one of the ready-made examples as a starting point:

| File | Where | Best for |
| --- | --- | --- |
| `kubernetes/values.yaml` | [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"} | Single-node clusters (Minikube, Kind, k3s). No persistence, uses `hostPath`. Includes JupyterHub (NORTH). Uses the distro-template image. |
| `custom-values/minikube.yaml` | [`nomad-helm-charts`](https://github.com/FAIRmat-NFDI/nomad-helm-charts){:target="_blank" rel="noopener"} | Minikube specifically. Reduced resource requests, hostname set to `nomad-oasis.local`, nginx ingress enabled. |
| `custom-values/kind.yaml` | [`nomad-helm-charts`](https://github.com/FAIRmat-NFDI/nomad-helm-charts){:target="_blank" rel="noopener"} | Kind specifically. Similar to the Minikube file but with `localhost` as hostname and longer health-check timeouts to account for Kind's slower image pull behaviour. |
| `custom-values/aws.yaml` | [`nomad-helm-charts`](https://github.com/FAIRmat-NFDI/nomad-helm-charts){:target="_blank" rel="noopener"} | AWS EKS. Enables persistence with EFS (`ReadWriteMany`) for NOMAD volumes and `gp2` EBS for databases. Configures an ALB ingress controller. |

All files can be layered — pass multiple `-f` flags to Helm to merge them, with later files taking precedence:

```sh
helm install nomad-oasis nomad/default \
  -f kubernetes/values.yaml \
  -f my-overrides.yaml \
  --timeout 15m
```

#### Secrets

The chart supports multiple methods for managing secrets:

**Method 1: Pre-created Kubernetes Secrets (Production)**

```yaml
nomad:
  secrets:
    api:
      existingSecret: "my-api-secret"
      key: password
```

Create the secret manually:

```bash
kubectl create secret generic my-api-secret --from-literal=password=$(openssl rand -hex 32)
```

**Method 2: Values File (Development)**

```yaml
nomad:
  secrets:
    api:
      value: "my-secret-value"
```

**Method 3: Auto-generate (Default)**

```yaml
nomad:
  secrets:
    api:
      autoGenerate: true
```

**Method 4: Separate secrets.yaml File**
Create a `secrets.yaml` file (keep out of git):

```yaml
nomad:
  secrets:
    api:
      value: "my-api-secret-here"
    keycloak:
      clientSecret:
        value: "keycloak-client-secret"
      password:
        value: "keycloak-password"
```

Install with both files:

```bash
helm install nomad-oasis nomad/default -f values.yaml -f secrets.yaml
```

**Method 5: Environment Variables with --set**

```bash
helm install nomad-oasis nomad/default \
  -f values.yaml \
  --set nomad.secrets.api.value="${NOMAD_API_SECRET}"
```

**Method 6: helm-secrets Plugin**

```bash
# Encrypt secrets with SOPS
sops -e secrets.yaml > secrets.enc.yaml

# Install with encrypted secrets
helm secrets install nomad-oasis nomad/default -f values.yaml -f secrets://secrets.enc.yaml
```

#### Required Secrets for Production

The following secrets are used by the NOMAD Oasis deployment. None of the followings are, by default, generated, and we recommend explicitly setting them for a production environment to ensure stability across upgrades.

- **`nomad.secrets.api`**: The fundamental API secret for cryptographic operations. **Required.** (Must be provided or `nomad.secrets.api.autoGenerate` set to `true` to avoid installation failure).
- **`nomad.secrets.north.hubServiceApiToken`**: Required if JupyterHub (NORTH) is enabled (`nomad.config.north.enabled: true`).
- **`nomad.secrets.keycloak.password` & `clientSecret`**: Required if using a local standalone Keycloak instance or institution SSO.
- **`nomad.secrets.datacite`**: Required if DataCite DOI minting is enabled.
- **`mongodb.auth.rootPassword`**: Root password for the internal MongoDB database. If left empty, the Bitnami chart auto-generates a random password on first boot, but it is highly recommended to set it manually.

*Example: Providing the NORTH hub token manually (Method 1):*

```sh
kubectl create secret generic nomad-hub-token --from-literal=token='<your-token>'
```

```yaml
nomad:
  secrets:
    north:
      hubServiceApiToken:
        existingSecret: "nomad-hub-token"
        key: token
```

#### Storage and Persistent Volumes

Storage is one of the most important architectural decisions when deploying NOMAD on Kubernetes, and the right approach depends entirely on whether all pods run on the same physical node or are spread across multiple nodes.

**What NOMAD stores on disk**

NOMAD uses five named data volumes, each mounted by one or more pods simultaneously:

| Volume | Mount path in container | Mounted by | Contents |
| --- | --- | --- | --- |
| `public` | `/app/.volumes/fs/public` | `app`, `worker`, `cpuworker`, `gpuworker`, `jupyterhub` | Published upload files |
| `staging` | `/app/.volumes/fs/staging` | `app`, `worker`, `cpuworker`, `gpuworker`, `jupyterhub` | In-progress uploads being parsed and processed |
| `nomad` | `/nomad` | `app`, `worker` | Other NOMAD internal shared data |
| `north-home` | `/app/.volumes/fs/north/users` | `app`, `jupyterhub` | JupyterHub (NORTH) per-user home directories |
| `tmp` | *(internal)* | `app`, `worker`, `cpuworker`, `gpuworker` | Temporary shared scratch space |

MongoDB, Elasticsearch, and PostgreSQL each manage their own separate storage volumes through their respective subcharts.

**Single-node: `hostPath` (default)**

When `nomad.persistence.enabled` is `false` (the default in `kubernetes/values.yaml`), the chart mounts all five volumes as [`hostPath`](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath){:target="_blank" rel="noopener"} volumes — each pod reads and writes directly from a path on the underlying Kubernetes node's filesystem. No storage provisioner is needed.

This works correctly only because, on a single-node cluster, every pod always schedules on the same machine and therefore sees the same local directories. The host paths come from the `nomad.config.fs` section:

```yaml
nomad:
  config:
    fs:
      public_external: /app/.volumes/fs/public
      staging_external: /app/.volumes/fs/staging
      north_home_external: /app/.volumes/fs/north/users
      nomad: /nomad
  persistence:
    enabled: false # uses hostPath — no PVCs are created
```

!!! warning
    The directories above must exist on the node and be writable by UID 1000 (the user the NOMAD containers run as) before the pods start. Create them manually:
    ```sh
    sudo mkdir -p /app/.volumes/fs/{public,staging,north/users} /nomad
    sudo chown -R 1000:1000 /app/.volumes/fs /nomad
    ```
    Missing directories are a common cause of `CrashLoopBackOff` errors on fresh single-node deployments.

**Multi-node: PersistentVolumeClaims**

Once workers or app replicas are scheduled across more than one node, `hostPath` breaks down: each node has its own local filesystem, so pod A on node 1 and pod B on node 2 would see completely different data. Setting `nomad.persistence.enabled: true` tells the chart to create [`PersistentVolumeClaims`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/){:target="_blank" rel="noopener"} (PVCs) instead, backed by a shared network storage provider.

```yaml
nomad:
  persistence:
    enabled: true
    storageClass: "your-storage-class"
    accessMode: ReadWriteMany # required for multi-node — see below

    public:
      size: 50Gi
    staging:
      size: 50Gi
    nomad:
      size: 100Gi
    north-home:
      size: 10Gi
    tmp:
      size: 20Gi
```

**Access modes: the critical distinction**

The [`accessMode`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes){:target="_blank" rel="noopener"} on a PVC controls how many nodes can mount the volume at the same time:

- **`ReadWriteOnce` (RWO)** — the volume can only be mounted by pods on a *single node* at a time. This is the standard mode for block storage (e.g. AWS EBS `gp2`, GCE persistent disk) and is perfectly fine for databases and for NOMAD on a single-node cluster.

- **`ReadWriteMany` (RWX)** — the volume can be mounted simultaneously by pods on *any number of nodes*. This is required for `public`, `staging`, `nomad`, and `north-home` in a multi-node setup, because both the `app` and `worker` deployments mount these volumes concurrently and can land on different nodes.

!!! warning "Using RWO for shared NOMAD volumes in a multi-node cluster will cause failures"
    If you configure `ReadWriteOnce` for the shared NOMAD volumes and scale workers across multiple nodes, the scheduler will either refuse to start pods on a second node (because the block device is already bound to another node) or, in rare race conditions, allow concurrent writes without coordination, risking data corruption. Always use `ReadWriteMany` for the NOMAD application volumes in any multi-node deployment.

**Choosing a storage class for `ReadWriteMany`**

Not all storage backends support `ReadWriteMany`. Common choices per environment:

| Environment | RWX storage option |
| --- | --- |
| AWS EKS | Amazon EFS with the [EFS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html){:target="_blank" rel="noopener"} |
| GCP GKE | [Filestore](https://cloud.google.com/filestore){:target="_blank" rel="noopener"} NFS volumes |
| Azure AKS | [Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/){:target="_blank" rel="noopener"} storage class |
| On-premises | NFS server, [Longhorn](https://longhorn.io/){:target="_blank" rel="noopener"}, [Ceph RBD/CephFS](https://rook.io/){:target="_blank" rel="noopener"} |
| Local dev (single-node only) | [Local Path Provisioner](https://github.com/rancher/local-path-provisioner){:target="_blank" rel="noopener"} (RWO — not suitable for multi-node) |

For AWS, the chart's `aws.yaml` values file uses EFS for NOMAD volumes and `gp2` (RWO block storage) for the databases, since each database runs as a single pod:

```yaml
nomad:
  persistence:
    enabled: true
    storageClass: "nomad-efs-sc" # EFS StorageClass — supports ReadWriteMany
    accessMode: "ReadWriteMany"

mongodb:
  persistence:
    storageClass: "gp2" # EBS block storage — RWO, single pod only

elasticsearch:
  persistence:
    storageClass: "gp2"

postgresql:
  primary:
    persistence:
      storageClass: "gp2"
```

**Using pre-existing volumes**

If you have already provisioned volumes externally (e.g. an existing NFS share or a pre-created PV), you can reference them by name and the chart will skip creating new PVCs:

```yaml
nomad:
  persistence:
    enabled: true
    public:
      existingClaim: "my-existing-public-pvc"
    staging:
      existingClaim: "my-existing-staging-pvc"
    nomad:
      existingClaim: "my-existing-nomad-pvc"
```

### Base Linux (without Docker)

Not recommended. We do not provide official support for this type of installation, but it is possible to run NOMAD without Docker. You can infer the necessary steps from the provided `docker-compose.yaml`.

## Deploying NOMAD on a cloud provider

!!! note

    **Disclaimer:** This guide is an independent tutorial for deploying NOMAD on various cloud providers.
    We are not affiliated with, endorsed by, or funded by any cloud providers mentioned in this document.

Regardless of the cloud provider, the deployment typically follows these steps:

1. Choose the cloud provider and and set up an account

2. Provision compute instances

3. Configure network and security

4. Deploy NOMAD

5. Access and test deployment

### Single node deployment with `docker-compose`

#### Amazon Web Services (AWS)

1. Create an AWS account

    Go to [AWS](https://aws.amazon.com/){:target="_blank" rel="noopener"}. You will need a credit card
    for creating an account.

2. Create an EC2 instance

    EC2 (Elastic Compute Cloud) is Amazon's platform for creating and running virtual machines. To create a new EC2 instance, you need to login to the AWS console and start the process of creating a new EC2 instance. In the EC2 instance settings, pay attention to the following settings:

    - Choose a Linux-based operating system (OS). (e.g. Ubuntu, Amazon Linux, Red Hat, SUSE Linux). This tutorial is based on using Ubuntu.
    - Select an instance type based on your workload ([see appropriate hardware resources](#hardware-considerations)). If you are unsure, you could start with a `c5.xlarge` instance.
    - In network settings, ensure that "Auto-assign public IP" is enabled
    - In network settings, ensure that "Allow HTTPS traffic from the internet" is enabled.
    - In network settings, ensure that "Allow HTTP traffic from the internet" is enabled.
    - In the storage settings, add persistent storage for databases and files stored by NOMAD. The default [EBS (Elastic Block Store)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html){:target="_blank" rel="noopener"} is a recommended option, as it provides durable and scalable storage. Learn more in the [AWS Storage Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html){:target="_blank" rel="noopener"}. We recommend starting with at least 30 GiB of storage to have space for the docker images and databases.
    - Launch the instance

3. Configure Network & Security

    - Check that inbound traffic is allowed in the [*Network & Security/Security Groups*](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html){:target="_blank" rel="noopener"} settings. Inbound traffic should be allowed for:
        - HTTP: Protocol TCP, port 80, source 0.0.0.0/0
        - HTTPS: Protocol TCP, port 443, source 0.0.0.0/0
        - (Optional) SSH: Protocol TCP, port 22, source 0.0.0.0/0

        These rules should have been added during the previous step if you selected to allow HTTP/HTTPS traffic from the internet.

    - Check that the OS firewall (e.g. `ufw` for Ubuntu) is also allowing this traffic.

    - Assign an [Elastic (static) IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html){:target="_blank" rel="noopener"}, as by default [AWS assigns a dynamic public IP that changes upon instance restart](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses){:target="_blank" rel="noopener"}.

    - To enable secure communication with the server, read the guide on [setting up secured connection using HTTPS](#secured-connections-using-https). For testing you can skip this step, but HTTPS communication must be enforced in the final production setup.

4. Deploy NOMAD
    - Connect to the EC2 instance. The easiest way is to use the browser based connection directly from the AWS console. You can alternatively also connect through SSH if you have generated a key pair and have SSH access enabled in the instance settings.

    - Install docker and docker compose on the virtual machine: you can [read more about the installation here](#installing-docker).

    - Ensure that Git is installed to be able to easily sync the distribution configuration. You can check this by running `git --version`. Generic installations instructions are found on [git > Linux](https://git-scm.com/downloads/linux){:target="_blank" rel="noopener"}.

    - Create a NOMAD Oasis distribution using our template [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"}. We recommend creating a new repository by presssing the "Use this template button", but for testing it is also possible to use the existing template repository directly.

    - Follow the deployment instructions in the `README.md` file under *Deploying the distribution/For a new Oasis*. This typically consists of cloning the repository, setting up file priviledges and then running `docker compose pull` + `docker compose up -d`.

5. Access and test deployment

    You should now be able to access the Oasis installation from anywhere using the static IP address or domain name you have configured: `http://<IP-or-domain>/nomad-oasis`. If you have not yet set up secure connections with HTTPS, [read about it here](#secured-connections-using-https).

## Installing Docker

You can find generic [installation instructions here](https://docs.docker.com/engine/install/){:target="_blank" rel="noopener"}. On Ubuntu, you can install docker and docker compose with:

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

You will also want to configure docker to be run as a non-root user using [these steps](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user){:target="_blank" rel="noopener"}. On Ubuntu, this can be done with:

```sh
sudo groupadd docker
sudo usermod -aG docker $USER
```

Note that you may need to reboot to get the docker daemon running and the user priviledges to work.

## Secured connections using HTTPS

Before entering production, you must set up secure connections through HTTPS. Without it any communication with the server is compromised and e.g. credentials and other sensitive data can be stolen. To set up secure connections, follow these steps (the steps focus on the single-node `docker-compose` setup):

1. Ensure that you have a static IP address.
2. Get a TLS certificate

    HTTPS connections require a TLS certificate which also needs to be
    renewed periodically. Depending on your setup, you have several alternatives
    for setting up a certificate:

    1. You already have a certificate.

        In this case you just need the certificate and key files.

    2. Self-signed certificate

        For testing, you can create a [self-signed certificate](https://en.wikipedia.org/wiki/Self-signed_certificate){:target="_blank" rel="noopener"}. These are not viable for a production setup, as they are not trusted e.g. by browsers.

        For detailed instructions, see the "Deploy Oasis with HTTPS" section in the [`nomad-distro-template` documentation](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#for-a-new-oasis){:target="_blank" rel="noopener"}

    3. Free certificate from Let's Encrypt

        [Let's Encrypt](https://letsencrypt.org/){:target="_blank" rel="noopener"} is a non-profit organization that provides free TLS certificats. To create a free certificate you must have a domain name. You can follow their tutorials on creating free certificates.

3. Setup your server to accept HTTPS traffic.
    To enable HTTPS, you need to mount your TLS certificate and ensure that port 443 is open. A template nginx configuration file is available, see the "Deploy Oasis with HTTPS" section of [`nomad-distro-template` documentation](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#for-a-new-oasis){:target="_blank" rel="noopener"}.
