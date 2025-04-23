It is very common to export measurement data into a tabular format such as `.csv` or `.xlsx`. Following, we'll explore how to utilize NOMAD's **tabular parser** effectively to enhance our data documentation and visualization.

Our objectives are:

1. To upload our `.csv` or `.xlsx` data files, so that we can visualize and publish them as **entries** in NOMAD.
2. Enhance our custom schema for polymer processing by making NOMAD parse the data within these files, and then visualize the data in plots that can be viewed in our customized ELN. 


NOMAD offers a versatile tabular parser that can be configured to process tabular data with different representations:

- **Column Mode:** each column contains an array of cells that we want to parse into one quantity. Example: current and voltage arrays to be plotted as x and y.
  
- **Row Mode**: each row contains a set of cells that we want to parse into a section, i.e., a set of quantities. Example: an inventory tabular data file (for substrates, precursors, or more) where each column represents a property and each row corresponds to one unit stored in the inventory.

More details on the different representations of tabular data can be found in [NOMAD documentation on how to parse tabular data](https://nomad-lab.eu/prod/v1/docs/howto/customization/tabular.html){:target="_blank"}.

## Steps to utilize NOMAD's tabular parser for `.csv` data

We use an example `.csv` file, which is the output of an optical absorption instrument (download the **P3HT_optical.csv** file  [here](https://github.com/FAIRmat-NFDI/FAIRmat-tutorial-16/blob/main/tutorial_16_materials/part_4_files/P3HT_optical.csv){:target="_blank"}). We open this file (e.g., using Notepad) and have a quick look:

<div style="text-align: center;">
    <img src="images/notpad_p3ht_optical.png" alt="csv file view" width="300">
</div>

In this `.csv` file:

- Headers are **Wavelength** and **Absorbance**.
- Line 2 gives the units, that we will not need, because we manually define them in the schema.
- Then we have the values for Wavelength and Absorbance, in column mode, as an array.
- The separator is: `,`.

Knowing this, we continue to utilize the NOMAD parser with following steps.


### **Step 1: Defining and saving the schema file**

Let's start by creating a new schema file with the `.archive.yaml` format, and create a section called Optical_absorption.

```yaml
definitions:
  name: This is a parser for optical absorption data in the .csv format.
  sections:
    Optical_absorption:
```

### **Step 2: Adding the needed base sections**

The next step is to inherit the base sections to meet our ELN needs.

- To create entries from this schema we will use `nomad.datamodel.data.EntryData`
- To use the tabular parser we will use `nomad.parsing.tabular.TableData`
- To enable the plot function we will use `nomad.datamodel.metainfo.plot.PlotSection`

remember, the NOMAD syntax to include sections to inherit from, was `base_sections:`, and also care for the indentation, `base_sections` should be indented one level (2 spaces) with respect to the `Optical_absorption:`.

```yaml
base_sections:
  - nomad.datamodel.data.EntryData
  - nomad.parsing.tabular.TableData
  - nomad.datamodel.metainfo.plot.PlotSection
```

### **Step 3: Defining the quantities of our schema**

We will define the quantities in our ELN schema. Three quantities are needed, let's call them:

- **`data_file`** to upload the data file and apply the tabular parser.
- **`wavelength`** to store x-axis values extracted by the parser.
- **`absorption`** to store y-axis values extracted by the parser.

and give them a proper type and shape attribute.

```yaml
quantities:
  data_file:
    type: str
  wavelength:
    type: np.float64
    unit: nm
    shape: ['*']
  absorbance:
    type: np.float64
    shape: ['*']
```

- `type: str` for `data_file` specifies that the value is a file path as a string (e.g., for uploaded `.csv` or `.xlsx` files).

- `shape: ['*']` defines a one-dimensional array with arbitrary length, suitable for storing array data like `wavelength` or `absorbance`.


### **Step 4: Instructing NOMAD on how to treat different quantities**

Remember, the syntax for this purpose was `m_annotations:`

* **The `data_file` quantity:**  

The first one is to instruct NOMAD to allow for dropping and selecting files in this quantity. Here we will use the following: 

```yaml
eln:
  component: FileEditQuantity
```
The second one is to instruct NOMAD to open the operating system's data browser to select files:

```yaml
browser:
  adaptor: RawFileAdaptor
```
The third one instructs NOMAD to apply the tabular parser to extract the data from the uploaded file:
```yaml
tabular_parser:
  parsing_options:
    comment: '#'
    skiprows: [1]
  mapping_options:
    - mapping_mode: column
      file_mode: current_entry
      sections:
        - '#root'
```
The value of `skiprows` can be an integer (e.g., n) or a list of integers. If this is an integer, the parser skips that number of rows and starts from the next one (n+1). If this is a list of integers (e.g., [m, n]), the parser skips the (m+1)th and (n+1)th rows (Python list). Here we have [1], meaning that the 2nd row (the units) will be skipped. We required that, because we needed capture the rest of the column as float numbers. The rest tells NOMAD, what parsing mode should be applied to the data file.

So we will annotate the `data_file` as following:

```yaml
m_annotations:
  eln:
    component: FileEditQuantity
  browser:
    adaptor: RawFileAdaptor
  tabular_parser:
    parsing_options:
      comment: '#'
      skiprows: [1]
    mapping_options:
      - mapping_mode: column
        file_mode: current_entry
        sections:
          - '#root'  
```


* **The `wavelength` quantity:**  
This quantity will accept values, that will be extracted by the tabular parser from the column with **Wavelength** as the header. Therefore the annotation will be:
```yaml
m_annotations:
  tabular:
    name: Wavelength
```
Note that the value for the `name` key **must** be exactly written as the **header of the column that we want to capture its values** (in this case **Wavelentgh**) and put in the `wavelength` quantity we defined in the schema.

* **The `absorbance` quantity:**  

```yaml
m_annotations:
  tabular:
    name: Absorbance
```
Again note that the value for the `name` key **must** be exactly written as the **header of the column that we want to capture its values** (in this case **Absorbance**) and put in the `absorbance` quantity we defined in the schema.

### **Step 5: Creating a plot for the data**

To visualize the data from the uploaded and parsed file within the ELN, we will use an annotation for the `Optical_absorption` section of our schema.
By using the `plotly_graph_object` annotation we instruct NOMAD which quanty should be used for the x-axis and which quanty for the y-axis (can also be several quantities, showing several curves in one plot), as well as provide the title of the plot. Within the `plotly_graph_object` annotation, the `data` key defines the quantities for each axis. Here, these variable names match those which are defined in the schema. Finally, plot's title is set using the `layout` key.

```yaml
m_annotations:
  plotly_graph_object:
    data:
      x: "#wavelength"
      y: "#absorbance"
    layout:
      title: Optical Spectrum
```
Note that here, the graph object belongs to the `Optical_absorption` section definition. Therefore, the `m_annotations:` **must be at the same hierarchy level as `quantities`, and `base_sections`** of the parent section, `Optical_absorption`.

### **Step 6 (optional): Adding a free text field**

If you only want to publish your data and graph, consider adding a short description.  
To do this, select a free text field from [editable quantities](https://nomad-lab.eu/prod/v1/gui/dev/editquantity){:target="_blank"} and add it as a **quantity** to your schema.  

For example:

```yaml
info_about_data:
  type: str
  m_annotations:
    eln:
      component: RichTextEditQuantity
```

Finally, our custom schema file should look like the following:

```yaml
definitions:
  name: This is a parser for optical absorption data in the .csv format.
  sections:
    Optical_absorption:
      base_sections:
        - nomad.datamodel.data.EntryData
        - nomad.parsing.tabular.TableData
        - nomad.datamodel.metainfo.plot.PlotSection
      quantities:
        info_about_data:
          type: str
          m_annotations:
            eln:
              component: RichTextEditQuantity          
        data_file:
          type: str
          m_annotations:
            eln:
              component: FileEditQuantity
            browser:
              adaptor: RawFileAdaptor
            tabular_parser:
              parsing_options:
                comment: '#'
                skiprows: [1]
              mapping_options:
                - mapping_mode: column
                  file_mode: current_entry
                  sections:
                    - '#root'
        wavelength:
          type: np.float64
          unit: nm
          shape: ['*']
          m_annotations:
            tabular:
              name: Wavelength
        absorbance:
          type: np.float64
          shape: ['*']
          m_annotations:
            tabular:
              name: Absorbance
      m_annotations:
        plotly_graph_object:
          data:
            x: "#wavelength"
            y: "#absorbance"
        layout:
          title: Optical Spectrum
```

### **Step 7: Uploading the Schema File to NOMAD and Creating an Entry**

Now that we have created the ELN schema file for parsing the optical absorption data file, let's put it to the test in the NOMAD GUI.


## Enhance the custom ELN schema with NOMAD's tabular parser.

In the current page of the tutorial, we have already explored how to use the tabular parser to visualize a `.csv` file of optical absorption data.We defined a main section that includes the tabular parser. A similar approach can be applied to other sections and subsections of a custom ELN template to allow file uploads and enable visualization. It is simply a matter of deciding where to include the section that holds the tabular parser.

Next, we will enhance the custom ELN template for polymer thin film preparation by adding a section for optical absorption data using the tabular parser.

??? example "Example: Enhancing the polymer processing custom ELN schema with tabular parser)"

    Let's now enhance our Polymer Processing schema by adding the tabular parser and a corresponding plot.

    We already created a custom schema named **polymer_processing_schema.archive.yaml**. You can copy the following snippet and paste it into a new `.archive.yaml` file:

    ```yaml
    definitions:
      name: Processing of polymers thin-films
      sections:
        Experiment_Information:
          base_sections: 
            - nomad.datamodel.data.EntryData
          quantities:
            Name:
              type: str  
              default: Experiment title
              m_annotations:
                eln:
                  component: StringEditQuantity
            Researcher:
              type: str
              default: Name of the researcher who performed the experiment
              m_annotations:
                eln:
                  component: StringEditQuantity
            Date:
              type: Datetime
              m_annotations:
                eln:
                  component: DateTimeEditQuantity
            Additional_Notes:
              type: str
              m_annotations:
                eln:
                  component: RichTextEditQuantity
          sub_sections:
            Sample:
              section:
                base_sections:
                  - nomad.datamodel.metainfo.eln.Sample
                m_annotations:
                  eln:
                    overview: true
                    hide: ['chemical_formula']
            Solution:
              section:
                base_sections:
                  - nomad.datamodel.metainfo.eln.Sample
                m_annotations:
                  eln:
                    overview: true
                    hide: ['chemical_formula', 'description']
                quantities:
                  Concentration:
                    type: np.float64
                    unit: mg/ml
                    m_annotations:
                      eln:
                        component: NumberEditQuantity
                sub_sections:
                  Solute:
                    section:
                      quantities:
                        Substance:
                          type: nomad.datamodel.metainfo.eln.ELNSubstance
                          m_annotations:
                            eln:
                              component: ReferenceEditQuantity
                        Mass:
                          type: np.float64
                          unit: kilogram
                          m_annotations:
                            eln:
                              component: NumberEditQuantity
                              defaultDisplayUnit: milligram
                  Solvent:
                    section:
                      quantities:
                        Substance:
                          type: nomad.datamodel.metainfo.eln.ELNSubstance
                          m_annotations:
                            eln:
                              component: ReferenceEditQuantity
                        Volume:
                          type: np.float64
                          unit: meter ** 3
                          m_annotations:
                            eln:
                              component: NumberEditQuantity
                              defaultDisplayUnit: milliliter
            Preparation:
              section:
                base_sections:
                  - nomad.datamodel.metainfo.eln.Process  
                m_annotations:
                  eln:
                    overview: true
    ```

    The tabular parser and plot can be added in various locations. In this case, we thought of adding it as a subsection of the main section, at the same hierarchy level of the subsections `Sample`, `Solution`, and `Preparation`. We already had the section definition of `Optical_absorption` in this tutorial page. Now it is just enough to provide this definition when `Optical_absorption` is a subsection of the main section, after adding the `section:` keyword (see guideline 4 for building custom ELN schemas):

       ```yaml
       Optical_absorption:
         section:
       ```  
      For this, we simply copy the section definition of the tabular parser (starting from `base_sections:` to the end of the YAML file) and use it as the definition of the new `Optical_absorption` subsection.

    Below is the final version of the polymer processing schema, now enhanced with an `Optical_absorption` subsection that supports file upload, parsing, and visualization. This YAML can be directly copied into a file and uploaded to NOMAD as a functional custom schema.

    ```yaml
    definitions:
      name: Processing of polymers thin-films
      sections:
        Experiment_Information:
          base_sections: 
            - nomad.datamodel.data.EntryData
          quantities:
            Name:
              type: str  
              default: Experiment title
              m_annotations:
                eln:
                  component: StringEditQuantity
            Researcher:
              type: str
              default: Name of the researcher who performed the experiment
              m_annotations:
                eln:
                  component: StringEditQuantity
            Date:
              type: Datetime
              m_annotations:
                eln:
                  component: DateTimeEditQuantity
            Additional_Notes:
              type: str
              m_annotations:
                eln:
                  component: RichTextEditQuantity
          sub_sections:
            Sample:
              section:
                base_sections:
                  - nomad.datamodel.metainfo.eln.Sample
                m_annotations:
                  eln:
                    overview: true
                    hide: ['chemical_formula']
            Solution:
              section:
                base_sections:
                  - nomad.datamodel.metainfo.eln.Sample
                m_annotations:
                  eln:
                    overview: true
                    hide: ['chemical_formula', 'description']
                quantities:
                  Concentration:
                    type: np.float64
                    unit: mg/ml
                    m_annotations:
                      eln:
                        component: NumberEditQuantity
                sub_sections:
                  Solute:
                    section:
                      quantities:
                        Substance:
                          type: nomad.datamodel.metainfo.eln.ELNSubstance
                          m_annotations:
                            eln:
                              component: ReferenceEditQuantity
                        Mass:
                          type: np.float64
                          unit: kilogram
                          m_annotations:
                            eln:
                              component: NumberEditQuantity
                              defaultDisplayUnit: milligram
                  Solvent:
                    section:
                      quantities:
                        Substance:
                          type: nomad.datamodel.metainfo.eln.ELNSubstance
                          m_annotations:
                            eln:
                              component: ReferenceEditQuantity
                        Volume:
                          type: np.float64
                          unit: meter ** 3
                          m_annotations:
                            eln:
                              component: NumberEditQuantity
                              defaultDisplayUnit: milliliter
            Preparation:
              section:
                base_sections:
                  - nomad.datamodel.metainfo.eln.Process  
                m_annotations:
                  eln:
                    overview: true
            Optical_absorption:
              section:
                base_sections:
                  - nomad.datamodel.data.EntryData
                  - nomad.parsing.tabular.TableData
                  - nomad.datamodel.metainfo.plot.PlotSection
                quantities:
                  info_about_data:
                    type: str
                    m_annotations:
                      eln:
                        component: RichTextEditQuantity          
                  data_file:
                    type: str
                    m_annotations:
                      eln:
                        component: FileEditQuantity
                      browser:
                        adaptor: RawFileAdaptor
                      tabular_parser:
                        parsing_options:
                          comment: '#'
                          skiprows: [1]
                        mapping_options:
                          - mapping_mode: column
                            file_mode: current_entry
                            sections:
                              - '#root'
                  wavelength:
                    type: np.float64
                    unit: nm
                    shape: ['*']
                    m_annotations:
                      tabular:
                        name: Wavelength
                  absorbance:
                    type: np.float64
                    shape: ['*']
                    m_annotations:
                      tabular:
                        name: Absorbance
                m_annotations:
                  plotly_graph_object:
                    data:
                      x: "#wavelength"
                      y: "#absorbance"
                  layout:
                    title: Optical Spectrum            
    ```