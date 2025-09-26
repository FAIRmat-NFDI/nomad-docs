# Domain-specific examples for X-ray photoelectron spectroscopy

!!! warning "Attention"
    We are currently working to update this content.

## Contextualization for the technique and the scientific domain

A variety of file formats are used in the research field of X-ray photoelectron spectroscopy and related techniques. The `pynxtools-xps` plugin of the `pynxtools` parsing library solves the challenge of how these formats can be parsed and normalized into a common representation that increases interoperability and adds semantic expressiveness.

`pynxtools-xps`, which is a plugin for [pynxtools](https://github.com/FAIRmat-NFDI/pynxtools){:target="_blank" rel="noopener"}, provides a tool for reading data from various propietary and open data formats from technology partners and the wider XPS community and standardizing it such that it is compliant with the [NeXus](https://www.nexusformat.org/){:target="_blank" rel="noopener"} application definitions [`NXmpes`](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXmpes.html){:target="_blank" rel="noopener"} and [`NXxps`](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXxps.html){:target="_blank" rel="noopener"}, which is an extension of `NXmpes`.

- [Documentation](https://fairmat-nfdi.github.io/pynxtools-xps/){:target="_blank" rel="noopener"}
- [GitHub repository](https://github.com/FAIRmat-NFDI/pynxtools-xps/){:target="_blank" rel="noopener"}
- [Issue tracker](https://github.com/FAIRmat-NFDI/pynxtools-xps/issues/){:target="_blank" rel="noopener"}

## How to upload XPS data to NOMAD

Documentation on how to upload XPS data sets from different sources can be found [here](https://fairmat-nfdi.github.io/pynxtools-xps/tutorial/nomad.html){:target="_blank" rel="noopener"}

## Supported file formats

A list of the supported file formats can be found in the `pynxtools-xps` [documentation](https://fairmat-nfdi.github.io/pynxtools-xps/){:target="_blank" rel="noopener"}.
