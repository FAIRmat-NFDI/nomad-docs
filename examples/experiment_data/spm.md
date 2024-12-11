# Domain-specific examples for SPM (Scanning Tunneling Spectorscopy)


Build upon your understanding of NOMAD's features with domain-specific examples and explanations.

### Contextualization for the technique and the scientific domain
A variety of file formats (coming technology instrumens) are used in the research field of scanning tunneling microscopy (STM), scanning tunneling spectroscopy (STS) and atomic force microscopy (AFM) to investigate topological propertise of surface of subjected material. The [pynxtools-spm](https://github.com/FAIRmat-NFDI/pynxtools-spm) plugin (note: The single plugin handles AFM, STM as well STS techniques) of the [pynxtools](https://github.com/FAIRmat-NFDI/pynxtools) parsing library solves the challenges of how these formats can be parsed and normalized into a common representation that increases interoperability and adds semantic expressiveness.

The [pynxtools-spm](https://github.com/FAIRmat-NFDI/pynxtools-spm) provides a indispensable tool to transfor the AFM, STM as well as STS experimental data (sometime refered as raw data or machine data) to common standarized structure defined in [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html#nxafm), [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html#nxstm), [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html#nxsts) application definition build with the help of [NeXus ontology](https://www.nexusformat.org/) ([GitHub page](https://github.com/FAIRmat-NFDI/nexus_definitions/tree/fairmat)). One of the main goals of such effort is to make the data comming from diverse sources comparable, searchable and shearable under the hood of NONAD research data management platform.

**NOTE**: Reader docs is still under development
<!-- For full benefits and usages of the reader please following links:

- [Full Reader Documentation](https://fairmat-nfdi.github.io/pynxtools-stm/)
- [GitHub Repository](https://github.com/FAIRmat-NFDI/pynxtools-stm)
- [Issue Tracker](https://github.com/FAIRmat-NFDI/pynxtools-stm/issues)


## How to upload XPS data to NOMAD
Documentation on how to upload STM / STS data sets from different sources can be found [here](https://fairmat-nfdi.github.io/pynxtools-sts/tutorials/nomad-tutorial.html)

## Supported file formats
A list of the supported file formats can be found in the `pynxtools-stm` [documentation](https://fairmat-nfdi.github.io/pynxtools-stm/). -->
