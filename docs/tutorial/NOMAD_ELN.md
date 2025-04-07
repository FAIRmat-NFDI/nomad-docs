# Using NOMAD as an Electronic Lab Notebook
In this tutorial, we will explore how to use NOMAD's Electronic Lab Notebook (ELN) functionality to record experiments effectively. You will learn how to create entries for substances and instruments, record samples along with their processing conditions, and the various measurements that make up your experiments. We will also cover NOMAD's built-in ELN templates, which help structure and interlink different aspects of an experiment, providing a clear, visual overview of the entire workflow.

In doing this, we will apply an example of an experiment on preparing solution-processed polymer thin-films and measuring their optical absorption spectrum.

??? example "About the example experiment used for this exercise"
    In this exercise, we will work with an example experiment involving the preparation and characterization of Poly(3-hexylthiophene-2,5-diyl) ("P3HT") thin films. The experiment consists of three main activities: preparing solutions, depositing thin films, and measuring optical absorption.

    1. **Preparing solutions:** The polymer powder is mixed with a solvent in predefined quantities to achieve the desired concentration. A scale is used to accurately weigh the polymer powder, ensuring precise solution concentration.

    2. **Depositing thin-films:** The prepared solution is used to create a thin film on a glass substrate through spin-coating. By carefully controlling the spin speed and duration, the desired film thickness is achieved.

    3. **Measuring optical absorption:** The optical absorption spectrum of the thin film is acquired using a UV-Vis-NIR spectrometer. The measurement results are saved as a .csv file for further analysis.

    To effectively document this experiment, we will create and interlink electronic lab notebook (ELN) entries in NOMAD. These entries will include key entities such as substances, instruments, and samples, as well as activities like material processing and measurements. By structuring the data in this way, we ensure a comprehensive and FAIR-compliant record of the experiment.

    ![Overview of the example entities and activities](images/ELN_2.png)

## Create a New ELN Upload

