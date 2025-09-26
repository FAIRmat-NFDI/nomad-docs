# Domain-specific examples for SPM (scanning probe microscopy)

Scanning probe microscopy (SPM) is an umbrella term for a family of microscopy techniques that use a physical probe to scan a sample's surface at the nanoscale or atomic scale. These techniques include Atomic Force Microscopy (AFM), Scanning Tunneling Microscopy (STM) and Scanning Tunneling Spectroscopy (STS).

The NOMAD plugin [pynxtools-spm](https://github.com/FAIRmat-NFDI/pynxtools-spm){:target="_blank" rel="noopener"}, which is a reader plugin for the [pynxtools](./pynxtools.md) parsing library, allows parsing of data from a variety of file formats (coming from different technology instrumens). The plugin normalizes these data into a common representation (using the NeXus application definition [`NXspm`](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html#nxpsm){:target="_blank" rel="noopener"} and its specializations [`NXafm`](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html#nxafm){:target="_blank" rel="noopener"}, [`NXstm`](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html#nxstm){:target="_blank" rel="noopener"}, and [`NXsts`](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html#nxsts){:target="_blank" rel="noopener"}, which increases interoperability and adds semantic expressiveness.

One of the main goals of such effort is to make the data comming from diverse sources comparable, searchable, and shareable using NOMAD.

More information about the plugin can be found here:

<!-- TODO: reactivate when the docs are working again -->
<!-- - [Documentation](https://fairmat-nfdi.github.io/pynxtools-spm/){:target="_blank" rel="noopener"} -->
- [GitHub Repository](https://github.com/FAIRmat-NFDI/pynxtools-spm){:target="_blank" rel="noopener"}

<!-- TODO: reactivate when the docs are working again -->
<!-- ## Supported file formats

A list of the supported file formats can be found in the `pynxtools-spm` [documentation](https://fairmat-nfdi.github.io/pynxtools-spm/){:target="_blank" rel="noopener"}. -->
