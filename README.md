## `nomad-docs`

This repository contains the documentation for the NOMAD website.

### Contributing

To contribute, please open a pull request (PR) with your changes.

#### Running the Docs Server Locally

You have two options to run the documentation server:

1. Use the [nomad-dev-distro](https://github.com/FAIRmat-NFDI/nomad-distro-dev?tab=readme-ov-file#day-to-day-development) command.

2. Or manually install the required dependencies and run:

```bash
uv run --with 'nomad-lab[dev, infrastructure, parsing]' mkdocs serve
```

This will start a local server where you can preview your changes.
