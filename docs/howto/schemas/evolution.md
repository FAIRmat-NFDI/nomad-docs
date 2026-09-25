# How to deal with schema evolution

Eventually you will change a schema. It is tempting to think of the state before and after a change
as version 1 and version 2 of the same schema, but technically they are two different schemas: you
are replacing the schema that describes existing data with a new one, and hoping the new one still
describes that data.

Whether it does depends on the kind of change you made. Some changes *break* existing data.

## What it means to break an entry

Breaking an entry means either that its `*.archive.[json|yaml]` raw files can no longer be parsed, or
that its processed archive data can no longer be opened. In both cases NOMAD is trying to convert
JSON-style data into section definition instances and validate it against the current schema; if
items in the data no longer match a definition, the process throws errors.

The rule is: if every section instance that *followed* a definition in the old schema still *follows
the same definition* in the new schema, you can safely replace the schema. If not, you must *migrate*
the data — or you break it.

## How NOMAD identifies a definition version

Every definition carries a `definition_id`, a hash-like identifier that uniquely identifies it. Any
change to a definition that affects the data it describes produces a new definition id. Some
applications use the definition id to distinguish between versions of the same schema package.

You can include definition ids when serializing with `m_to_dict(with_def_id=True)`.

## Safe and unsafe changes

*Adding* to a schema is generally safe — new section definitions, new quantities, new subsections.
All existing data still only uses definitions that continue to exist.

*Removing* is generally not safe. Removing a quantity makes NOMAD ignore values in existing entries;
removing a section definition breaks them outright.

*Changing* may or may not be safe. In many cases a change is really a removal plus an addition:

- **Names** determine the identity of a definition, so renaming is literally removing and adding one.
  Not safe, unless you add an `alias`.
- **Adding `base_sections`** is safe; removing them is not — it adds and removes properties respectively.
- **Hoisting a property** from a section into a base section is safe (you only add properties). The
  reverse is not (you remove properties from some definitions).
- **Making a subsection type more generic** is safe (you add properties to it); making it more
  specific is not.
- **Changing a quantity's `type` or `shape`, or a subsection's `repeats`**, is not safe.

Two kinds of change do not break entries but do change their meaning:

- Changing a `unit` leaves entries openable but silently reinterprets every stored value.
- Changing annotations leaves entries openable but changes how tools treat them. The GUI is the most
  important such tool — changing ELN annotations can stop users editing old data the way they used to.

## Keep versions side by side

Once a breaking change is unavoidable, you need a new major version of the schema — and you must keep
the old version as long as data still follows it. Two versions therefore have to exist at the same
time.

Each section instance refers to its schema by qualified Python name, including the module holding the
schema package. Breaking changes therefore belong in a *new schema package*. By convention:

- carry the major version in the package name, e.g. `nomad_example.schema_packages.my_package_v2`; or
- maintain schema packages in version submodules, e.g. `nomad_example.schema_packages.my_package.v2`.

!!! note
    Because breaking changes are effectively inevitable, start a new schema package at `v1` rather
    than adding the version later.

Only the *major* version warrants a separate module. Minor and patch versions do not introduce
breaking changes by definition, so the module for a given major version can be changed safely.

## Migration strategies

!!! warning
    This is preliminary information.

### Use schema package aliases

If you have moved a definition to a new module without making other breaking changes, use a schema
package alias.

By default a schema package is identified by the fully qualified path of the Python module containing
its definitions, for example `nomad_example.schema_packages.mypackage` — package name, subpackage,
then the module. This keeps packages from clashing: Python package names are unique, and a path
within a package points at exactly one module. The consequence is that **moving a schema definition
to a new module breaks every reference to the old one**.

To move a schema to a new module, e.g. `nomad_example.schema_packages.mypackage.v2`, while letting
existing entries keep resolving it under the old name, declare the old path as an alias on the schema
package definition:

```python
m_package = SchemaPackage(aliases=['nomad_example.schema_packages.mypackage'])
```

!!! note
    Aliases also work when you need to move a schema package for other reasons, such as moving
    schemas from one plugin to another.

### Offer migration functionality

!!! warning
    This approach is still being tested and more dedicated functionality may be provided in future.

You will not want to maintain an old version indefinitely. Eventually you deprecate and remove schema
package versions from new plugin releases, so you should offer users a way to migrate data that
follows the old version.

#### Migrate processed data

Where your schema is instantiated by a parser, processed data — entry archives — can be migrated by
reprocessing the affected uploads with a new version of the parser that follows the new schema. Users
need to be told to reprocess.

#### Migrate raw files

Where the data lives in `*.archive.json` raw files, as with NOMAD ELNs, the raw files themselves have
to change. This is harder, because mainfile immutability is built into NOMAD. To reuse the
parser-based strategy above, add a `normalize` function to the `EntryData` section definitions of the
*old* schema version. That function:

- transforms the old instance into an instance of the new version;
- writes the new version's `m_to_dict` back into the mainfile;
- replaces the `data` section with the transformed instance.

In pseudo code:

```py
from ..v2 import MyData as MyDataV2


def normalize(self, archive, logger):
    transformed = MyDataV2()

    # code that fills transformed from self

    with archive.context.raw_file(archive.metadata.mainfile, 'wt') as f:
        f.write(json.dumps(dict(data=transformed.m_to_dict())))

    archive.data = transformed
```

With such a `normalize` function in place, you can apply the reprocessing strategy to migrate.

!!! warning
    There may be issues with this approach depending on how the `normalize` functions are executed.
    It only works well if, after `data` is replaced, the `normalize` functions of the transformed
    instance are called and none of the original instance's `normalize` functions have run yet.

    This approach also carries risk: if the process fails in an unexpected way, raw file data may be
    lost.

## Related materials

- {{ nav_link("reference/code_guidelines.md", breadcrumb=True) }} — backwards compatibility rules for schema base classes.
- {{ nav_link("explanation/north.md", breadcrumb=True) }} — schema version mismatches between NORTH tools.
- {{ nav_link("howto/plugins/types/schema_packages.md", breadcrumb=True) }} — packaging and releasing a schema package.
