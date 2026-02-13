# NOMAD Plugin Registry

This page contains information about all NOMAD plugins owned and maintained by  the GitHub organizations: FAIRmat-NFDI, nomad-coe.  The information is automatically updated monthly. **Last Updated:** 2026-02-13 10:49 UTC

[Browse All Plugins in the NOMAD Plugins App](https://nomad-lab.eu/prod/v1/oasis/gui/search/plugins){:.md-button .nomad-button target="_blank" rel="noopener"}

## Available Plugins

Quick reference table of all available plugins:

<div class="plugin-registry-filter" data-plugin-registry-filter>
<label class="plugin-registry-filter__label">Containing</label>
<select class="plugin-registry-filter__select">
<option value="">All entry point types</option>
<option value="App">App</option>
<option value="Example upload">Example upload</option>
<option value="Normalizer">Normalizer</option>
<option value="Parser">Parser</option>
<option value="Schema package">Schema package</option>
</select>
<button class="plugin-registry-filter__clear" type="button">Clear</button>
<span class="plugin-registry-filter__count" aria-live="polite"></span>
</div>

<div class="plugin-registry-chart" data-plugin-registry-chart>
<p class="plugin-registry-chart__title"><strong>Plugin Type Distribution (Filtered)</strong></p>
<div class="plugin-registry-chart__content">
<div class="plugin-registry-chart__pie-wrap">
<div class="plugin-registry-chart__pie" role="img" aria-label="Plugin type distribution pie chart">
<span class="plugin-registry-chart__pie-total">0</span>
</div>
</div>
<div class="plugin-registry-chart__legend"></div>
</div>
</div>

<table class="plugin-registry-table" data-plugin-registry="true">
<thead>
<tr><th>Plugin</th><th>Description</th><th>Deployment</th><th>Links</th></tr>
</thead>
<tbody>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-0" data-entry-point-types="app|schema package">
<td><strong>nomad-aitoolkit </strong>(⭐ 0)<br><small>App, Schema package</small></td>
<td>Schema and app for AI Toolkit notebooks.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-aitoolkit" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-aitoolkit/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-0">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Adam Fekete<br>
<strong>Maintainers:</strong> Adam Fekete<br>
<strong>Entry Points:</strong> <code>aitookitschema</code>, <code>aitookitapp</code><br>
<strong>Created:</strong> 2024-05-24 | <strong>Last Updated:</strong> 2025-01-23
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-1" data-entry-point-types="schema package">
<td><strong>nomad-analysis </strong>(⭐ 2)<br><small>Schema package</small></td>
<td>A NOMAD plugin for analysis of FAIR data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-analysis" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-analysis/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-1">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Sarthak Kapoor, Jose M. Pizarro, Andrea Albino, Hampus Näsström, Sebastian Brückner<br>
<strong>Maintainers:</strong> FAIRmat<br>
<strong>Entry Points:</strong> <code>general_analysis_schema</code>, <code>jupyter_analysis_schema</code><br>
<strong>Created:</strong> 2024-02-26 | <strong>Last Updated:</strong> 2025-11-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-2" data-entry-point-types="app|example upload|schema package">
<td><strong>nomad-auto-xrd </strong>(⭐ 1)<br><small>App, Example upload, Schema package</small></td>
<td>A NOMAD plugin containing schemas for automatic XRD analysis.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-auto-xrd" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-2">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Pepe Márquez, Sarthak Kapoor<br>
<strong>Maintainers:</strong> FAIRmat<br>
<strong>Entry Points:</strong> <code>schema</code>, <code>models_app</code>, <code>example_upload</code>, <code>auto_xrd_training_action</code>, <code>auto_xrd_training_wandb_action</code>, <code>auto_xrd_analysis_action</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code>, <code>nomad-analysis</code>, <code>nomad-schema-plugin-simulation-workflow</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-09-13 | <strong>Last Updated:</strong> 2025-12-18
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-3" data-entry-point-types="app|parser|schema package">
<td><strong>nomad-battery-database </strong>(⭐ 1)<br><small>App, Parser, Schema package</small></td>
<td>app for battery database</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-battery-database" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-battery-database/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-3">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Uday Gajera<br>
<strong>Maintainers:</strong> Uday Gajera<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2025-02-16 | <strong>Last Updated:</strong> 2025-12-13
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-4" data-entry-point-types="app|example upload|schema package">
<td><strong>nomad-bayesian-optimization </strong>(⭐ 1)<br><small>App, Example upload, Schema package</small></td>
<td>NOMAD plugin for driving experiments/simulations using bayesian optimization</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-bayesian-optimization" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-4">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Lauri Himanen<br>
<strong>Maintainers:</strong> Lauri Himanen<br>
<strong>Entry Points:</strong> <code>nomad_bayesian_optimization.apps:bayesian_optimization_tasks</code>, <code>nomad_bayesian_optimization.schema_packages:experiments</code>, <code>nomad_bayesian_optimization.schema_packages:bayesian_optimization</code>, <code>nomad_bayesian_optimization.example_uploads:getting_started</code>, <code>nomad_bayesian_optimization.example_uploads:optimization_tasks</code><br>
<strong>Created:</strong> 2024-06-17 | <strong>Last Updated:</strong> 2025-05-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-5" data-entry-point-types="app|parser|schema package">
<td><strong>nomad-camels-plugin </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>Parser for HDF5 files coming from NOMAD CAMELS.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-camels-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-camels-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-5">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Alexander Fuchs<br>
<strong>Maintainers:</strong> Alexander Fuchs<br>
<strong>Entry Points:</strong> <code>camels_schema_package</code>, <code>camels_parser</code>, <code>camelsDiode_parser</code>, <code>camels_app</code><br>
<strong>Created:</strong> 2024-11-05 | <strong>Last Updated:</strong> 2025-12-18
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-6" data-entry-point-types="app|example upload|parser|schema package">
<td><strong>nomad-catalysis </strong>(⭐ 4)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>A NOMAD plugin for heterogeneous catalysis data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-catalysis-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-catalysis-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-6">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Julia Schumann, Hampus Näsström, Michael Götte<br>
<strong>Maintainers:</strong> Julia Schumann, FAIRmat<br>
<strong>Entry Points:</strong> <code>catalysis</code>, <code>catalysis_app</code>, <code>catalysis_parser</code>, <code>catalysis_collection</code>, <code>example_catalysis</code><br>
<strong>Created:</strong> 2024-07-15 | <strong>Last Updated:</strong> 2025-11-13
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-7" data-entry-point-types="app|parser|schema package">
<td><strong>nomad-countries </strong>(⭐ 100)<br><small>App, Parser, Schema package</small></td>
<td>Countries of the world plugin</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-7">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> John Doe<br>
<strong>Maintainers:</strong> John Doe<br>
<strong>Entry Points:</strong> <code>countryparser</code>, <code>countrypackage</code>, <code>countryapp</code><br>
<strong>Created:</strong> 2021-02-18 | <strong>Last Updated:</strong> 2025-12-18
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-8" data-entry-point-types="schema package">
<td><strong>nomad-crystallm </strong>(⭐ 1)<br><small>Schema package</small></td>
<td>A NOMAD plugin for running CrystaLLM inference in NOMAD installations.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-crystallm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-crystallm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-8">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Ahmed Ilyas, Sarthak Kapoor<br>
<strong>Maintainers:</strong> FAIRmat<br>
<strong>Entry Points:</strong> <code>crystallm_inference</code>, <code>crystallm_schemas</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2025-06-10 | <strong>Last Updated:</strong> 2025-10-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-9" data-entry-point-types="schema package">
<td><strong>nomad-eos-workflows </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>A NOMAD plugin containing the section definitions of a standard Equation of State (EoS) workflow.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-schema-plugin-eos-workflows" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-9">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Joseph Rudzinski<br>
<strong>Maintainers:</strong> Joseph Rudzinski<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-04-01 | <strong>Last Updated:</strong> 2025-04-01
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-10" data-entry-point-types="example upload|parser|schema package">
<td><strong>nomad-external-eln-integrations </strong>(⭐ 0)<br><small>Example upload, Parser, Schema package</small></td>
<td>3rd Party Integration packages</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-external-eln-integrations" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-10">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Amir Golparvar<br>
<strong>Maintainers:</strong> Amir Golparvar<br>
<strong>Entry Points:</strong> <code>elabftwparser</code>, <code>chemotionparser</code>, <code>labfolderschema</code>, <code>elabftwschema</code>, <code>openbisschema</code>, <code>elabftwexample</code><br>
<strong>Created:</strong> 2024-10-01 | <strong>Last Updated:</strong> 2025-10-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-11" data-entry-point-types="schema package">
<td><strong>nomad-gallery </strong>(⭐ 1)<br><small>Schema package</small></td>
<td>A mkdocs-based GitHub Pages site for showcasing NOMAD features, examples, and use cases.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-gallery" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-gallery/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-11">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Joseph Rudzinski<br>
<strong>Maintainers:</strong> Joseph Rudzinski<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-02-17 | <strong>Last Updated:</strong> 2025-12-14
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-12" data-entry-point-types="schema package">
<td><strong>nomad-material-processing </strong>(⭐ 11)<br><small>Schema package</small></td>
<td>A plugin for NOMAD containing base sections for material processing.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-material-processing" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-material-processing/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-12">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Andrea Albino, Sebastian Brückner, Michael Götte, Ahmed Ilyas, Sarthak Kapoor, José A. Márquez, Hampus Näsström, Markus Scheidgen<br>
<strong>Maintainers:</strong> FAIRmat<br>
<strong>Entry Points:</strong> <code>general_schema</code>, <code>solution_schema</code>, <code>vd_schema</code>, <code>cvd_schema</code>, <code>movpe_schema</code>, <code>pvd_schema</code>, <code>mbe_schema</code>, <code>pld_schema</code>, <code>sputtering_schema</code>, <code>thermal_schema</code><br>
<strong>Created:</strong> 2023-08-15 | <strong>Last Updated:</strong> 2025-08-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-13" data-entry-point-types="app|example upload|parser|schema package">
<td><strong>nomad-material-processing-example </strong>(⭐ 2)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>An example plugin to demonstrate the use of schemas from the nomad-material-processing plugin.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-material-processing-example" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-13">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Sarthak Kapoor<br>
<strong>Maintainers:</strong> Sarthak Kapoor<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-02-18 | <strong>Last Updated:</strong> 2025-08-06
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-14" data-entry-point-types="parser|schema package">
<td><strong>nomad-measurements </strong>(⭐ 14)<br><small>Parser, Schema package</small></td>
<td>A plugin for NOMAD containing base sections for measurements.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-measurements" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-measurements/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-14">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Andrea Albino, Sebastian Brückner, Sarthak Kapoor, José A. Márquez, Rubel Mozumder, Hampus Näsström<br>
<strong>Maintainers:</strong> FAIRmat<br>
<strong>Entry Points:</strong> <code>general_schema</code>, <code>xrd_schema</code>, <code>xrd_parser</code>, <code>qd_eto_schema</code>, <code>qd_act_schema</code>, <code>qd_acms_schema</code>, <code>qd_mpms_schema</code>, <code>qd_resisitivity_schema</code>, <code>qd_eto_parser</code>, <code>qd_act_parser</code>, <code>qd_acms_parser</code>, <code>qd_mpms_parser</code>, <code>qd_resistivity_parser</code>, <code>qd_sequence_parser</code>, <code>transmission_schema</code>, <code>transmission_parser</code>, <code>mapping_schema</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2023-09-06 | <strong>Last Updated:</strong> 2025-11-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-15" data-entry-point-types="schema package">
<td><strong>nomad-neb-workflows </strong>(⭐ 4)<br><small>Schema package</small></td>
<td>A NOMAD plugin containing the section definitions of a standard Nudged Elastic Band (NEB) workflow.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-neb-workflows" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-neb-workflows/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-15">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Julia Schumann, Uday Gajera, Jose M. Pizarro, Hampus Näsström<br>
<strong>Maintainers:</strong> Julia Schumann, Uday Gajera, Hampus Näsström<br>
<strong>Entry Points:</strong> <code>nomad_neb_workflows_plugin</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-normalizer-plugin-simulation-workflow</code>, <code>nomad-normalizer-plugin-soap</code>, <code>nomad-simulations</code>, <code>nomad-normalizer-plugin-spectra</code>, <code>nomad-schema-plugin-run</code>, <code>nomad-normalizer-plugin-bandstructure</code>, <code>nomad-parser-plugins-workflow</code>, <code>nomad-parser-plugins-database</code>, <code>nomad-normalizer-plugin-system</code>, <code>nomad-schema-plugin-simulation-workflow</code>, <code>nomad-parser-plugins-electronic</code>, <code>nomad-normalizer-plugin-dos</code>, <code>nomad-parser-plugins-atomistic</code><br>
<strong>Created:</strong> 2024-06-21 | <strong>Last Updated:</strong> 2025-12-13
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-16" data-entry-point-types="schema package">
<td><strong>nomad-nmr-schema </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>Schema plugin containing shared classes for NMR metadata</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-schema-plugin-nmr" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-16">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Andrea Albino<br>
<strong>Maintainers:</strong> Andrea Albino<br>
<strong>Entry Points:</strong> <code>nmr_schema</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code><br>
<strong>Created:</strong> 2025-03-25 | <strong>Last Updated:</strong> 2025-12-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-17" data-entry-point-types="normalizer">
<td><strong>nomad-normalizer-plugin-bandstructure </strong>(⭐ 1)<br><small>Normalizer</small></td>
<td>Band structure normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-bandstructure" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-bandstructure/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-17">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>bandstructurenormalizer</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-normalizer-plugin-system</code>, <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2023-12-23 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-18" data-entry-point-types="normalizer">
<td><strong>nomad-normalizer-plugin-dos </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>DOS normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-dos" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-dos/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-18">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>dosnormalizer</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-normalizer-plugin-system</code>, <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2023-12-20 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-19" data-entry-point-types="normalizer">
<td><strong>nomad-normalizer-plugin-simulation-workflow </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>Simulation workflow nomad plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-simulation-workflow" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-simulation-workflow/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-19">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>simulationworkflownormalizer</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2023-12-01 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-20" data-entry-point-types="normalizer">
<td><strong>nomad-normalizer-plugin-soap </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>SOAP nomad plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-soap" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-20">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>soapnormalizer</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2024-01-15 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-21" data-entry-point-types="normalizer">
<td><strong>nomad-normalizer-plugin-spectra </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>Spectra normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-spectra" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-spectra/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-21">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>spectranormalizer</code><br>
<strong>Created:</strong> 2024-01-15 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-22" data-entry-point-types="normalizer">
<td><strong>nomad-normalizer-plugin-system </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>System normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-system" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-system/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-22">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>systemnormalizer</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2023-12-29 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-23" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-edmft </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-edmft" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-23">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Jose Pizarro<br>
<strong>Maintainers:</strong> Jose Pizarro<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2024-09-05 | <strong>Last Updated:</strong> 2024-11-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-24" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-fhiaims </strong>(⭐ 2)<br><small>Parser, Schema package</small></td>
<td>Standalone NOMAD plugin for parsing FHI-aims calculation files</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-fhiaims" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-24">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Nathan Daelman<br>
<strong>Maintainers:</strong> Nathan Daelman<br>
<strong>Entry Points:</strong> <code>fhiaimsparser</code>, <code>fhiaimsschemapackage</code><br>
<strong>Created:</strong> 2024-06-24 | <strong>Last Updated:</strong> 2025-01-09
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-25" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-gsd </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>Parser for trajectory files in GSD format (<https://gsd.readthedocs.io/en/v3.3.1/).></td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-gsd" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-25">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Bernadette Mohr<br>
<strong>Maintainers:</strong> Bernadette Mohr<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code><br>
<strong>Created:</strong> 2024-08-28 | <strong>Last Updated:</strong> 2024-12-12
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-26" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-h5md </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser plugin for h5md-based simulation files.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-h5md" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-26">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Joseph Rudzinski<br>
<strong>Maintainers:</strong> Joseph Rudzinski<br>
<strong>Entry Points:</strong> <code>h5md_parser_entry_point</code>, <code>h5md_schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-simulation-workflow</code>, <code>nomad-simulations</code><br>
<strong>Created:</strong> 2024-09-10 | <strong>Last Updated:</strong> 2025-04-09
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-27" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-molpro </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-molpro" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-27">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Esma Boydas<br>
<strong>Maintainers:</strong> Esma Boydas<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2024-10-10 | <strong>Last Updated:</strong> 2024-10-10
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-28" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-orca </strong>(⭐ 2)<br><small>Parser, Schema package</small></td>
<td>nomad plugin for ORCA calculations</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-orca" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-28">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Esma Boydas<br>
<strong>Maintainers:</strong> Esma Boydas<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code><br>
<strong>Created:</strong> 2024-09-09 | <strong>Last Updated:</strong> 2025-01-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-29" data-entry-point-types="parser">
<td><strong>nomad-parser-plugin-boss </strong>(⭐ 1)<br><small>Parser</small></td>
<td>Plugin for parsing and displaying BOSS PES arftifacts</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-plugin-boss" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-29">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Nathan Daelman<br>
<strong>Maintainers:</strong> Nathan Daelman<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code><br>
<strong>Created:</strong> 2024-11-19 | <strong>Last Updated:</strong> 2025-11-20
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-30" data-entry-point-types="parser">
<td><strong>nomad-parser-plugins-atomistic </strong>(⭐ 7)<br><small>Parser</small></td>
<td>Collection of NOMAD parsers for atomistic codes.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/atomistic-parsers" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-30">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>amberparser</code>, <code>asapparser</code>, <code>aseparser</code>, <code>bopfoxparser</code>, <code>dftbplusparser</code>, <code>dlpolyparser</code>, <code>gromacsparser</code>, <code>gromosparser</code>, <code>gulpparser</code>, <code>h5mdparser</code>, <code>lammpsparser</code>, <code>libatomsparser</code>, <code>namdparser</code>, <code>tinkerparser</code>, <code>xtbparser</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2022-02-19 | <strong>Last Updated:</strong> 2025-11-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-31" data-entry-point-types="parser">
<td><strong>nomad-parser-plugins-electronic </strong>(⭐ 23)<br><small>Parser</small></td>
<td>Collection of NOMAD parsers for electronic structure codes.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/electronic-parsers" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-31">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>abacusparser</code>, <code>abinitparser</code>, <code>amsparser</code>, <code>atkparser</code>, <code>bigdftparser</code>, <code>castepparser</code>, <code>charmmparser</code>, <code>cp2kparser</code>, <code>cpmdparser</code>, <code>crystalparser</code>, <code>dmol3parser</code>, <code>edmftparser</code>, <code>elkparser</code>, <code>excitingparser</code>, <code>fhiaimsparser</code>, <code>fleurparser</code>, <code>fploparser</code>, <code>gamessparser</code>, <code>gaussianparser</code>, <code>gpawparser</code>, <code>magresparser</code>, <code>molcasparser</code>, <code>mopacparser</code>, <code>nwchemparser</code>, <code>oceanparser</code>, <code>octopusparser</code>, <code>onetepparser</code>, <code>openmxparser</code>, <code>orcaparser</code>, <code>psi4parser</code>, <code>qballparser</code>, <code>qboxparser</code>, <code>quantumespressoparser</code>, <code>siestaparser</code>, <code>soliddmftparser</code>, <code>tbstudioparser</code>, <code>turbomoleparser</code>, <code>vaspparser</code>, <code>w2dynamicsparser</code>, <code>wannier90parser</code>, <code>wien2kparser</code>, <code>yamboparser</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-simulation-workflow</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2022-02-19 | <strong>Last Updated:</strong> 2025-12-18
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-32" data-entry-point-types="parser">
<td><strong>nomad-parser-plugins-workflow </strong>(⭐ 5)<br><small>Parser</small></td>
<td>Collection of NOMAD parsers for workflow engines.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/workflow-parsers" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-32">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>aflowparser</code>, <code>asrparser</code>, <code>atomateparser</code>, <code>elasticparser</code>, <code>fhivibesparser</code>, <code>lobsterparser</code>, <code>phonopyparser</code>, <code>quantum_espresso_epwparser</code>, <code>quantum_espresso_phononparser</code>, <code>quantum_espresso_xspectraparser</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2022-02-19 | <strong>Last Updated:</strong> 2025-10-31
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-33" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-pwd </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A parser and schema for the Python workflow definition.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-python-workflow-definition" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-33">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Joseph Rudzinski<br>
<strong>Maintainers:</strong> Joseph Rudzinski<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-10-21 | <strong>Last Updated:</strong> 2025-12-15
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-34" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-ro-crate </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A parser for ro-crate schema plus.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-ro-crate" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-34">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Joseph Rudzinski<br>
<strong>Maintainers:</strong> Joseph Rudzinski<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-10-23 | <strong>Last Updated:</strong> 2025-10-23
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-35" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-w2dynamics </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser plugin for w2dynamics input/output files.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-w2dynamics" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-35">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Jose Pizarro<br>
<strong>Maintainers:</strong> Jose Pizarro<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code><br>
<strong>Created:</strong> 2024-08-27 | <strong>Last Updated:</strong> 2024-08-27
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-36" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-wannier90 </strong>(⭐ 2)<br><small>Parser, Schema package</small></td>
<td>A NOMAD parser plugin for Wannier90 input/output files.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-wannier90" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-parser-wannier90/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-36">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Jose M. Pizarro<br>
<strong>Maintainers:</strong> Jose M. Pizarro<br>
<strong>Entry Points:</strong> <code>nomad_parser_wannier90_plugin</code>, <code>nomad_parser_wannier90_schema</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code><br>
<strong>Created:</strong> 2024-07-04 | <strong>Last Updated:</strong> 2024-08-15
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-37" data-entry-point-types="parser|schema package">
<td><strong>nomad-parser-yambo </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A NOMAD parser plugin for YAMBO input/outputs files.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-yambo" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-parser-yambo/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-37">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Jose M. Pizarro<br>
<strong>Maintainers:</strong> Jose M. Pizarro<br>
<strong>Entry Points:</strong> <code>nomad_parser_yambo_plugin</code>, <code>nomad_parser_yambo_schema</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-simulation-workflow</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-07-02 | <strong>Last Updated:</strong> 2024-07-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-38" data-entry-point-types="app|schema package">
<td><strong>nomad-plugins </strong>(⭐ 1)<br><small>App, Schema package</small></td>
<td>A plugin for discovering other plugins.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-plugins" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-38">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Hampus Näsström<br>
<strong>Maintainers:</strong> Hampus Näsström<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code>, <code>plugin_app_entry_point</code><br>
<strong>Created:</strong> 2024-12-06 | <strong>Last Updated:</strong> 2025-11-03
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-39" data-entry-point-types="app|schema package">
<td><strong>nomad-polymerization-reactions </strong>(⭐ 2)<br><small>App, Schema package</small></td>
<td>A NOMAD plugin for polymerization reactions.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-polymerization-reactions" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-39">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Pepe Márquez, Sarthak Kapoor<br>
<strong>Maintainers:</strong> Pepe Márquez, Sarthak Kapoor<br>
<strong>Entry Points:</strong> <code>polymerization_schema</code>, <code>polymerization_app</code><br>
<strong>Created:</strong> 2024-08-07 | <strong>Last Updated:</strong> 2025-12-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-40" data-entry-point-types="app|normalizer">
<td><strong>nomad-porous-materials </strong>(⭐ 0)<br><small>App, Normalizer</small></td>
<td>NOMAD plugin for porous materials</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-porous-materials" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-40">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Lauri Himanen<br>
<strong>Maintainers:</strong> Lauri Himanen<br>
<strong>Entry Points:</strong> <code>porositynormalizer</code>, <code>mofapp</code><br>
<strong>Created:</strong> 2024-05-09 | <strong>Last Updated:</strong> 2025-04-29
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-41" data-entry-point-types="schema package">
<td><strong>nomad-schema-plugin-run </strong>(⭐ 1)<br><small>Schema package</small></td>
<td>Run schema plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-schema-plugin-run" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-schema-plugin-run/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-41">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>runschema</code><br>
<strong>Created:</strong> 2023-12-05 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-42" data-entry-point-types="schema package">
<td><strong>nomad-schema-plugin-simulation-workflow </strong>(⭐ 2)<br><small>Schema package</small></td>
<td>Simulation workflow schema plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-schema-plugin-simulation-workflow" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-schema-plugin-simulation-workflow/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-42">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-coe<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>simulationworkflowschema</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2023-11-28 | <strong>Last Updated:</strong> 2025-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-43" data-entry-point-types="app">
<td><strong>nomad-simulation-apps </strong>(⭐ 2)<br><small>App</small></td>
<td>A repository for housing NOMAD's collection of simulation app plugins.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-app-plugins-simulation" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-app-plugins-simulation/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-43">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Martin Kuban<br>
<strong>Maintainers:</strong> Martin Kuban<br>
<strong>Entry Points:</strong> <code>alexandria_app</code><br>
<strong>Created:</strong> 2025-02-24 | <strong>Last Updated:</strong> 2025-10-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-44" data-entry-point-types="example upload">
<td><strong>nomad-simulation-examples </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>Example uploads for multiple simulation codes for NOMAD development.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-simulation-examples" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-44">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Entry Points:</strong> <code>example_gromacs</code>, <code>example_lammps</code>, <code>example_orca</code>, <code>example_vasp</code><br>
<strong>Created:</strong> 2025-12-11 | <strong>Last Updated:</strong> 2025-12-16
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-45" data-entry-point-types="parser|schema package">
<td><strong>nomad-simulation-parsers </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A repository for housing NOMAD's collection of simulation parser plugins.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-plugins-simulation" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-parser-plugins-simulation/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-45">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Esma B. Boydas, Nathan Daelman, Alvin N. Ladines, Bernadette Mohr, Joseph F. Rudzinski<br>
<strong>Maintainers:</strong> Nathan Daelman, Alvin N. Ladines, Joseph F. Rudzinski<br>
<strong>Entry Points:</strong> <code>abinit_parser</code>, <code>abinit_schema_package</code>, <code>ams_parser</code>, <code>ams_schema_package</code>, <code>crystal_parser</code>, <code>crystal_schema_package</code>, <code>exciting_parser</code>, <code>exciting_schema_package</code>, <code>fhiaims_parser</code>, <code>fhiaims_schema_package</code>, <code>gpaw_parser</code>, <code>gpaw_schema_package</code>, <code>gromacs_parser</code>, <code>gromacs_schema_package</code>, <code>h5md_parser</code>, <code>h5md_schema_package</code>, <code>lammps_parser</code>, <code>octopus_parser</code>, <code>octopus_schema_package</code>, <code>phonopy_parser</code>, <code>phonopy_schema_package</code>, <code>quantumespresso_parser</code>, <code>quantumespresso_schema_package</code>, <code>vasp_parser</code>, <code>vasp_schema_package</code>, <code>wannier90_parser</code>, <code>wannier90_schema_package</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2025-01-16 | <strong>Last Updated:</strong> 2025-12-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-46" data-entry-point-types="normalizer|schema package">
<td><strong>nomad-simulation-workflow </strong>(⭐ 0)<br><small>Normalizer, Schema package</small></td>
<td>Schema defintions and normalizer for NOMAD simulation workflows</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-simulation-workflow" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-46">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Alvin Noe Ladines<br>
<strong>Maintainers:</strong> Alvin Noe Ladines<br>
<strong>Entry Points:</strong> <code>mypackage</code>, <code>mynormalizer</code><br>
<strong>Created:</strong> 2024-05-29 | <strong>Last Updated:</strong> 2024-05-29
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-47" data-entry-point-types="schema package">
<td><strong>nomad-simulations </strong>(⭐ 7)<br><small>Schema package</small></td>
<td>A NOMAD plugin for FAIR schemas for simulation data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-simulations" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-simulations/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-47">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Jose M. Pizarro, Nathan Daelman, Bernadette Mohr, Joseph F. Rudzinski<br>
<strong>Maintainers:</strong> Jose M. Pizarro, Joseph F. Rudzinski<br>
<strong>Entry Points:</strong> <code>nomad_simulations_plugin</code><br>
<strong>Created:</strong> 2024-01-17 | <strong>Last Updated:</strong> 2026-01-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-48" data-entry-point-types="app|example upload|parser|schema package">
<td><strong>nomad-tadf-molecules </strong>(⭐ 2)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>NOMAD plugin for thermally activated delayed fluorescent molecules</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-tadf-molecules" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-48">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Lauri Himanen<br>
<strong>Maintainers:</strong> Lauri Himanen<br>
<strong>Entry Points:</strong> <code>parser</code>, <code>package</code>, <code>app</code>, <code>example_upload</code><br>
<strong>Created:</strong> 2024-06-05 | <strong>Last Updated:</strong> 2025-08-06
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-49" data-entry-point-types="app|parser|schema package">
<td><strong>nomad-unisyscat </strong>(⭐ 1)<br><small>App, Parser, Schema package</small></td>
<td>A example plugin for a demonstration for UniSysCat.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-unisyscat-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-unisyscat-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-49">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Julia Schumann, Pepe Marquez, Ahmed Mansour<br>
<strong>Maintainers:</strong> Julia Schumann, Pepe Marquez<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code>, <code>myapp</code><br>
<strong>Created:</strong> 2024-05-27 | <strong>Last Updated:</strong> 2024-07-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-50" data-entry-point-types="app|example upload|normalizer|parser|schema package">
<td><strong>nomad-utility-workflows </strong>(⭐ 4)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>A module with utilities for interacting with NOMAD via, e.g., a workflow manager.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-utility-workflows" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-utility-workflows/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-50">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Joseph F. Rudzinski<br>
<strong>Maintainers:</strong> Joseph F. Rudzinski<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2024-10-14 | <strong>Last Updated:</strong> 2025-11-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-51" data-entry-point-types="normalizer|schema package">
<td><strong>nomad_topology_normalizer </strong>(⭐ 0)<br><small>Normalizer, Schema package</small></td>
<td>Topology Normalizer</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-topology-normalizer" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-51">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Amir Golparvar<br>
<strong>Maintainers:</strong> Amir Golparvar<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code>, <code>topology_normalizer_plugin</code><br>
<strong>Created:</strong> 2025-04-14 | <strong>Last Updated:</strong> 2025-10-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-52" data-entry-point-types="app|parser|schema package">
<td><strong>perovskite-solar-cell-database </strong>(⭐ 8)<br><small>App, Parser, Schema package</small></td>
<td>Perovskite solar cell data schema plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-perovskite-solar-cells-database/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-52">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Jose Marquez, Yaru Wang, Hampus Näsström<br>
<strong>Maintainers:</strong> Jose Marquez, Hampus Näsström<br>
<strong>Entry Points:</strong> <code>perovskite_solar_cell</code>, <code>perovskite_solar_cell_database_app</code>, <code>perovskite_composition</code>, <code>ion_parser</code>, <code>perovskite_ions_app</code>, <code>perovskite_tandem_cell</code>, <code>perovskite_tandem_json_parser</code>, <code>solar_cell_app</code>, <code>tandem_app</code>, <code>llm_extraction_schema</code>, <code>llm_extractor_schema</code>, <code>llm_extracted_solar_cells</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code>, <code>nomad-schema-plugin-simulation-workflow</code><br>
<strong>Created:</strong> 2023-12-05 | <strong>Last Updated:</strong> 2026-01-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-53" data-entry-point-types="app|example upload|parser|schema package">
<td><strong>pynxtools </strong>(⭐ 19)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>Extend NeXus for experiments and characterization in Materials Science and Materials Engineering and serve as a NOMAD parser implementation for NeXus.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-53">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>nexus_parser</code>, <code>nexus_schema</code>, <code>nexus_data_converter</code>, <code>nexus_app</code>, <code>simple_nexus_example</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools-igor</code>, <code>pynxtools-ellips</code>, <code>pynxtools-em</code>, <code>pynxtools-apm</code>, <code>pynxtools-mpes</code>, <code>pynxtools-spm</code>, <code>pynxtools-raman</code>, <code>pynxtools-xps</code><br>
<strong>Created:</strong> 2021-10-22 | <strong>Last Updated:</strong> 2025-11-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-54" data-entry-point-types="example upload">
<td><strong>pynxtools-apm </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>A reader for transferring APM from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-apm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-apm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-54">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>apm_example</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-03-14 | <strong>Last Updated:</strong> 2025-12-01
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-55" data-entry-point-types="example upload">
<td><strong>pynxtools-ellips </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>A reader for transferring ellipsometry data from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-ellips" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-ellips/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-55">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>ellips_example</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-05-03 | <strong>Last Updated:</strong> 2025-10-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-56" data-entry-point-types="example upload">
<td><strong>pynxtools-em </strong>(⭐ 3)<br><small>Example upload</small></td>
<td>A reader for transferring EM from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-em" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-em/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-56">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>em_example</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-03-18 | <strong>Last Updated:</strong> 2025-11-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-57" data-entry-point-types="example upload">
<td><strong>pynxtools-igor </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>pynxtools plugin for reading igor pro waves and packed experiments</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-igor" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-igor/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-57">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>igor_example</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-12-05 | <strong>Last Updated:</strong> 2025-10-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-58" data-entry-point-types="app|example upload">
<td><strong>pynxtools-mpes </strong>(⭐ 0)<br><small>App, Example upload</small></td>
<td>—</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-mpes" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-mpes/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-58">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>mpes_example</code>, <code>mpes_app</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-02-20 | <strong>Last Updated:</strong> 2025-10-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-59" data-entry-point-types="app">
<td><strong>pynxtools-raman </strong>(⭐ 0)<br><small>App</small></td>
<td>A reader for transferring Raman data from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-raman" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-raman/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-59">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>raman_app</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-06-27 | <strong>Last Updated:</strong> 2025-11-12
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-60" data-entry-point-types="app|example upload">
<td><strong>pynxtools-spm </strong>(⭐ 0)<br><small>App, Example upload</small></td>
<td>pynxtools-spm: A pynxtools plugin for SPM (Scanning Probe Microscopy) data readers</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-spm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-spm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-60">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>sts_example</code>, <code>stm_example</code>, <code>afm_example</code>, <code>spm_app</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-11-19 | <strong>Last Updated:</strong> 2025-12-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-61" data-entry-point-types="example upload">
<td><strong>pynxtools-stm </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>A plugin for pynxtools to convert sts and stm files</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-stm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-stm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-61">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>sts_example</code>, <code>stm_example</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2023-11-28 | <strong>Last Updated:</strong> 2025-10-19
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-62" data-entry-point-types="example upload">
<td><strong>pynxtools-xps </strong>(⭐ 5)<br><small>Example upload</small></td>
<td>pynxtools-xps is a pynxtools reader plugin for X-ray photoelectron spectroscopy (XPS) data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-xps" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-xps/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-62">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> The NOMAD authors<br>
<strong>Entry Points:</strong> <code>xps_example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2024-02-19 | <strong>Last Updated:</strong> 2025-12-08
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-63" data-entry-point-types="parser|schema package">
<td><strong>rtg-sims </strong>(⭐ 11)<br><small>Parser, Schema package</small></td>
<td>A plugin for RTG SIMS.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/AreaA-data_modeling_and_schemas/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-63">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Authors:</strong> Andrea Albino, Sebastian Brückner, Sarthak Kapoor, Hampus Näsström<br>
<strong>Entry Points:</strong> <code>schema</code>, <code>parser</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code>, <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2022-11-04 | <strong>Last Updated:</strong> 2025-08-05
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-64" data-entry-point-types="parser|schema package">
<td><strong>transmission </strong>(⭐ 11)<br><small>Parser, Schema package</small></td>
<td>A plugin for NOMAD containing base sections for transmission spectrophotometry.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/AreaA-data_modeling_and_schemas/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-64">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAIRmat-NFDI<br>
<strong>Entry Points:</strong> <code>transmission_schema</code>, <code>transmission_parser</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2022-11-04 | <strong>Last Updated:</strong> 2025-08-05
</p>
</div>
</details>
</td>
</tr>
</tbody>
</table>
