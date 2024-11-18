# How to write an example upload

Example uploads can be used to add representative collections of data for your plugin. Example uploads are available for end-users in the *Uploads*-page under the *Add example uploads*-button. There, users can instantiate an example upload with a click. This can be very useful for educational or demonstration purposes but also for testing.

This documentation shows you how to write a plugin entry point for an example upload. You should read the [documentation on getting started with plugins](./plugins.md) to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template) to create an initial structure for a plugin containing an example upload. The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── example_uploads
   │   │   │   ├── getting_started
   │   │   │   ├── __init__.py
   ├── LICENSE.txt
   ├── README.md
   ├── MANIFEST.in
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](./plugins.md#plugin-development-guidelines) for more details on the best development practices for plugins, including linting, testing and documenting.

## Example upload entry point

The entry point is an instance of a `ExampleUploadEntryPoint` or its subclass. It defines basic information about your example upload and is used to automatically load the associated data into a NOMAD distribution. The entry point should be defined in `*/example_uploads/__init__.py` like this:

```python
from nomad.config.models.plugins import ExampleUploadEntryPoint

myexampleupload = ExampleUploadEntryPoint(
    title = 'My Example Upload',
    category = 'Examples',
    description = 'Description of this example upload.',
    resources=['example_uploads/getting_started/*']
)
```

The `resources` field can contain one or several data resources that can be provided directly in the Python package or stored online. You can learn more about different data loading options in the next section. In the reference you can also see all of the available [configuration options for a `ExampleUploadEntryPoint`](../../reference/plugins.md#exampleuploadentrypoint).

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']` table in `pyproject.toml` in order for the example upload to be automatically detected:

```toml
[project.entry-points.'nomad.plugin']
myexampleupload = "nomad_example.example_uploads:myexampleupload"
```

## Including data in an example upload

There are three main ways to include data in an example upload, and you can also combine these different methods:

1. Data stored directly in the plugin package:

    You can include data from the Python package by specifying file or folder names. Here are some examples:

    ```python
    # Include a file into the upload
    resources = 'example_uploads/getting_started/README.md'

    # Include the entire folder recursively
    resources = 'example_uploads/getting_started'

    # Include contents of a folder recursively
    resources = 'example_uploads/getting_started/*'

    # Include a file/folder into a specific location within the upload
    resources = UploadResource(
        path='example_uploads/getting_started',
        target='upload_subfolder'
    )

    # Include multiple files/folders. The resources will be added in the given order.
    resources = [
        'example_uploads/getting_started/README.md',
        'example_uploads/getting_started/data.txt'
    ]
    ```

    This is convenient if you have relative small example data that can be tracked in version control. The path should be given relative to the package installation location (`src/<package-name>`), and you should ensure that the data is distributed with your Python package. Distribution of additional data files in Python packages is controlled with the `MANIFEST.in` file. If you create a plugin with our [template](https://github.com/FAIRmat-NFDI/nomad-plugin-template), the `src/<package-name>/example_uploads` folder is included automatically in `MANIFEST.in`. If you later add an example upload entry point to your plugin, remember to include the folder by adding the following line to `MANIFEST.in`:

    ```sh
    graft src/<package-name>/<path>
    ```

2. Data retrieved online:

    If your example uploads are very large (>100MB), storing them in Git may become unpractical. In order to deal with larger uploads, they can be stored in a separate online service. For example, [Zenodo](https://zenodo.org/) is an open and free platform for hosting scientific data. To load such external resources, you can specify one or multiple URLs as resources:

    ```python
    # Include single ZIP file (note that ZIP contents are not automatically extracted)
    resources = 'http://my_large_file_address.zip'

    # Include a file into a specific location within the upload
    resources = UploadResource(
        path='http://my_large_file_address.zip',
        target='upload_subfolder'
    )

    # Include multiple online files
    resources = ['http://my_large_file_address.zip', 'http://data.txt']
    ```

    Note that by default online files are downloaded only when the user requests the creation of an example upload, and that the downloaded files are not cached.

3. Data retrieved with a custom method:

    If the above options do not suite your use case, you can also override the `load`-method of `ExampleUploadEntryPoint` to perform completely custom data loading logic. Note that the `load` function receives the root upload folder as an argument, and you should store all files in this location. Below is an example of a custom `load` function that generates a data file on the fly:

    ```python
    import numpy as np
    from nomad.config.models.plugins import ExampleUploadEntryPoint, UploadPath


    class MyExampleUploadEntryPoint(ExampleUploadEntryPoint):

        def load(self, upload_path: str):
            """Custom load function that generates a data file on the fly."""
            filepath = os.path.join(upload_path, 'my_large_data.npy')
            np.save(filepath, np.ones((1000, 1000)))
    ```

    The utility function `ExampleUploadEntryPoint.resolve_resource` can be used for downloading files into the correct location, see the default `load` function for reference.