In NOMAD, an Electronic Lab Notebook (ELN) is created by initiating a NOMAD upload. This process allows you to structure and document your research data efficiently. For a step-by-step guide on how to create an upload, please refer to [this page](upload_publish.md#create-new-upload){:target="_blank"}.

## Create ELN Entries

The next step is to create entries for your substances, instruments, processes, and measurements. In NOMAD, each ELN entry is structured using templates called *built-in schema*. These templates are specifically designed to capture relevant information for different types of entries, ensuring consistency and completeness in documentation.

They include general fields tailored to the type of entry you are creating. The currently available ELN built-in schemas in NOMAD are illustrated in the figure below.

![ELN built-in base schema](images/ELN_1.png)

To create ELN entries using the templates provided by NOMAD, we will generate instances from the built-in schemas. This will automatically create entries with predefined fields, allowing us to efficiently fill in the relevant information of our experiment.

Follow these steps to create ELN entries using the built-in schema: *(click on the arrows to navigate between steps)*

<div class="image-slider" id="slider1">
    <div class="nav-arrow left" id="prev1">←</div>
    <img src="images/ELN_built-in_1.png" alt="Step 1" class="active">
    <img src="images/ELN_built-in_2.png" alt="Step 2">
    <img src="images/ELN_built-in_3.png" alt="Step 3">
    <img src="images/ELN_built-in_4.png" alt="Step 4">
    <div class="nav-arrow right" id="next1">→</div>
</div>

### Create a Substance Entry

Now, let's create an entry using the built-in *Substance ELN* schema for **P3HT powder**. Follow the steps of creating an entry described above and select *Substance ELN* from the drop-down menu in step 4.

<div style="text-align: center;">
    <img src="images/ELN_built-in_5.png" alt="P3HT powder ELN substance entry" width="400">
</div>

??? info "Input fields offered by the built-in schema *Substance ELN*"
    The built-in schema *Substance ELN*  provides the following fields for input:

    - **substance name:** Automatically used as the entry name.
    - **tags:** User selected tags to improve searchability.
    - **datetime:** Allows entry of a date/time stamp.
    - **substance ID:** A unique, human-readable ID for the substance.
    - **detailed substance description:** A free text field for additional information.

    Additional subsections available in the *data* subsection include:

    - **elemental composition:** Define the chemical composition with atomic and mass fractions.
    - **pure substance:** Specify if the material is a pure substance purchased from an external vendor, with fields like:
        - Substance name
        - IUPAC name
        - Molecular formula
        - CAS number
        - Inchi Key, SMILES, and more.
    - **substance identifier:** Add identifiers for specific substances.

Once the entry is created, we can fill in the relevant fields with detailed and accurate information. Fields can also be updated as needed to keep the entry accurate and useful.

See the example below. *(click the arrows to navigate through the steps)*

<div class="image-slider" id="slider2">
    <div class="nav-arrow left" id="prev2">←</div>
    <img src="images/ELN_built-in_6.png" alt="Step 1" class="active">
    <img src="images/ELN_built-in_7.png" alt="Step 2">
    <img src="images/ELN_built-in_8.png" alt="Step 3">
    <img src="images/ELN_built-in_9.png" alt="Step 4">
    <img src="images/ELN_built-in_10.png" alt="Step 5">
    <img src="images/ELN_built-in_11.png" alt="Step 6">
    <div class="nav-arrow right" id="next2">→</div>
</div>

??? task "Task: Create an ELN entry for substances"
    Create an ELN entry in NOMAD for the following substances:

    - Chloroform
    - Glass substrate

    Use the *Substance ELN* schema and include as many details as you like (e.g., Substance Name, Datetime, Substance ID, Description).

-----------------
### Create a Sample Entry

Now, let's create an entry using the built-in *Generic Sample ELN* schema for **P3HT Thin Film**. Follow the steps of creating an entry described above and select *Generic Sample ELN* from the drop-down menu in step 4.

<div style="text-align: center;">
    <img src="images/ELN_built-in_12.png" alt="P3HT thin-film sample ELN substance entry" width="400">
</div>


??? info "Input fields offered by the built-in schema *Generic Sample ELN*"
    The built-in schema *Generic Sample ELN* provides the following fields for input:

    - **name:** Automatically used as the entry name.
    - **tags:** User selected tags to improve searchability.
    - **datetime:** Allows entry of a date/time stamp.
    - **ID:** A unique, human-readable ID for the sample.
    - **description:** A free text field for additional information.

    Additional subsections available in the *data* subsection include:

    - **elemental composition:** Define the chemical composition with atomic and mass fractions.
    - **components:** Specify the components used to create the sample, including raw materials or system components.
    - **sample identifier:** Add unique identifiers for the sample.

Once the entry is created, we can fill in the relevant fields with detailed and accurate information. Fields can also be updated as needed to keep the entry accurate and useful.

See the example below. *(click the arrows to navigate through the steps)*

<div class="image-slider" id="slider3">
    <div class="nav-arrow left" id="prev3">←</div>
    <img src="images/ELN_built-in_13.png" alt="Step 1" class="active">
    <img src="images/ELN_built-in_14.png" alt="Step 2">
    <img src="images/ELN_built-in_15.png" alt="Step 3">
    <img src="images/ELN_built-in_16.png" alt="Step 4">
    <img src="images/ELN_built-in_17.png" alt="Step 5">
    <img src="images/ELN_built-in_18.png" alt="Step 6">
    <div class="nav-arrow right" id="next3">→</div>
</div>

??? task "Task: Create an ELN entry for a sample"

    Create an ELN entry in NOMAD for P3HT solution in chloroform.
    Reference the sample to its components (P3HT powder and chloroform).

    Use the *Generic Sample ELN* schema and include as many details as you like (e.g., Short Name, Datetime, ID, Description).

-----------------
### Create an Instrument Entry

Now, let's create an entry using the built-in *Instrument ELN* schema for **scale**. Follow the steps of creating an entry described above and select *Instrument ELN* from the drop-down menu in step 4.

<div style="text-align: center;">
    <img src="images/ELN_built-in_19.png" alt="Scale ELN instrument entry" width="400">
</div>

??? info "Input fields offered by the built-in schema *Instrument ELN*"
    The built-in schema *Instrument ELN* provides the following fields for input:

    - **name:** Automatically used as the entry name.
    - **tags:** User selected tags to improve searchability.
    - **datetime:** Allows entry of a date/time stamp.
    - **ID:** A unique, human-readable ID for the.
    - **description:** A free text field for additional information.

    Additional subsections available in the *data* subsection include:

    - **instrument identifiers:** Specify the type of instrument and additional metadata, if applicable.

Once the entry is created, we can fill in the relevant fields with detailed and accurate information. Fields can also be updated as needed to keep the entry accurate and useful.

See the example below. *(click the arrows to navigate through the steps)*

<div class="image-slider" id="slider4">
    <div class="nav-arrow left" id="prev4">←</div>
    <img src="images/ELN_built-in_20.png" alt="Step 1" class="active">
    <img src="images/ELN_built-in_21.png" alt="Step 2">
    <div class="nav-arrow right" id="next4">→</div>
</div>

??? task "Task: Create an ELN entry for an instrument"
    Create an ELN entry in NOMAD for one of the following instruments:

    - Optical Spectrometer
    - Spin Coater

    Use the *Instrument ELN* schema and include as many details as you like (e.g., name, datetime, ID, description).

-----------------

### Create a Process Entry

Now, let's create an entry using the built-in *Material Processing ELN* schema for **Preparation of P3HT solution**. Follow the steps of creating an entry described above and select *Materials Processing ELN* from the drop-down menu in step 4.

<div style="text-align: center;">
    <img src="images/ELN_built-in_22.png" alt="Material Processing ELN entry" width="400">
</div>

??? info "Input fields offered by the built-in schema *Material Processing ELN*"
    The *Material Processing ELN* schema provides the following fields for input:

    - **name:** Automatically used as the entry name.
    - **starting time and ending time:** Allows entry of a date/time stamp for the process duration.
    - **tags:** User selected tags to improve searchability.
    - **ID:** A unique, human-readable ID for the process.
    - **location:** A text field specifying the location where the process took place.
    - **description:** A free text field for additional information about the process.

    Additional subsections available in the *data* subsection include:

    - **steps:** Define the step-by-step procedure for the material processing.
    - **process identifier:** Add unique identifiers for the process.
    - **instruments:** List the instruments used in the process.
    - **samples:** Specify the samples that are created or used in the process.

Once the entry is created, we can fill in the relevant fields with detailed and accurate information. Fields can also be updated as needed to keep the entry accurate and useful.

See the example below (click the arrows to navigate through the steps).

<div class="image-slider" id="slider5">
    <div class="nav-arrow left" id="prev5">←</div>
    <img src="images/ELN_built-in_23.png" alt="step 1" class="active">
    <img src="images/ELN_built-in_24.png" alt="step 2">
    <img src="images/ELN_built-in_25.png" alt="step 3">
    <img src="images/ELN_built-in_26.png" alt="step 4">
    <img src="images/ELN_built-in_27.png" alt="step 5">
    <img src="images/ELN_built-in_28.png" alt="step 6">
    <div class="nav-arrow right" id="next5">→</div>
</div>

??? task "Task: Reference a sample to your process ELN"
    For the Process ELN entry created above, make a reference to a sample entry called *P3HT_solution_in_CF*.

    - If the P3HT_solution_in_CF sample entry already exists, simply link to it within the samples subsection of your Process ELN entry.
    - If the sample entry does not exist, first create a Sample ELN entry named P3HT_solution_in_CF, then add the reference in the Process ELN entry.

**Defining the steps of a process**

The *steps* subsection in the *Materials Processing ELN* allows us to document each stage of the process and visualize them in an interactive workflow graph.

For the example process entry **Preparation of P3HT solution**, we will define the following three steps:

1. weighing the powder
2. filling the solvent
3. mixing the solution

Follow these steps to define the process stages in your material processing entry: *(click on the arrows to navigate between steps)*

<div class="image-slider" id="slider6">
    <div class="nav-arrow left" id="prev6">←</div>
    <img src="images/ELN_built-in_29.png" alt="step 1" class="active">
    <img src="images/ELN_built-in_30.png" alt="step 2">
    <img src="images/ELN_built-in_31.png" alt="step 3">
    <img src="images/ELN_built-in_32.png" alt="step 4">
    <div class="nav-arrow right" id="next6">→</div>
</div>

Note that the added information in the **subsections** will be used to automatically fill in the Workflow graph as **tasks**, as well as **the References section**. You can find the Workflow Graph the in **OVERVIEW** tab of the entry.

<div style="text-align: center;">
    <img src="images/ELN_built-in_33.png" alt="Process workflow graph" width="400">
</div>

The workflow graph can be modified and enriched by adding additional information such as **inputs**, **additional tasks**, and **outputs** for each step. You can do this in the **workflow2** section.

The **workflow2** section of the **Preparation of P3HT solution** example can be found under the **DATA** tab, in the left panel under **workflow2**. We can now add inputs, by referencing existing substance entries.

See the example below. *click the arrows to navigate through the steps*.

<div class="image-slider" id="slider7">
    <div class="nav-arrow left" id="prev7">←</div>
    <img src="images/ELN_built-in_34.png" alt="step 1" class="active">
    <img src="images/ELN_built-in_35.png" alt="step 2">
    <img src="images/ELN_built-in_36.png" alt="step 3">
    <img src="images/ELN_built-in_37.png" alt="step 4">
    <div class="nav-arrow right" id="next7">→</div>
</div>

??? task "Task: Reference P3HT powder as input for the process"
    For the Process ELN entry created above, make reference to the substance ELN entry *P3HT Powder* as an input of the process.

    *Tip:* Use the workflow2 section of the entry.

We can now see the changes in the workflow graph based on our modifications in the workflow section.

<div style="text-align: center;">
    <img src="images/ELN_built-in_38.png" alt="Process workflow graph" width="400">
</div>

-----------------

### Create a Measurement Entry

Now, let's create an entry using the built-in *Measurement ELN* schema for **Optical absorption measurement**. Follow the steps of creating an entry described above and select *Measurement ELN* from the drop-down menu in step 4.

<div style="text-align: center;">
    <img src="images/ELN_built-in_39.png" alt="Material Processing ELN entry" width="400">
</div>

??? info "Input fields offered by the built-in schema *Measurement ELN*"
    - **name:** Automatically used as the entry name.
    - **starting time** Allows entry of a date/time stamp for the measurement.
    - **tags:** User selected tags to improve searchability.
    - **ID:** A unique, human-readable ID for the process.
    - **location:** A text field specifying the location where the process took place.
    - **description:** A free text field for additional information about the process.

    Additional subsections available in the *data* subsection include:

    - **steps:** Define the step-by-step procedure for the material processing.
    - **samples:** Specify the samples that are being measured.
    - **measurement identifier:** Add unique identifiers for the measurement.
    - **instruments:** List the instruments used in the measurement.
    - **results:** Provide information about the results of the measurements (text and images).

Once the entry is created, we can fill in the relevant fields with detailed and accurate information. Fields can also be updated as needed to keep the entry accurate and useful.

See the example below. *(click the arrows to navigate through the steps)*

<div class="image-slider" id="slider8">
    <div class="nav-arrow left" id="prev8">←</div>
    <img src="images/ELN_built-in_40.png" alt="Step 1" class="active">
    <img src="images/ELN_built-in_41.png" alt="Step 2">
    <img src="images/ELN_built-in_42.png" alt="Step 3">
    <img src="images/ELN_built-in_43.png" alt="Step 4">
    <img src="images/ELN_built-in_44.png" alt="Step 5">
    <img src="images/ELN_built-in_45.png" alt="Step 6">
    <img src="images/ELN_built-in_46.png" alt="Step 7">
    <img src="images/ELN_built-in_47.png" alt="Step 8">
    <div class="nav-arrow right" id="next8">→</div>
</div>

--------------

### Integrate Your Experiment

Once all substances, samples, processes, and measurements are defined, you can integrate them into a structured workflow using the *Experiment ELN* schema. The *Experiment ELN* schema allows linking *processes* and *measurements* into a single entry for a comprehensive overview of your experimental workflow.

To create an entry using the built-in *Experiment ELN* schema for **Characterization of P3HT**. Follow the steps of creating an entry described above and select *Experiment ELN* from the drop-down menu in step 4.

<div style="text-align: center;">
    <img src="images/ELN_built-in_48.png" alt="Experiment ELN entry" width="400">
</div>

??? info "Input fields offered by the built-in schema *Experiment ELN*"
    - **name:** Automatically used as the entry name.
    - **starting time** Allows entry of a date/time stamp for the measurement.
    - **tags:** User selected tags to improve searchability.
    - **ID:** A unique, human-readable ID for the process.
    - **location:** A text field specifying the location where the process took place.
    - **description:** A free text field for additional information about the process.

    Additional subsections available in the *data* subsection include:

    - **steps:** Define the step-by-step procedure for the material processing.
    - **experiment identifiers:** Specify the additional metadata for the experiment.

The *steps* subsection allows us to reference the various processes and measurements that were part of the experiments. By organizing these elements into a structured and interactive workflow, we can provide a clearer overview of the experimental sequence, enabling better visualization and understanding of how different steps are interconnected.


<div style="text-align: center;">
    <img src="images/ELN_built-in_39.gif" alt="interactive workflow gif" width="400">
</div>

--------------------
## Exploring and Searching Your ELN

??? example "Download the example file for this exercise"
    We have prepared a compressed file for this task, which can be downloaded from this [link](https://github.com/FAIRmat-NFDI/FAIRmat-tutorial-16/raw/refs/heads/main/tutorial_16_materials/part_4_files/example_NOMAD_ELN.zip).

    The file contains multiple NOMAD ELN entries in `.json` format.

    These entries have been created using the NOMAD ELN built-in schema, organized into folders, and categorized with custom tags.

    You can drag and drop this file into a new upload in NOMAD to view its contents.

Imagine you have created multiple entries of substances, samples, instruments, processes, and measurements, and you need to quickly find a specific experiment or material. Instead of manually searching through files, NOMAD’s ELN allows you to search, filter, and organize your entries—saving you time and effort.

??? info "Organizing your ELN upload"
    NOMAD is a file-based system. You can access, organize, and download your files within each upload. You can also create folders to categorize entries into materials, samples, instruments, processes, and results, as well as upload additional documents, such as relevant PDFs.

    !!! warning "If you plan to organize your entries into separate folders, do so before you reference them to each other. Moving them afterward may break the reference links."

    You can follow these steps to organize your ELN entries:

    1. Navigate to the **FILES** tab in your upload. This view functions like a file explorer, allowing you to view and manage files.
    <div style="text-align: center;">
    <img src="images/files_explorer_in_NOMAD.png" alt="interactive workflow gif" width="400">
    </div>

    2. Add new folders and organize them according to your needs.
    <div style="text-align: center;">
        <img src="images/creating_new_folders.gif" alt="interactive workflow gif" width="400">
    </div>

    3. Drag and drop files into the desired folder. A prompt will appear, asking if you want to copy or move the files—choose according to your needs.
    <div style="text-align: center;">
        <img src="images/moving_files_to_a_folder.gif" alt="interactive workflow gif" width="400">
    </div>

    4. Once all files are sorted, take a moment to review the structure. Here’s an example of an organized ELN
    <div style="text-align: center;">
        <img src="images/after_organization.png" alt="interactive workflow gif" width="400">
    </div>

**Searching your ELN entries**

To search for entries in your ELN, follow these steps:

1. on the top of the ELN upload page, click on the <img src="images/icon_search_upload.png" alt="Search ELN icon" width="20"> icon.

    ![screenshot of step 1](images/explore_ELN_step_1.png)

2. From the drop-down menu, select *Entries*.

    ![screenshot of step 2](images/explore_ELN_step_2.png)

    This will open NOMAD's **EXPLORE** page with a filter applied to display only the entries from your upload.

    ![screenshot of NOMAD EXPLORE page wiht the filter applied](images/explore_ELN_step_2r.png)

On the **EXPLORE** page, you can use the filter options in the sidebar to refine your search, enter specific keywords in the search bar to find relevant entries, or create custom widgets to visualise your ELN data.

??? info "Filtering entries in NOMAD"
    NOMAD provides various filters that can be used to efficiently find your ELN entries, but the following two filters are particularlly effective:

    - Filter by built-in schema used to create the entry.

        *For example, ELNInstrument, ELNSubstances, ELNSample, etc.*

    - Filter by custom tags, where you assign common tags to related entries for easy grouping.

        *For example, tag all solvents as "my_solvent" or all samples as "my_samples".*

    Using these filters helps you quickly locate specific entries in your ELN.

**Customize your search interface with widgets**

Widgets allow you to customize your search interface to better suit your data exploration needs. By adding and rearranging widgets, you can create a personalized view that highlights the most relevant filters, metadata, or visualizations most relevant to your research.

??? task "Create a custom widget for ELN sections and custom tags"
    To create a custom widget for filtering your ELN, follow these steps:

    1. Click on the `+ TERMS` button to open the *Edit terms widget* menu.

    <div style="text-align: center;">
        <img src="images/widget_step_1.png" alt="Screenshot of the Edit terms widget menu" width="800">
    </div>

    2. In the *Search quantity* field, type *eln*. A list of available filters will appear.

    3. Select `results.eln.sections` from the list. This will enable filtering based on the built-in ELN sections available in your ELN upload.

    <div style="text-align: center;">
        <img src="images/widget_step_2_3.png" alt="Screenshot of selecting results.eln.sections filter" width="400">
    </div>

    4. Write a descriptive title for the custom widget in *Title field*.

    5. Click DONE!

    <div style="text-align: center;">
        <img src="images/widget_step_4_5.png" alt="Screenshot of finalizing the custom widget" width="400">
    </div>

    The new ELN sections widget now appears at the top of your **EXPLORE** page and displays ELN entry types along with their corresponding counts.

    <div style="text-align: center;">
        <img src="images/widget_step_5r.png" alt="Screenshot of the newly created ELN sections widget" width="400">
    </div>

    You can now follow the same steps to create a custom widget for filtering by custom tags.

    In Step 3, instead of selecting `results.eln.sections`, choose `results.eln.tags`. This will create a widget that filters your ELN entries based on the custom tags you have assigned.

    This widget will then appear on your **EXPLORE** page, allowing you to quickly view and filter entries by their associated tags.

    <div style="text-align: center;">
        <img src="images/explore_you_ELN_entries.gif" alt="Animation of filtering using widgets" width="800">
    </div>

----------------