# How to install a NOMAD Oasis

NOMAD software is Open-Source, and everybody can run it. A self-hosted instance is called a [*NOMAD Oasis*](../../reference/glossary.md#deployment-nomad-oasis). A *NOMAD Oasis* does not need to be fully isolated. For example, you can publish uploads from your NOMAD Oasis to the central NOMAD installation. A NOMAD Oasis can be installed on a wide variety of different platforms: from your local laptop to a kubernetes cluster running in the cloud. We also support the three major operating systems: Linux, Windows and macOS.

The entire setup for a running a NOMAD Oasis is contained in a Git repository, and is called a [*NOMAD distribution*](../../reference/glossary.md#distribution-distro). We provide different distribution templates to help you get started:

1. **<a href="https://github.com/FAIRmat-NFDI/nomad-distro-template/" target="_blank" rel="noopener">NOMAD distribution for production</a>**

    For installing a production-ready, self-hosted NOMAD Oasis for research groups or institutions.

2. **<a href="https://github.com/FAIRmat-NFDI/nomad-distro-dev/" target="_blank" rel="noopener">NOMAD distribution for development</a>**

    Specialized template that allows for a much faster development cycle. This is targeted for plugin developers, Oasis administrators and for developing the `nomad-lab` package. Should not be used in production.

Once you have created a distribution, you can proceed to learning more about the different [configuration options](./configure.md), different ways to [deploy your distribution](./deploy.md), and also about how to [update](./update.md), [administer](./administer.md) or [troubleshoot](./troubleshoot.md) your Oasis.

!!! note

    If you are installing a NOMAD Oasis, please <a href="https://nomad-lab.eu/fairdi/keycloak/auth/realms/nomad-oasis/protocol/openid-connect/registrations?client_id=account&scope=openid%20profile&redirect_uri=https%3A%2F%2Fnomad-lab.eu%2Fnomad-lab%2Fnomad-oasis-registration.html&response_type=code" target="_blank" rel="noopener">register your Oasis with FAIRmat</a>. This allows us to contact you for important updates and helps us keep track of the number and location of installations.

## How to install the NOMAD Python Library

The `nomad-lab` Python package contains the core software features of the NOMAD software,
including the API, CLI, upload processing routines etc. This Python package is installed
automatically as part of a NOMAD Oasis, but you can optionally install and use it as a
stand-alone library for tasks like parsing or programmatic data querying.

You can install the latest stable version from <a href="https://pypi.org/project/nomad-lab/" target="_blank" rel="noopener">PyPI</a>:

```bash
pip install nomad-lab
```

or alternatively use our own GitLab package registry to download a more recent development version:

```bash
pip install nomad-lab --extra-index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
```

The Python package offers different feature sets through optional dependencies:

```bash
pip install nomad-lab[infrastructure] # For running the NOMAD infrastructure
pip install nomad-lab[dev]            # Contains development tools (pytest, pylint, mypy)
```

The `nomad-lab` package and it's dependencies can run natively on Linux, Windows and macOS.
