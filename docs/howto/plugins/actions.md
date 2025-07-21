# How to define actions

Actions allow to define executable workflows in NOMAD. They provide an
alternative to entry normalize methods and are well-suited for setting up
long-running workflows, like running training and inferring ML models, or
workflows that need to be triggered at regular time intervals. Dedicated
workers can be configured to manage workflows, allowing targeted allocation of
resources like GPUs for specific tasks.

This documentation shows you how to write a plugin entry point for an action.
You should read the [introduction to plugins](./plugins.md)
to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template) to
create an initial structure for a plugin containing an action.
The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── actions
   │   │   │   ├── __init__.py
   │   │   │   ├── activities.py
   │   │   │   ├── workflow.py
   │   │   │   ├── models.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](./plugins.md#plugin-development-guidelines)
for more details on the best development practices for plugins, including linting, testing and documenting.

