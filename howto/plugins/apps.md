# How to write an app

Apps provide customized views of data in the GUI, making it easier for the users to navigate and understand the data related to a specific domain. This typically means that certain domain-specific properties are highlighted, different units may be used for physical properties, and specialized dashboards may be presented. This becomes crucial for NOMAD installations to be able to scale with data that contains a mixture of experiments and simulations, different techniques, and physical properties spanning different time and length scales.

Apps only affect the way data is *displayed* for the user: if you wish to affect the underlying data structure, you will need to write a [Python schema package](./schema_packages.md) or a [YAML schema package](../customization/basics.md).

This documentation shows you how to write an plugin entry point for an app. You should read the [introduction to plugins](./plugins.md) to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template) to create an initial structure for a plugin containing an app. The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── apps
   │   │   │   ├── __init__.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](./plugins.md#plugin-development-guidelines) for more details on the best development practices for plugins, including linting, testing and documenting.

## App entry point

The entry point defines basic information about your app and is used to automatically load the app into a NOMAD distribution. It is an instance of an `AppEntryPoint` and unlike many other plugin entry points, it does not have a separate resource that needs to be lazy-loaded as the entire app is defined in the configuration as an instance of `nomad.config.models.ui.App`. You will learn more about the `App` class in the next sections. The entry point should be defined in `*/apps/__init__.py` like this:

```python
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App

myapp = AppEntryPoint(
    name = 'MyApp',
    description = 'My custom app.',
    app = App(...)
)
```

Here we have instantiated an object `myapp` in which you specify the default parameterization and other details about the app. In the reference you can see all of the available [configuration options for an `AppEntryPoint`](../../reference/plugins.md#appentrypoint).

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']` table in `pyproject.toml` in order for the app to be automatically detected:

```toml
[project.entry-points.'nomad.plugin']
myapp = "nomad_example.apps:myapp"
```

## Creating an `App`

The definition fo the actual app is given as an instance of the `App` class specified as part of the entry point. A full breakdown of the model is given below in the [app reference](#app-reference), but here is a small example:

```python
--8<-- "examples/plugins/app.py"
```

!!! tip
    If you want to load an app definition from a YAML file, this can be easily done with the pydantic `parse_obj` function:

    ```python
        import yaml
        from nomad.config.models.plugins import AppEntryPoint
        from nomad.config.models.ui import App

        yaml_data = """
            label: My App
            path: myapp
            category: Theory
        """
        myapp = AppEntryPoint(
            name='MyApp',
            description='App defined using the new plugin mechanism.',
            app=App.parse_obj(
                yaml.safe_load(yaml_data)
            ),
        )
    ```

### Loading quantity definitions into an app

By default, quantities from custom schemas are not available in an app, and they need to be explicitly added. Each app may define the quantities to load by using the **search_quantities** field in the app config. Once loaded, these search quantities can be queried in the search interface, but also targeted in the rest of the app configuration as explained below.

!!! important

    Note that not all of the quantities from a custom schema can be loaded into the search. At the moment, we only support loading **scalar** quantities from custom schemas.

Each schema has a unique name within the NOMAD ecosystem, which is needed to target them in the configuration. The name depends on the resource in which the schema is defined in:

- Python schemas are identified by the python path for the class that inherits
from `Schema`. For example, if you have a python package called `nomad_example`,
which has a subpackage called `schema_packages`, containing a module called `mypackage.py`, which contains the class `MySchema`, then
the schema name will be `nomad_example.schema_packages.mypackage.MySchema`.
- YAML schemas are identified by the entry id of the schema file together with
the name of the section defined in the YAML schema. For example
if you have uploaded a schema YAML file containing a section definition called
`MySchema`, and it has been assigned an `entry_id`, the schema name will be
`entry_id:<entry_id>.MySchema`.

The quantities from schemas may be included or excluded by using the [`SearchQuantities`](#app-reference)
field in the app config. This option supports a wildcard/glob syntax for including/excluding certain
search quantities. For example, to include all search quantities from the Python schema defined in the class
`nomad_example.schema_packages.mypackage.MySchema`, you could use:

```python
search_quantities=SearchQuantities(
    include=['*#nomad_example.schema_packages.mypackage.MySchema']
)
```

The same thing for a YAML schema could be achieved with:

```python
search_quantities=SearchQuantities(
    include=['*#entry_id:<entry_id>.MySchema']
)
```

### Using loaded search quantity definitions

Once search quantities are loaded, they can be targeted in the rest of the app. The app configuration often refers to specific search quantities to configure parts of the user interface.

The syntax for targeting quantities depends on the resource:

- For python schemas, you need to provide the path and the python schema name separated
by a hashtag (#), for example `data.mysection.myquantity#nomad_example.schema_packages.mypackage.MySchema`.
- For YAML schemas, you need to provide the path and the YAML schema name separated
by a hashtag (#), for example `data.mysection.myquantity#entry_id:<entry_id>.MySchema`.
- Quantities that are common for all NOMAD entries can be targeted by using only
the path without the need for specifying a schema, e.g. `results.material.symmetry.space_group`.

For example, one could configure the results table to show a new column using one of the search quantities with:

```python
--8<-- "examples/plugins/columns.py"
```

### Narrowing down search results in the app

The search results that will show up in the app can be narrowed down by passing
a dictionary to the `filters_locked` option. In the example app, only
entries that use `MySchema` are included.

```python
filters_locked={
    "section_defs.definition_qualified_name": [schema]
}
```

It is also possible to filter by quantities defined in the [`results`](../../reference/glossary.md#results-section-results) section. For example, if you want to limit your app to entries that have the property `catalytic` filled in the `results` section:

```python
filters_locked={
    "quantities": ["results.properties.catalytic"]
}
```

### Menu

The `menu` field controls the structure of the menu shown on the left side of the search interface. Menus have a controllable width, and they contain items that are displayed on a 12-based grid. You can also nest menus within each other. For example, this defines a menu with two levels:

```python
--8<-- "examples/plugins/menu.py"
```

The following items are supported in menus, and you can read more about them in the App reference:

 - [`Menu`](#app-reference): Defines a nested submenu.
 - `MenuItemTerms`: Used to display a set of possible text options.
 - `MenuItemHistogram`: Histogram of numerical values.
 - `MenuItemPeriodictable`: Displays a periodic table.
 - `MenuItemOptimade`: Field for entering OPTIMADE queries.
 - `MenuItemVisibility`: Controls for the query visibility.
 - `MenuItemDefinitions`: Shows a tree of available definitions from which items can be selected for the query.
 - `MenuItemCustomQuantities`: Form for querying custom quantities coming from any schema.
 - `MenuItemNestedObject`: Used to group together menu items so that their query is performed using an Elasticsearch nested query. Note that you cannot yet use nested queries for search quantities originating from custom schemas.

### Dashboard
 The Dashboard field controls the content of the main search interface window. Different widgets can be added which contain terms or numerical information and can be controlled in size and position. There are 4 different types of Widgets:
 `WidgetTerms`,
 `WidgetHistogram`,
 `WidgetScatterplot` and
 `WidgetPeriodicTable`

```python
--8<-- "examples/plugins/dashboard.py:13:"
```

## App reference

{{ pydantic_model('nomad.config.models.ui.App')}}
