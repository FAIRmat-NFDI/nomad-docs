


## Guidelines for building a custom schema

NOMAD YAML schema files must have the `.archive.yaml` extension for NOMAD to recognize them as schema files. Below are six main guidelines for creating a custom YAML schema file.

??? info "1. NOMAD's `archive.yaml` files start with the `definitions:` keyword, and must have a `name:`, and can have a `description:`."
    
    NOMAD syntax:
    ```yaml
    definitions:
      name:
      description:
    ```

    Example:
    ```yaml
    definitions:
      name: My NOMAD Custom Schema
      description: This is a custom schema that includes several sections.
    ```
??? info "2. A schema can have several sections."

    The keyword to introduce different sections of a schema is `sections:`.

    NOMAD syntax:

    ```yaml
    definitions:
      name:
      description: 

      sections:
        My_first_section:
        My_second_section:
        My_third_section:
    ```


??? info "3. Sections can inherit from NOMAD's `base_sections` or other sections."
    When inheriting structure and definition from an existing section, use the `base_sections:` keyword and list the desired base sections you would like to inherit from. The keyword `base_sections:` additionally allows you to also inherit from other sections (e.g., within the same schema or even a section that have been published in NOMAD, see [schema package references in NOMAD Documentation](https://nomad-lab.eu/prod/v1/docs/howto/customization/basics.html#schema-package-references){:target="_blank"}). Inherited sections can be given in a python list, or subsequent indented lines starting with a dash, `-`.

    Example:

    ```yaml
    definitions:
      name: My NOMAD Custom Schema
      description: This is a custom schema that includes several sections.

      sections:
        My_first_section:
          base_sections:
            - nomad.datamodel.data.EntryData
            - nomad.datamodel.metainfo.eln.Sample
  
        My_second_section:
        My_third_section:
    ```

    or alternatively in the form of a Python list:

    ```yaml
    definitions:
      name: My NOMAD ELN
      description: This is a custom schema that includes several sections.

      sections:
        My_first_section:
          base_sections: ['nomad.datamodel.data.EntryData', 'nomad.datamodel.metainfo.eln.Sample']
  
        My_second_section:
        My_third_section:          
    ``` 

??? info "4. Each section can contain quantities, other sections, and subsections."
    Each section can define quantities, representing parameters such as measurement conditions or sample properties. In addition, sections **can also contain** subsections. When including subsections, you need to tell NOMAD the subsections you included are themselves a section. How? By including the keyword `section:` in the next indented line (see bottom example). A list of editable quantities can be found [here](https://nomad-lab.eu/prod/v1/gui/dev/editquantity){:target="_blank"}.

    NOMAD syntax is:

    ```yaml
    definitions:
      name: My NOMAD ELN
      description: This is a custom schema that includes several sections.

      sections:
        My_first_section:
          base_sections:
            - nomad.datamodel.data.EntryData
            - nomad.datamodel.metainfo.eln.Sample
          quantities:

          sub_sections:
            My_first_subsection:
              section:
            My_second_subsection:
              section:      
        My_second_section:
        My_third_section:        
    ```


??? info "5. Quantities can be defined with type, shape, unit and other properties"
    Quantities define possible primitive values. The basic properties that can go into a quantity definition are `type`, `shape`, and `unit`.

    ```yaml
    definitions:
      name: My NOMAD ELN
      description: This is a custom schema that includes several sections.

      sections:
        My_first_section:
          base_sections:
            - nomad.datamodel.data.EntryData
            - nomad.datamodel.metainfo.eln.Sample
          quantities:
            first_quantity:
              - type: #For example, str or np.float64
              - shape: #For example scalar or list (['*'])
              - unit: #For example, meters, amperes, or seconds
          sub_sections:
            My_first_subsection:
              section:
            My_second_subsection:
              section:
            My_third_subsection:
              section:

        My_second_section:
        My_third_section:          
    ```

??? info "6. Sections and quantities can have annotations"
    Annotations provide additional information that NOMAD can use to alter its behavior around these definitions and how users can interact with them. The keyword for annotations is `m_annotations:`.
    Among the various functionalities that annotations provide, they enable the transformation of schema sections, subsections, and quantities into ELN components that users can edit directly within the GUI.
    ```yaml
    definitions:
      name: My NOMAD ELN
      description: This is an electronic lab notebook schema that includes several sections.
      
      sections:
        My_first_section:
          base_sections:
            - nomad.datamodel.data.EntryData
            - nomad.datamodel.metainfo.eln.Sample
          quantities:
            first_quantity:
              - type: #For example, str or np.float64
              - shape: #For example scalar or list (['*'])
              - unit: #For example, meters, amperes, or seconds
              m_annotations:
                annotation_name:
                  key1: value1  
              sub_section:
                My_first_subsection:
                  section:
                My_second_subsection:
                  section:
                My_third_subsection:
                  section:

        My_second_section:
        My_third_section:    
    ```