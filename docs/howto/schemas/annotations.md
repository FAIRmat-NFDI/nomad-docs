# How to annotate schemas for the GUI

A schema defines what data can exist. *Annotations* tell NOMAD what to do with that data — how to
display it, plot it, and let users edit it. Adding ELN annotations to a schema turns it into an
Electronic Lab Notebook: users can create entries from it and edit the structured data directly in
the GUI.

Annotations are named blocks of key-value pairs attached to a definition under `m_annotations`:

```yaml
definitions:
  sections:
    MyAnnotatedSection:
      m_annotations:
        annotation_name:
          key1: value
          key2: value
```

For the complete list of annotations and their arguments, see
{{ nav_link("reference/annotations.md", breadcrumb=True) }}.

## Make quantities editable

The `eln` annotation gives a quantity an editor component in the GUI. The component you choose has to
suit the quantity's type — a string quantity can use a text field, a datetime quantity a date picker,
an enum a dropdown:

```yaml
definitions:
  sections:
    Sample:
      base_sections:
        - nomad.datamodel.data.EntryData
      quantities:
        name:
          type: str
          m_annotations:
            eln:
              component: StringEditQuantity
        preparation_date:
          type: Datetime
          m_annotations:
            eln:
              component: DateTimeEditQuantity
        data_file:
          type: str
          m_annotations:
            eln:
              component: FileEditQuantity
```

Adding the `eln` annotation to the *section* makes it selectable when creating a new entry from the
GUI. See {{ nav_link("reference/annotations.md", breadcrumb=True) }} for every available component
and the types each one accepts.

## Control how values are displayed

Use the `display` annotations to set the unit a quantity is shown in, and to give sections a label
derived from one of their quantities. When labelling quantities, follow the naming conventions in
[Reference > Schema language > Naming conventions](../../reference/metainfo.md#naming-conventions).

## Plot data

The `plot` annotation renders quantities as interactive charts on the entry page, and
`H5WebAnnotation` does the same for HDF5-backed quantities. See
{{ nav_link("howto/plugins/tools/hdf5.md", breadcrumb=True) }} for the HDF5 case.

## Example ELN schema

This is the commented ELN schema from the ELN example upload, which you can create from NOMAD's
upload page:

```yaml
--8<-- "examples/data/eln/schema.archive.yaml"
```

## Related materials

- {{ nav_link("reference/annotations.md", breadcrumb=True) }} — every annotation and its arguments.
- {{ nav_link("howto/schemas/tabular.md", breadcrumb=True) }} — annotations that drive the tabular parser.
- {{ nav_link("howto/manage/gui/eln.md", breadcrumb=True) }} — using ELNs in the GUI.
- {{ nav_link("tutorial/eln/custom_eln_yaml.md", breadcrumb=True) }} — a guided walkthrough.
