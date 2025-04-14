# Deploying an Oasis

Once you have configured your NOMAD Oasis through a distribution project as described in the [configuration how-to](./configure.md), it is time to deploy it. This document contains information about the basic requirements and available alternatives for deploying your NOMAD Oasis.

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

NOMAD keeps all files that it manages as they are. The files that NOMAD processes in addition (e.g. through parsing) are typically smaller than the original raw files. Therefore, you can base your storage requirements based on the size of the data files that you expect to manage. The additional MongoDB database and Elasticsearch index is comparatively small. A minimum storage size of 30GB is enough to host the required docker images and also to run the databases without hitting any [disk-usage watermark errors](https://www.elastic.co/guide/en/elasticsearch/reference/current/fix-watermark-errors.html).

Storage speed is another consideration. NOMAD can work with NAS systems. All that NOMAD needs is a POSIX-compliant filesystem as an interface. So everything you can (e.g. Docker host) mount should be compatible. For processing data obviously relies on read/write speed, but this is just a matter of convenience. The processing is designed to run as managed asynchronous tasks. Local storage might be favorable for MongoDB and Elasticsearch operation, but it is not a must.

## Deployment alternatives

NOMAD is designed so that it can be run either on a single machine using `docker-compose` or then can be scaled to using several virtual machines using `kubernetes`. The single machine setup with `docker-compose` is more typical for an Oasis as it is easier to get running and in many cases a single machine can deal with the computational load. The setup with `kubernetes` requires a bit more work but becomes important once you need to scale the service to deal with more processing, more simultaneous remote tools and so on.

### `docker-compose`

For the single-machine setup with `docker-compose`, the [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template) provides a basic `docker-compose.yaml` file and a set of instructions in `README.md` for booting up all of the service.

### kubernetes

!!! warning "Attention"

    This is just preliminary documentation and many details are missing.

There is a NOMAD [Helm](https://helm.sh/) chart. First we need to add the NOMAD Helm chart repository:

```sh
helm repo add nomad https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/helm/latest
```

New we need a minimal `values.yaml` that configures the individual kubernetes resources created by our Helm chart:

```yaml
--8<-- "ops/kubernetes/example-values.yaml"
```

The `jupyterhub`, `mongodb`, `elasticsearch`, `rabbitmq` follow the respective official Helm charts configuration.

Run the Helm chart and install NOMAD:

```sh
helm update --install nomad nomad/nomad -f values.yaml
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

    You can do it [here](https://aws.amazon.com/). You will need a credit card
    for creating an account.

2. Create an EC2 instance

    EC2 (Elastic Compute Cloud) is Amazon's platform for creating and running virtual machines. To create a new EC2 instance, you need to login to the AWS console and start the process of creating a new EC2 instance. In the EC2 instance settings, pay attention to the following settings:

    - Choose a Linux-based operating system (OS). (e.g. Ubuntu, Amazon Linux, Red Hat, SUSE Linux). This tutorial is based on using Ubuntu.
    - Select an instance type based on your workload ([see appropriate hardware resources](#hardware-considerations)). If you are unsure, you could start with a `c5.xlarge` instance.
    - In network settings, ensure that "Auto-assign public IP" is enabled
    - In network settings, ensure that "Allow HTTPS traffic from the internet" is enabled.
    - In network settings, ensure that "Allow HTTP traffic from the internet" is enabled.
    - In the storage settings, add persistent storage for databases and files stored by NOMAD. The default [EBS (Elastic Block Store)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) is a recommended option, as it provides durable and scalable storage. Learn more in the [AWS Storage Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html). We recommend starting with at least 30 GiB of storage to have space for the docker images and databases.
    - Launch the instance

3. Configure Network & Security

    - Check that inbound traffic is allowed in the [*Network & Security/Security Groups*](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) settings. Inbound traffic should be allowed for:
        - HTTP: Protocol TCP, port 80, source 0.0.0.0/0
        - HTTPS: Protocol TCP, port 443, source 0.0.0.0/0
        - (Optional) SSH: Protocol TCP, port 22, source 0.0.0.0/0

        These rules should have been added during the previous step if you selected to allow HTTP/HTTPS traffic from the internet.

    - Check that the OS firewall (e.g. `ufw` for Ubuntu) is also allowing this traffic.

    - Assign an [Elastic (static) IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html), as by default [AWS assigns a dynamic public IP that changes upon instance restart](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses).

    - To enable secure communication with the server, read the guide on [setting up secured connection using HTTPS](#secured-connections-using-https). For testing you can skip this step, but HTTPS communication must be enforced in the final production setup.

4. Deploy NOMAD
    - Connect to the EC2 instance. The easiest way is to use the browser based connection directly from the AWS console. You can alternatively also connect through SSH if you have generated a key pair and have SSH access enabled in the instance settings.

    - Install docker and docker compose on the virtual machine: you can [read more about the installation here](#installing-docker).

    - Ensure that Git is installed to be able to easily sync the distribution configuration. You can check this by running `git --version`. Generic installations instructions are found [here](https://git-scm.com/downloads/linux).

    - Create a NOMAD Oasis distribution using our template [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template). We recommend creating a new repository by presssing the "Use this template button", but for testing it is also possible to use the existing template repository directly.

    - Follow the deployment instructions in the `README.md` file under *Deploying the distribution/For a new Oasis*. This typically consists of cloning the repository, setting up file priviledges and then running `docker compose pull` + `docker compose up -d`.

5. Access and test deployment

    You should now be able to access the Oasis installation from anywhere using the static IP address or domain name you have configured: `http://<IP-or-domain>/nomad-oasis`. If you have not yet set up secure connections with HTTPS, [read about it here](#secured-connections-using-https).

## Installing Docker

You can find generic [installation instructions here](https://docs.docker.com/engine/install/). On Ubuntu, you can install docker and docker compose with:

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

You will also want to configure docker to be run as a non-root user using [these steps](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user). On Ubuntu, this can be done with:

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

        For testing, you can create a [self-signed certificate](https://en.wikipedia.org/wiki/Self-signed_certificate). These are not viable for a production setup, as they are not trusted e.g. by browsers.

        For detailed instructions, see the "Deploy Oasis with HTTPS" section in the [`nomad-distro-template` documentation](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#for-a-new-oasis)

    3. Free certificate from Let's Encrypt

        [Let's Encrypt](https://letsencrypt.org/) is a non-profit organization that provides free TLS certificats. To create a free certificate you must have a domain name. You can follow their tutorials on creating free certificates.

3. Setup your server to accept HTTPS traffic.
    To enable HTTPS, you need to mount your TLS certificate and ensure that port 443 is open. A template nginx configuration file is available, see the "Deploy Oasis with HTTPS" section of [`nomad-distro-template` documentation](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#for-a-new-oasis).
