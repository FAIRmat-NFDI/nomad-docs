# How to write an API

APIs allow you to add more APIs to the NOMAD app. More specifically you can create
a [FastAPI](https://fastapi.tiangolo.com) apps that can be mounted into the main NOMAD app alongside other apis
such as `/api/v1`, `/optimade`, etc.

This documentation shows you how to write a plugin entry point for an API.
You should read the [introduction to plugins](./plugins.md)
to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template) to
create an initial structure for a plugin containing an API.
The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── apis
   │   │   │   ├── __init__.py
   │   │   │   ├── myapi.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](./plugins.md#plugin-development-guidelines)
for more details on the best development practices for plugins, including linting, testing and documenting.

## API entry point

The entry point defines basic information about your API and is used to automatically
load it into a NOMAD distribution. It is an instance of a `APIEntryPoint` or its subclass and it contains a `load` method which returns a `fastapi.FastAPI` app instance.
Furthermore, it allows you to define a path prefix for your API.
The entry point should be defined in `*/apis/__init__.py` like this:

```python
from nomad.config.models.plugins import APIEntryPoint


class MyAPIEntryPoint(APIEntryPoint):

    def load(self):
        from nomad_example.apis.myapi import app

        return app


myapi = MyAPIEntryPoint(
    prefix = 'myapi',
    name = 'MyAPI',
    description = 'My custom API.',
)
```

Here you can see that a new subclass of `APIEntryPoint` was defined. In this new class you have to override the `load` method to determine the FastAPI app that makes your API.
In the reference you can see all of the available [configuration options for a `APIEntryPoint`](../../reference/plugins.md#apientrypoint).

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']` table in `pyproject.toml` in order for it to be automatically detected:

```toml
[project.entry-points.'nomad.plugin']
myapi = "nomad_example.apis:myapi"
```

## The FastAPI app

The `load`-method of an API entry point has to return an instance of a `fastapi.FastAPI`.
This app should be implemented in a separate file (e.g. `*/apis/myapi.py`) and could look like this:

```python
from fastapi import FastAPI
from nomad.config import config

myapi_entry_point = config.get_plugin_entry_point('nomad_example.apis:myapi')

app = FastAPI(
    root_path=f'{config.services.api_base_path}/{myapi_entry_point.prefix}'
)

@app.get('/')
async def root():
    return {"message": "Hello World"}
```

Read the official [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/) to learn how to build apps and APIs with
FastAPI.

If you run NOMAD with this plugin following our [Oasis configuration documentation](../oasis/configure.md)
you can curl this API and should receive the message:

```sh
curl localhost:8000/nomad-oasis/myapi/
```

In a nomad-distro-dev environment, the API should be accessible at:

```sh
curl localhost:8000/fairdi/nomad/latest/myapi/
```

For serving static content, one can use the `mount` operation of FastAPI. An example could look like this:

```python
from fastapi import FastAPI
from nomad.config import config

myapi_entry_point = config.get_plugin_entry_point('nomad_example.apis:myapi')

app = FastAPI(
    root_path=f'{config.services.api_base_path}/{myapi_entry_point.prefix}'
)

static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
app.mount("/static", StaticFiles(directory=static_folder), name="static")
```

Then e.g. the page `static_page.html` will be available at:

```sh
curl localhost:8000/nomad-oasis/myapi/static/static_page.html
```

or 

```sh
curl localhost:8000/fairdi/nomad/latest/myapi/static_page.html
```
