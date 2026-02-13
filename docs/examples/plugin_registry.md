# NOMAD Plugin Registry

This page contains information about all plugin entries currently listed in NOMAD. The information is automatically updated monthly. **Last Updated:** 2026-02-13 12:00 UTC

[Browse All Plugins in the NOMAD Plugins App](https://nomad-lab.eu/prod/v1/oasis/gui/search/plugins){:.md-button .nomad-button target="_blank" rel="noopener"}

## Available Plugins

Quick reference table of all available plugins:

<div class="plugin-registry-filter" data-plugin-registry-filter>
<label class="plugin-registry-filter__label plugin-registry-filter__label--type">Containing</label>
<select class="plugin-registry-filter__select plugin-registry-filter__type">
<option value="">All entry point types</option>
<option value="API">API</option>
<option value="App">App</option>
<option value="Example upload">Example upload</option>
<option value="Normalizer">Normalizer</option>
<option value="Parser">Parser</option>
<option value="Schema package">Schema package</option>
</select>
<label class="plugin-registry-filter__label plugin-registry-filter__label--owner">Owner</label>
<select class="plugin-registry-filter__select plugin-registry-filter__owner">
<option value="">All owners</option>
<option value="__fairmat__">FAIRmat</option>
<option value="__non_fairmat__">Non-FAIRmat</option>
<option value="AddMorePower">AddMorePower</option>
<option value="fabianli789">fabianli789</option>
<option value="IKZ-Berlin">IKZ-Berlin</option>
<option value="nomad-hzb">nomad-hzb</option>
</select>
<label class="plugin-registry-filter__label plugin-registry-filter__label--sort">Sort</label>
<select class="plugin-registry-filter__select plugin-registry-filter__sort">
<option value="name_asc">Name (A→Z)</option>
<option value="name_desc">Name (Z→A)</option>
<option value="stars_desc">Stars (high→low)</option>
</select>
<button class="plugin-registry-filter__clear" type="button">Clear</button>
<span class="plugin-registry-filter__count" aria-live="polite"></span>
</div>

<div class="plugin-registry-chart" data-plugin-registry-chart>
<p class="plugin-registry-chart__title"><strong>Filtered Distributions</strong></p>
<div class="plugin-registry-chart__panels">
<section class="plugin-registry-chart__panel" data-chart-kind="type">
<p class="plugin-registry-chart__panel-title"><strong>Containing (Type)</strong></p>
<div class="plugin-registry-chart__panel-content">
<div class="plugin-registry-chart__pie-wrap">
<div class="plugin-registry-chart__pie" role="img" aria-label="Plugin type distribution pie chart">
<span class="plugin-registry-chart__pie-total">0</span>
</div>
</div>
<div class="plugin-registry-chart__legend"></div>
</div>
</section>
<section class="plugin-registry-chart__panel" data-chart-kind="owner">
<p class="plugin-registry-chart__panel-title"><strong>Owner</strong></p>
<div class="plugin-registry-chart__panel-content">
<div class="plugin-registry-chart__pie-wrap">
<div class="plugin-registry-chart__pie" role="img" aria-label="Plugin owner distribution pie chart">
<span class="plugin-registry-chart__pie-total">0</span>
</div>
</div>
<div class="plugin-registry-chart__legend"></div>
</div>
</section>
</div>
</div>

<table class="plugin-registry-table" data-plugin-registry="true">
<thead>
<tr><th>Plugin</th><th>Description</th><th>Deployment</th><th>Links</th></tr>
</thead>
<tbody>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-0" data-entry-point-types="parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>apbs_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser for APBS</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/apbs_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-0">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-12-03 | <strong>Last Updated:</strong> 2024-12-03
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-1" data-entry-point-types="parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>battery_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>nomad parser for Meysams Battery SEI simulations</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/battery_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-1">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-11-24 | <strong>Last Updated:</strong> 2024-11-24
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-2" data-entry-point-types="app|example upload|schema package" data-owner="ka-sarthak" data-owner-group="other">
<td><strong>bayesian-optimization-hpt </strong>(⭐ 0)<br><small>App, Example upload, Schema package</small></td>
<td>A plugin to conduct BO for Hydrogen plasma treatment</td>
<td><small>—</small></td>
<td><a href="https://github.com/ka-sarthak/bayesian-optimization-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-2">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> ka-sarthak<br>
<strong>Authors:</strong> Sarthak Kapoor<br>
<strong>Maintainers:</strong> Sarthak Kapoor<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-analysis</code><br>
<strong>Created:</strong> 2024-10-17 | <strong>Last Updated:</strong> 2024-10-26
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-3" data-entry-point-types="app" data-owner="CCP-NC" data-owner-group="other">
<td><strong>ccpnc-oasis-app </strong>(⭐ 0)<br><small>App</small></td>
<td>NOMAD Oasis app for customising gui elements in the CCPNC NOMAD Oasis database.</td>
<td><small>—</small></td>
<td><a href="https://github.com/CCP-NC/ccpnc-oasis-app" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-3">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> CCP-NC<br>
<strong>Authors:</strong> Sathya Sai Seetharaman<br>
<strong>Maintainers:</strong> Sathya Sai Seetharaman<br>
<strong>Entry Points:</strong> <code>app_entry_point</code><br>
<strong>Created:</strong> 2025-09-10 | <strong>Last Updated:</strong> 2025-09-10
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-4" data-entry-point-types="parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>cg_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser for Ka Chun Chan's coarse-grained simulations</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/cg_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-4">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2024-11-27 | <strong>Last Updated:</strong> 2024-11-27
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-5" data-entry-point-types="example upload|schema package" data-owner="sd-fbk" data-owner-group="other">
<td><strong>characterization_utilities </strong>(⭐ 0)<br><small>Example upload, Schema package</small></td>
<td>Plugin to treat characterization steps and standardize them from proprietary data formats to NeXuS</td>
<td><small>—</small></td>
<td><a href="https://github.com/sd-fbk/Characterization-utilities" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-5">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> sd-fbk<br>
<strong>Authors:</strong> Matteo Bontorno<br>
<strong>Maintainers:</strong> Matteo Bontorno, Lorenza Ferrario<br>
<strong>Entry Points:</strong> <code>characterization_entry_point</code>, <code>dataconverter_entry_point</code>, <code>em_schema_package_entry_point</code>, <code>afm_schema_package_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools</code><br>
<strong>Created:</strong> 2025-10-01 | <strong>Last Updated:</strong> 2025-11-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-6" data-entry-point-types="schema package" data-owner="MPI-CPfS-Dresden" data-owner-group="other">
<td><strong>cpfs_synthesis </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>Includes ELN entries for Flux Growth, Czochalski, Bridgman, Float zone, and CVT</td>
<td><small>—</small></td>
<td><a href="https://github.com/MPI-CPfS-Dresden/nomad-cpfs-synthesis-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-6">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> MPI-CPfS-Dresden<br>
<strong>Authors:</strong> Jonathan Noky<br>
<strong>Maintainers:</strong> Jonathan Noky<br>
<strong>Entry Points:</strong> <code>schema_bridgman_entry_point</code>, <code>schema_cvt_entry_point</code>, <code>schema_czochalski_entry_point</code>, <code>schema_floatingzone_entry_point</code>, <code>schema_fluxgrowth_entry_point</code><br>
<strong>Created:</strong> 2024-10-10 | <strong>Last Updated:</strong> 2025-10-10
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-7" data-entry-point-types="schema package" data-owner="Bondoki" data-owner-group="other">
<td><strong>crc1415plugin </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>This is a schema package plugin for the CRC1415.</td>
<td><small>—</small></td>
<td><a href="https://github.com/Bondoki/NOMADOasisPlugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-7">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Bondoki<br>
<strong>Authors:</strong> Ron Dockhorn<br>
<strong>Maintainers:</strong> Ron Dockhorn<br>
<strong>Entry Points:</strong> <code>CRC1415SampleOverview</code>, <code>CRC1415MeasurementGeneric</code>, <code>CRC1415MeasurementIR</code>, <code>CRC1415MeasurementRaman</code>, <code>CRC1415MeasurementSEM</code>, <code>CRC1415MeasurementTEM</code>, <code>CRC1415MeasurementXRD</code>, <code>CRC1415MeasurementAdsorption</code>, <code>CRC1415MeasurementTGA</code><br>
<strong>Created:</strong> 2025-04-08 | <strong>Last Updated:</strong> 2025-12-19
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-8" data-entry-point-types="parser|schema package" data-owner="MaMMoS-project" data-owner-group="other">
<td><strong>cube </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>Plugin for cube files</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/MaMMoS-project/nomad-mammos-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-8">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> MaMMoS-project<br>
<strong>Authors:</strong> Martin Dobiasch<br>
<strong>Maintainers:</strong> Martin Dobiasch<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>uuparser_entry_point</code>, <code>ifwparser_entry_point</code>, <code>cube</code>, <code>tmr</code>, <code>onto</code>, <code>uu</code>, <code>ifw</code><br>
<strong>Created:</strong> 2025-03-17 | <strong>Last Updated:</strong> 2025-04-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-9" data-entry-point-types="parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>electrooptics_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser for Ka Chun Chan's electrooptics simulations</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/electrooptics_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-9">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2024-11-27 | <strong>Last Updated:</strong> 2024-11-27
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-10" data-entry-point-types="parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>electrospinning_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser for Ka Chun Chans electrospinning simulations</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/electrospinning_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-10">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-12-03 | <strong>Last Updated:</strong> 2024-12-03
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-11" data-entry-point-types="app|schema package" data-owner="Trog-404" data-owner-group="other">
<td><strong>Fabrication-facilities </strong>(⭐ 0)<br><small>App, Schema package</small></td>
<td>Plugin for fabrication processes</td>
<td><small>—</small></td>
<td><a href="https://github.com/Trog-404/Fabrication-utilities" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-11">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Trog-404<br>
<strong>Authors:</strong> Matteo Bontorno<br>
<strong>Maintainers:</strong> Matteo Bontorno<br>
<strong>Entry Points:</strong> <code>equipmentapp</code>, <code>processapp</code>, <code>stepapp</code>, <code>Items_entry_point</code>, <code>Utilities_entry_point</code>, <code>Add_entry_point</code>, <code>Transform_entry_point</code>, <code>Remove_entry_point</code>, <code>Equipments_entry_point</code>, <code>materials_entry_point</code><br>
<strong>Created:</strong> 2025-02-11 | <strong>Last Updated:</strong> 2025-07-20
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-12" data-entry-point-types="app|example upload|schema package" data-owner="Trog-404" data-owner-group="other">
<td><strong>Fabrication-utilities </strong>(⭐ 1)<br><small>App, Example upload, Schema package</small></td>
<td>Plugin for nanofabrication semiconductor cleanroom processes</td>
<td><small>—</small></td>
<td><a href="https://github.com/Trog-404/Fabrication-utilities" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-12">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Trog-404<br>
<strong>Authors:</strong> Matteo Bontorno<br>
<strong>Maintainers:</strong> Matteo Bontorno<br>
<strong>Entry Points:</strong> <code>equipmentapp</code>, <code>processapp</code>, <code>removeapp</code>, <code>addapp</code>, <code>transapp</code>, <code>materialapp</code>, <code>Items_entry_point</code>, <code>Utilities_entry_point</code>, <code>Equipments_entry_point</code>, <code>materials_entry_point</code>, <code>calculus_entry_point</code>, <code>dryetch_entry_point</code>, <code>wetetch_entry_point</code>, <code>strip_entry_point</code>, <code>drying_entry_point</code>, <code>develop_entry_point</code>, <code>cvds_entry_point</code>, <code>coating_entry_point</code>, <code>electron_gun_entry_point</code>, <code>sputtering_entry_point</code>, <code>sog_entry_point</code>, <code>bonding_entry_point</code>, <code>baking_entry_point</code>, <code>thermal_oxidation_entry_point</code>, <code>annealing_oxidation_entry_point</code>, <code>ebl_entry_point</code>, <code>fib_entry_point</code>, <code>labeling_entry_point</code>, <code>dicing_entry_point</code>, <code>process_entry_point</code><br>
<strong>Created:</strong> 2025-02-11 | <strong>Last Updated:</strong> 2025-10-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-13" data-entry-point-types="" data-owner="OpenCOMPES" data-owner-group="other">
<td><strong>fhi_sed_config </strong>(⭐ 0)<br><small>—</small></td>
<td>—</td>
<td><small>—</small></td>
<td><a href="https://github.com/OpenCOMPES/fhi_sed_config" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-13">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> OpenCOMPES<br>
<strong>Authors:</strong> Laurenz Rettig<br>
<strong>Entry Points:</strong> <code>fhi_sed_config</code><br>
<strong>Created:</strong> 2025-01-07 | <strong>Last Updated:</strong> 2025-12-05
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-14" data-entry-point-types="parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>graphene_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser for Meysam's graphene simulations</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/graphene_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-14">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-12-03 | <strong>Last Updated:</strong> 2024-12-03
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-15" data-entry-point-types="app|parser|schema package" data-owner="nomad-hzb" data-owner-group="other">
<td><strong>hzb-combinatorial-libraries </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>A schema package plugin for HZB Library Unold lab at HZB.</td>
<td><small>—</small></td>
<td><a href="https://github.com/nomad-hzb/hzb-combinatorial-libraries-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-15">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-hzb<br>
<strong>Authors:</strong> Michael Götte, Carla Terboven<br>
<strong>Maintainers:</strong> Carla Terboven, Michael Götte<br>
<strong>Entry Points:</strong> <code>hzb_library_package</code>, <code>hzb_library_parser</code>, <code>combinatorial_library_app</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code>, <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2024-03-07 | <strong>Last Updated:</strong> 2024-10-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-16" data-entry-point-types="app|normalizer|parser|schema package" data-owner="IKZ-Berlin" data-owner-group="other">
<td><strong>ikz-trpl </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>TRPL at DESY</td>
<td><small>—</small></td>
<td><a href="https://github.com/IKZ-Berlin/ikz-trpl" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-16">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IKZ-Berlin<br>
<strong>Authors:</strong> Sebastian Brueckner<br>
<strong>Maintainers:</strong> Sebastian Brueckner<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2024-10-10 | <strong>Last Updated:</strong> 2025-01-29
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-17" data-entry-point-types="parser|schema package" data-owner="IMEM-CNR-Parma" data-owner-group="other">
<td><strong>imem-nomad-plugin </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A plugin for IMEM-CNR NOMAD containing principal techniques.</td>
<td><small>—</small></td>
<td><a href="https://github.com/IMEM-CNR-Parma/IMEM-NOMAD-plugins" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-17">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IMEM-CNR-Parma<br>
<strong>Authors:</strong> Andrea Albino, Hampus Näsström, Sarthak Kapoor, Sebastian Brückner<br>
<strong>Maintainers:</strong> Andrea Albino<br>
<strong>Entry Points:</strong> <code>general_schema</code>, <code>characterization_schema</code>, <code>movpe_schema</code>, <code>movpe_growth_excel_parser</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code>, <code>nomad-material-processing</code>, <code>nomad-analysis</code><br>
<strong>Created:</strong> 2024-04-16 | <strong>Last Updated:</strong> 2025-05-06
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-18" data-entry-point-types="parser|schema package" data-owner="IKZ-Berlin" data-owner-group="other">
<td><strong>laytec_epitt_plugin </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A plugin for NOMAD containing LayTec EpiTT data model.</td>
<td><small>—</small></td>
<td><a href="https://github.com/IKZ-Berlin/laytec_epitt_nomad_plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-18">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IKZ-Berlin<br>
<strong>Authors:</strong> Sebastian Brückner, Andrea Albino, Hampus Näsström, Sarthak Kapoor<br>
<strong>Entry Points:</strong> <code>laytec_schema</code>, <code>laytec_parser</code><br>
<strong>Created:</strong> 2024-01-16 | <strong>Last Updated:</strong> 2025-01-10
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-19" data-entry-point-types="parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>lightforge_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser for lightforge</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/lightforge_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-19">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2024-11-05 | <strong>Last Updated:</strong> 2024-11-05
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-20" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="fabianli789" data-owner-group="other">
<td><strong>Lightforge_v2 </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>nomad parser for LightForge with new entry points</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianli789/LightForge_v2" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-20">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianli789<br>
<strong>Authors:</strong> Fabian Li<br>
<strong>Maintainers:</strong> Fabian Li<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-09-17 | <strong>Last Updated:</strong> 2024-11-08
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-21" data-entry-point-types="app|parser|schema package" data-owner="andreaa93" data-owner-group="other">
<td><strong>nomad-aa-plugin </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>small demo plugin</td>
<td><small>—</small></td>
<td><a href="https://github.com/andreaa93/nomad-aa-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-21">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> andreaa93<br>
<strong>Authors:</strong> Andrea Albino<br>
<strong>Maintainers:</strong> Andrea Albino<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code>, <code>parser_one_entry_point</code>, <code>parser_two_entry_point</code>, <code>parser_three_entry_point</code>, <code>parser_four_entry_point</code>, <code>parser_five_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2025-01-08 | <strong>Last Updated:</strong> 2025-09-25
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-22" data-entry-point-types="app|normalizer|parser|schema package" data-owner="exp4-age" data-owner-group="other">
<td><strong>nomad-age </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>A NOMAD plugin for the AGE.</td>
<td><small>—</small></td>
<td><a href="https://github.com/exp4-age/nomad-age" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-22">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> exp4-age<br>
<strong>Authors:</strong> Nikolai Weidt<br>
<strong>Maintainers:</strong> Nikolai Weidt<br>
<strong>Entry Points:</strong> <code>age_samples</code>, <code>age_schema_entry_point</code>, <code>lmoke_parser_entry_point</code>, <code>lmokeandvmoke_schema_entry_point</code>, <code>lmokenormalizer_entry_point</code>, <code>field_cooling_schema</code>, <code>field_cooling_parser_entry_point</code><br>
<strong>Created:</strong> 2024-12-10 | <strong>Last Updated:</strong> 2025-06-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-23" data-entry-point-types="parser|schema package" data-owner="mxwalbert" data-owner-group="other">
<td><strong>nomad-ait-echt-oasis-sputtering </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A NOMAD Oasis plugin including a schema package and parser for the magnetron sputtering system at AIT</td>
<td><small>—</small></td>
<td><a href="https://github.com/mxwalbert/ait-echt-oasis-sputtering" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-23">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> mxwalbert<br>
<strong>Authors:</strong> Maximilian Wolf<br>
<strong>Maintainers:</strong> Maximilian Wolf<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code><br>
<strong>Created:</strong> 2024-08-22 | <strong>Last Updated:</strong> 2024-08-22
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-24" data-entry-point-types="app|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-aitoolkit </strong>(⭐ 0)<br><small>App, Schema package</small></td>
<td>Schema and app for AI Toolkit notebooks.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-aitoolkit" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-aitoolkit/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-24">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-25" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-analysis </strong>(⭐ 2)<br><small>Schema package</small></td>
<td>A NOMAD plugin for analysis of FAIR data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-analysis" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-analysis/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-25">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-26" data-entry-point-types="app|example upload|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-auto-xrd </strong>(⭐ 1)<br><small>App, Example upload, Schema package</small></td>
<td>A NOMAD plugin containing schemas for automatic XRD analysis.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-auto-xrd" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-26">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-27" data-entry-point-types="" data-owner="nomad-hzb" data-owner-group="other">
<td><strong>nomad-baseclasses </strong>(⭐ 6)<br><small>—</small></td>
<td>A schema package plugin for chemical energy at hzb.</td>
<td><small>—</small></td>
<td><a href="https://github.com/nomad-hzb/nomad-baseclasses" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-hzb.github.io/nomad-baseclasses/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-27">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-hzb<br>
<strong>Authors:</strong> Michael Götte, Carla Terboven<br>
<strong>Maintainers:</strong> Carla Terboven, Michael Götte<br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-simulation-workflow</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2023-06-26 | <strong>Last Updated:</strong> 2025-12-15
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-28" data-entry-point-types="app|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-battery-database </strong>(⭐ 1)<br><small>App, Parser, Schema package</small></td>
<td>app for battery database</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-battery-database" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-battery-database/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-28">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-29" data-entry-point-types="app|example upload|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-bayesian-optimization </strong>(⭐ 1)<br><small>App, Example upload, Schema package</small></td>
<td>NOMAD plugin for driving experiments/simulations using bayesian optimization</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-bayesian-optimization" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-29">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-30" data-entry-point-types="app|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-camels-plugin </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>Parser for HDF5 files coming from NOMAD CAMELS.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-camels-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-camels-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-30">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-31" data-entry-point-types="app|example upload|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-catalysis </strong>(⭐ 4)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>A NOMAD plugin for heterogeneous catalysis data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-catalysis-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-catalysis-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-31">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-32" data-entry-point-types="example upload|normalizer|parser|schema package" data-owner="CAU-Kiel" data-owner-group="other">
<td><strong>nomad-cau-plugin </strong>(⭐ 0)<br><small>Example upload, Normalizer, Parser, Schema package</small></td>
<td>nomad plugin for CAU Kiel</td>
<td><small>—</small></td>
<td><a href="https://github.com/CAU-Kiel/nomad-cau-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-32">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> CAU-Kiel<br>
<strong>Authors:</strong> Stepanka Lankova<br>
<strong>Maintainers:</strong> Stepanka Lankova<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>MRO005_schema</code>, <code>MRO004_schema</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-05-16 | <strong>Last Updated:</strong> 2025-12-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-33" data-entry-point-types="app|parser|schema package" data-owner="nomad-hzb" data-owner-group="other">
<td><strong>nomad-chemical-energy </strong>(⭐ 3)<br><small>App, Parser, Schema package</small></td>
<td>A schema package plugin for chemical energy at hzb.</td>
<td><small>—</small></td>
<td><a href="https://github.com/nomad-hzb/nomad-chemical-energy" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-33">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-hzb<br>
<strong>Authors:</strong> Michael Götte, Carla Terboven<br>
<strong>Maintainers:</strong> Carla Terboven, Michael Götte<br>
<strong>Entry Points:</strong> <code>ce_amcc_package</code>, <code>ce_nome_package</code>, <code>ce_necc_package</code>, <code>ce_nesd_package</code>, <code>ce_nsli_package</code>, <code>ce_wannsee_package</code>, <code>hzb_characterization_package</code>, <code>hzb_catlab_package</code>, <code>dlr_ec_package</code>, <code>hzb_general_process_package</code>, <code>tfc_package</code>, <code>hzb_catlab_parser</code>, <code>ce_amcc_biologic_parser</code>, <code>ce_nesd_biologic_parser</code>, <code>ce_nesd_zahner_parser</code>, <code>ce_nesd_chi_parser</code>, <code>ce_nesd_labview_parser</code>, <code>ce_nesd_palmsens_parser</code>, <code>ce_nesd_metadata_parser</code>, <code>ce_necc_xlsx_parser</code>, <code>ce_necc_biologic_parser</code>, <code>ce_nome_gamry_parser</code>, <code>kmc3_biologic_parser</code>, <code>ce_nome_csv_parser</code>, <code>ce_nome_uvvis_parser</code>, <code>ce_nome_tif_parser</code>, <code>ce_nome_massspectrometry_parser</code>, <code>ce_wannsee_cor_parser</code>, <code>ce_wannsee_xrd_xy_parser</code>, <code>dlr_ec_cv_parser</code>, <code>dlr_ec_cp_parser</code>, <code>dlr_ec_eis_parser</code>, <code>hzb_general_process_parser</code>, <code>tfc_sputtering_parser</code>, <code>tfc_xrf_parser</code>, <code>tfc_xrd_parser</code>, <code>kmc2_xas_parser</code>, <code>kmc3_xas_parser_before2021</code>, <code>kmc3_xas_parser</code>, <code>ce_nome_general_parser</code>, <code>necc_find_app</code>, <code>necc_compare_app</code>, <code>voila_finder_app</code>, <code>nome_sample_app</code>, <code>nome_oer_cp_analysis_app</code>, <code>nesd_oer_app</code>, <code>amcc_reproducibility_app</code>, <code>catlab_combinatorial_library_app</code>, <code>catlab_pixel_app</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code>, <code>nomad-measurements</code>, <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2023-06-26 | <strong>Last Updated:</strong> 2025-11-24
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-34" data-entry-point-types="app|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-countries </strong>(⭐ 100)<br><small>App, Parser, Schema package</small></td>
<td>Countries of the world plugin</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-34">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-35" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-crystallm </strong>(⭐ 1)<br><small>Schema package</small></td>
<td>A NOMAD plugin for running CrystaLLM inference in NOMAD installations.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-crystallm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-crystallm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-35">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-36" data-entry-point-types="parser|schema package" data-owner="AddMorePower" data-owner-group="other">
<td><strong>nomad-DAMASK_parser </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A parser plugin for the DAMASK output files</td>
<td><small>—</small></td>
<td><a href="https://github.com/AddMorePower/nomad-DAMASK_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-36">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> AddMorePower<br>
<strong>Authors:</strong> Guillaume Gaisné<br>
<strong>Maintainers:</strong> Guillaume Gaisné<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code><br>
<strong>Created:</strong> 2024-08-01 | <strong>Last Updated:</strong> 2025-08-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-37" data-entry-point-types="normalizer|schema package" data-owner="lauri-codes" data-owner-group="other">
<td><strong>nomad-demo-plugin </strong>(⭐ 0)<br><small>Normalizer, Schema package</small></td>
<td>NOMAD demo plugin</td>
<td><small>—</small></td>
<td><a href="https://github.com/lauri-codes/nomad-demo-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-37">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> lauri-codes<br>
<strong>Authors:</strong> Lauri Himanen<br>
<strong>Maintainers:</strong> Lauri Himanen<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code><br>
<strong>Created:</strong> 2025-08-21 | <strong>Last Updated:</strong> 2025-08-21
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-38" data-entry-point-types="app|parser|schema package" data-owner="DTU-Nanolab-materials-discovery" data-owner-group="other">
<td><strong>nomad-dtu-nanolab-plugin </strong>(⭐ 3)<br><small>App, Parser, Schema package</small></td>
<td>A plugin for the schemas, parsers,</td>
<td><small>—</small></td>
<td><a href="https://github.com/DTU-Nanolab-materials-discovery/nomad-dtu-nanolab-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://dtu-nanolab-materials-discovery.github.io/nomad-dtu-nanolab-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-38">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> DTU-Nanolab-materials-discovery<br>
<strong>Authors:</strong> Lena Mittman<br>
<strong>Maintainers:</strong> Lena Mittman<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>sputtering_targets_app</code>, <code>sputering_app</code>, <code>xrd_app</code>, <code>edx_app</code>, <code>analysis_app</code>, <code>samples_app</code>, <code>sputtering</code>, <code>thermal</code>, <code>rtp</code>, <code>gas</code>, <code>instrument</code>, <code>target</code>, <code>substrate</code>, <code>edx</code>, <code>xrd</code>, <code>xps</code>, <code>ellipsometry</code>, <code>rt</code>, <code>pl</code>, <code>raman</code>, <code>sample</code>, <code>basesections</code>, <code>analysis</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code>, <code>nomad-material-processing</code>, <code>nomad-analysis</code><br>
<strong>Created:</strong> 2024-05-23 | <strong>Last Updated:</strong> 2025-12-12
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-39" data-entry-point-types="parser|schema package" data-owner="AddMorePower" data-owner-group="other">
<td><strong>nomad-ECCI_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A NOMAD parser plugin for ECCI measurements in AddMorePower</td>
<td><small>—</small></td>
<td><a href="https://github.com/AddMorePower/nomad-ECCI_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-39">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> AddMorePower<br>
<strong>Authors:</strong> Guillaume Gaisné<br>
<strong>Maintainers:</strong> Guillaume Gaisné<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-01-30 | <strong>Last Updated:</strong> 2025-08-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-40" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-eos-workflows </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>A NOMAD plugin containing the section definitions of a standard Equation of State (EoS) workflow.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-schema-plugin-eos-workflows" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-40">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-41" data-entry-point-types="example upload|schema package" data-owner="ka-sarthak" data-owner-group="other">
<td><strong>nomad-example </strong>(⭐ 0)<br><small>Example upload, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/ka-sarthak/nomad-example" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-41">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> ka-sarthak<br>
<strong>Authors:</strong> Sarthak Kapoor<br>
<strong>Maintainers:</strong> Sarthak Kapoor<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code>, <code>myaction</code><br>
<strong>Created:</strong> 2025-07-25 | <strong>Last Updated:</strong> 2025-08-19
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-42" data-entry-point-types="example upload|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-external-eln-integrations </strong>(⭐ 0)<br><small>Example upload, Parser, Schema package</small></td>
<td>3rd Party Integration packages</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-external-eln-integrations" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-42">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-43" data-entry-point-types="app|normalizer|parser|schema package" data-owner="blueraft" data-owner-group="other">
<td><strong>nomad-foobar </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/blueraft/foobar" target="_blank" rel="noopener">Code</a> | <a href="https://blueraft.github.io/foobar/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-43">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> blueraft<br>
<strong>Authors:</strong> John Doe<br>
<strong>Maintainers:</strong> John Doe<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code>, <code>mynormalizer</code>, <code>myapp</code><br>
<strong>Created:</strong> 2024-06-04 | <strong>Last Updated:</strong> 2024-06-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-44" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="mcasademont9" data-owner-group="other">
<td><strong>nomad-forematics </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>NOMAD plugin for forematics experiments</td>
<td><small>—</small></td>
<td><a href="https://github.com/mcasademont9/nomad-forematics" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-44">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> mcasademont9<br>
<strong>Authors:</strong> Miquel Casademont<br>
<strong>Maintainers:</strong> Miquel Casademont<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>substrate</code>, <code>solution</code>, <code>experiment</code>, <code>processing</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-03-25 | <strong>Last Updated:</strong> 2025-09-03
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-45" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-gallery </strong>(⭐ 1)<br><small>Schema package</small></td>
<td>A mkdocs-based GitHub Pages site for showcasing NOMAD features, examples, and use cases.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-gallery" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-gallery/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-45">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-46" data-entry-point-types="parser|schema package" data-owner="ZBT-Tools" data-owner-group="other">
<td><strong>nomad-greenlight-plugin </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD plugin for greenlight fuel cell test benches</td>
<td><small>—</small></td>
<td><a href="https://github.com/ZBT-Tools/nomad-greenlight-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-46">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> ZBT-Tools<br>
<strong>Authors:</strong> Lukas Feierabend<br>
<strong>Maintainers:</strong> Lukas Feierabend<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2024-11-28 | <strong>Last Updated:</strong> 2025-07-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-47" data-entry-point-types="schema package" data-owner="nomad-hzb" data-owner-group="other">
<td><strong>nomad-hiern </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>A schema package plugin for HIERN.</td>
<td><small>—</small></td>
<td><a href="https://github.com/nomad-hzb/nomad-hiern" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-47">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-hzb<br>
<strong>Authors:</strong> Michael Götte<br>
<strong>Maintainers:</strong> Michael Götte<br>
<strong>Entry Points:</strong> <code>hiern_package</code><br>
<strong>Created:</strong> 2024-07-29 | <strong>Last Updated:</strong> 2025-11-03
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-48" data-entry-point-types="app|parser|schema package" data-owner="nomad-hzb" data-owner-group="other">
<td><strong>nomad-hysprint </strong>(⭐ 5)<br><small>App, Parser, Schema package</small></td>
<td>A schema package plugin for hysprint lab at hzb.</td>
<td><small>—</small></td>
<td><a href="https://github.com/nomad-hzb/nomad-hysprint" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-hzb.github.io/nomad-hysprint/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-48">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-hzb<br>
<strong>Authors:</strong> Michael Götte, Carla Terboven<br>
<strong>Maintainers:</strong> Carla Terboven, Michael Götte<br>
<strong>Entry Points:</strong> <code>hysprint_package</code>, <code>solai_package</code>, <code>hysprint_parser</code>, <code>solartab_sim_parser</code>, <code>solartab_package</code>, <code>hysprint_experiment_parser</code>, <code>ink_recycling_package</code>, <code>hysprint_voila_app</code>, <code>absolute_pl_app</code>, <code>solar_cell_overview_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code>, <code>nomad-luqy-plugin</code>, <code>nomad-measurements</code>, <code>pynxtools-xps</code><br>
<strong>Created:</strong> 2023-06-26 | <strong>Last Updated:</strong> 2025-11-27
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-49" data-entry-point-types="app|normalizer|schema package" data-owner="IKZ-Berlin" data-owner-group="other">
<td><strong>nomad-ikz-fz </strong>(⭐ 0)<br><small>App, Normalizer, Schema package</small></td>
<td>NOMAD plugin for Fz data used at IKZ Berlin</td>
<td><small>—</small></td>
<td><a href="https://github.com/IKZ-Berlin/ikz-fz-nomad-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-49">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IKZ-Berlin<br>
<strong>Authors:</strong> Sebastian Brueckner<br>
<strong>Maintainers:</strong> Sebastian Brueckner<br>
<strong>Entry Points:</strong> <code>mypackage</code>, <code>mynormalizer</code>, <code>myapp</code>, <code>fzcrysapp</code>, <code>fzinstrumentapp</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2024-05-23 | <strong>Last Updated:</strong> 2025-03-24
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-50" data-entry-point-types="app|parser|schema package" data-owner="IKZ-Berlin" data-owner-group="other">
<td><strong>nomad-ikz-plugin </strong>(⭐ 2)<br><small>App, Parser, Schema package</small></td>
<td>A plugin for NOMAD containing IKZ use cases.</td>
<td><small>—</small></td>
<td><a href="https://github.com/IKZ-Berlin/nomad-ikz-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-50">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IKZ-Berlin<br>
<strong>Authors:</strong> Hampus Näsström, Andrea Albino, Sarthak Kapoor, Sebastian Brückner<br>
<strong>Entry Points:</strong> <code>general_schema</code>, <code>characterization_schema</code>, <code>characterization_transmission_parser</code>, <code>deprecated_characterization_schema</code>, <code>pld_schema</code>, <code>movpe_schema</code>, <code>movpe2_growth_excel</code>, <code>movpe1_growth_excel</code>, <code>movpe1_old_growth_excel</code>, <code>movpe1_rcp_parser</code>, <code>substrate_excel_parser</code>, <code>mbe_schema</code>, <code>czochralski_schema</code>, <code>czochralski_multilog_parser</code>, <code>movpe_substrate_app</code>, <code>movpe_growth_run_app</code>, <code>movpe_layers_app</code>, <code>pld_app</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code>, <code>laytec_epitt_plugin</code>, <code>nomad-material-processing</code>, <code>nomad-analysis</code><br>
<strong>Created:</strong> 2024-09-24 | <strong>Last Updated:</strong> 2025-11-28
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-51" data-entry-point-types="schema package" data-owner="IKZ-Berlin" data-owner-group="other">
<td><strong>nomad-ikz-sem </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>SEM plugin</td>
<td><small>—</small></td>
<td><a href="https://github.com/IKZ-Berlin/ikz-sem" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-51">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IKZ-Berlin<br>
<strong>Authors:</strong> Sebastian Brueckner<br>
<strong>Maintainers:</strong> Sebastian Brueckner<br>
<strong>Entry Points:</strong> <code>semsupport</code><br>
<strong>Created:</strong> 2024-07-04 | <strong>Last Updated:</strong> 2025-01-20
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-52" data-entry-point-types="parser|schema package" data-owner="IKZ-Berlin" data-owner-group="other">
<td><strong>nomad-ikz_omega_theta_xrd </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD plugin for Omega Theta XRD Measurements</td>
<td><small>—</small></td>
<td><a href="https://github.com/IKZ-Berlin/ikz-omega-theta-xrd" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-52">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IKZ-Berlin<br>
<strong>Authors:</strong> Sebastian Brueckner<br>
<strong>Maintainers:</strong> Sebastian Brueckner<br>
<strong>Entry Points:</strong> <code>omegascan</code>, <code>omegathetaxrdparser</code><br>
<strong>Created:</strong> 2024-06-24 | <strong>Last Updated:</strong> 2025-01-29
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-53" data-entry-point-types="parser|schema package" data-owner="IKZ-Berlin" data-owner-group="other">
<td><strong>nomad-ikz_raman </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD plugin for Raman data from a Horiba LabRAM instrument</td>
<td><small>—</small></td>
<td><a href="https://github.com/IKZ-Berlin/IKZ_raman" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-53">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> IKZ-Berlin<br>
<strong>Authors:</strong> Sebastian Brückner<br>
<strong>Maintainers:</strong> Sebastian Brückner<br>
<strong>Entry Points:</strong> <code>ramanparser</code>, <code>raman</code><br>
<strong>Created:</strong> 2024-06-13 | <strong>Last Updated:</strong> 2025-01-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-54" data-entry-point-types="parser|schema package" data-owner="GarzonDiegoFEUP" data-owner-group="other">
<td><strong>nomad-inl-base </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A plugin to manage the data from LaNaSC</td>
<td><small>—</small></td>
<td><a href="https://github.com/GarzonDiegoFEUP/nomad-inl-base" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-54">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> GarzonDiegoFEUP<br>
<strong>Authors:</strong> Diego Garzon<br>
<strong>Maintainers:</strong> Diego Garzon<br>
<strong>Entry Points:</strong> <code>CVarser_entry_point</code>, <code>EDparser_entry_point1</code>, <code>schema_package_entry_point</code>, <code>cyclic_voltammetry_entry_point</code>, <code>star_entry_point</code>, <code>crystaLLM_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2024-09-24 | <strong>Last Updated:</strong> 2025-06-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-55" data-entry-point-types="schema package" data-owner="MPI-CPfS-Dresden" data-owner-group="other">
<td><strong>nomad-labfolder-plugin </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>Can import LabFolder entries into the NOMAD ELN when provided with a mapping file</td>
<td><small>—</small></td>
<td><a href="https://github.com/MPI-CPfS-Dresden/nomad-labfolder-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-55">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> MPI-CPfS-Dresden<br>
<strong>Authors:</strong> Jonathan Noky<br>
<strong>Maintainers:</strong> Jonathan Noky<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2024-10-10 | <strong>Last Updated:</strong> 2025-03-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-56" data-entry-point-types="schema package" data-owner="FAU-LAP" data-owner-group="other">
<td><strong>nomad-lap-schema </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>Provides the schemas used at LAP</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAU-LAP/nomad-lap-schema" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-56">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> FAU-LAP<br>
<strong>Authors:</strong> Johannes Lehmeyer<br>
<strong>Maintainers:</strong> Johannes Lehmeyer<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-03-24 | <strong>Last Updated:</strong> 2025-12-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-57" data-entry-point-types="app|schema package" data-owner="kaikoebnick" data-owner-group="other">
<td><strong>nomad-laserphysics </strong>(⭐ 0)<br><small>App, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/kaikoebnick/nomad-laserphysics" target="_blank" rel="noopener">Code</a> | <a href="https://kaikoebnick.github.io/nomad-laserphysics/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-57">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> kaikoebnick<br>
<strong>Authors:</strong> Kai Koebnick<br>
<strong>Maintainers:</strong> Kai Koebnick<br>
<strong>Entry Points:</strong> <code>measurements_app_entry_point</code>, <code>evaluations_app_entry_point</code>, <code>objects_app_entry_point</code>, <code>evaluation_schema_package_entry_point</code>, <code>ML_evaluation_schema_package_entry_point</code>, <code>ML_evaluation_procedure_schema_package_entry_point</code>, <code>measurement_schema_package_entry_point</code>, <code>FIM_test_chamber_schema_package_entry_point</code>, <code>FEM_correlation_chamber_schema_package_entry_point</code>, <code>object_schema_package_entry_point</code>, <code>tip_sample_schema_package_entry_point</code><br>
<strong>Created:</strong> 2024-09-24 | <strong>Last Updated:</strong> 2025-03-10
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-58" data-entry-point-types="app|example upload|parser|schema package" data-owner="Pepe-Marquez" data-owner-group="other">
<td><strong>nomad-luqy-plugin </strong>(⭐ 0)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>A plugin to manage LuQY Pro measurement data</td>
<td><small>—</small></td>
<td><a href="https://github.com/Pepe-Marquez/nomad-luqy-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-58">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Pepe-Marquez<br>
<strong>Authors:</strong> Pepe Márquez<br>
<strong>Maintainers:</strong> Pepe Márquez<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code><br>
<strong>Created:</strong> 2025-01-28 | <strong>Last Updated:</strong> 2025-07-08
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-59" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-material-processing </strong>(⭐ 11)<br><small>Schema package</small></td>
<td>A plugin for NOMAD containing base sections for material processing.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-material-processing" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-material-processing/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-59">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-60" data-entry-point-types="app|example upload|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-material-processing-example </strong>(⭐ 2)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>An example plugin to demonstrate the use of schemas from the nomad-material-processing plugin.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-material-processing-example" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-60">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-61" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-measurements </strong>(⭐ 14)<br><small>Parser, Schema package</small></td>
<td>A plugin for NOMAD containing base sections for measurements.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-measurements" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-measurements/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-61">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-62" data-entry-point-types="example upload|parser|schema package" data-owner="hampusnasstrom" data-owner-group="other">
<td><strong>nomad-migration-example </strong>(⭐ 0)<br><small>Example upload, Parser, Schema package</small></td>
<td>An example plugin showing how a parser can be used to migrate from one version of an ELN schema to the next</td>
<td><small>—</small></td>
<td><a href="https://github.com/hampusnasstrom/nomad-migration-example" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-62">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> hampusnasstrom<br>
<strong>Authors:</strong> Hampus Näsström<br>
<strong>Maintainers:</strong> Hampus Näsström<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-06-04 | <strong>Last Updated:</strong> 2025-06-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-63" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-neb-workflows </strong>(⭐ 4)<br><small>Schema package</small></td>
<td>A NOMAD plugin containing the section definitions of a standard Nudged Elastic Band (NEB) workflow.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-neb-workflows" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-neb-workflows/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-63">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-64" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-nmr-schema </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>Schema plugin containing shared classes for NMR metadata</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-schema-plugin-nmr" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-64">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-65" data-entry-point-types="app|normalizer|schema package" data-owner="budschi" data-owner-group="other">
<td><strong>nomad-nomadtestapp </strong>(⭐ 0)<br><small>App, Normalizer, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/budschi/testnomadapp" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-65">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> budschi<br>
<strong>Authors:</strong> Sebastian Brueckner<br>
<strong>Maintainers:</strong> Sebastian Brueckner<br>
<strong>Entry Points:</strong> <code>mypackage</code>, <code>mynormalizer</code>, <code>myapp</code><br>
<strong>Created:</strong> 2024-05-16 | <strong>Last Updated:</strong> 2024-05-16
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-66" data-entry-point-types="normalizer" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-normalizer-plugin-bandstructure </strong>(⭐ 1)<br><small>Normalizer</small></td>
<td>Band structure normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-bandstructure" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-bandstructure/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-66">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-67" data-entry-point-types="normalizer" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-normalizer-plugin-dos </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>DOS normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-dos" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-dos/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-67">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-68" data-entry-point-types="normalizer" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-normalizer-plugin-simulation-workflow </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>Simulation workflow nomad plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-simulation-workflow" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-simulation-workflow/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-68">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-69" data-entry-point-types="normalizer" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-normalizer-plugin-soap </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>SOAP nomad plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-soap" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-69">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-70" data-entry-point-types="normalizer" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-normalizer-plugin-spectra </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>Spectra normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-spectra" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-spectra/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-70">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-71" data-entry-point-types="normalizer" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-normalizer-plugin-system </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>System normalizer plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-normalizer-plugin-system" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-normalizer-plugin-system/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-71">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-72" data-entry-point-types="app|parser|schema package" data-owner="fliaght" data-owner-group="other">
<td><strong>nomad-novelMOF </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>a novel MOF database</td>
<td><small>—</small></td>
<td><a href="https://github.com/fliaght/nomad-novelMOF" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-72">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fliaght<br>
<strong>Authors:</strong> Yi luo<br>
<strong>Maintainers:</strong> Yi luo<br>
<strong>Entry Points:</strong> <code>novel_mof_parser_entry_point</code>, <code>novel_mof_schema</code>, <code>novel_mof_app_entry_point</code><br>
<strong>Created:</strong> 2025-06-30 | <strong>Last Updated:</strong> 2025-07-10
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-73" data-entry-point-types="schema package" data-owner="CCP-NC" data-owner-group="other">
<td><strong>nomad-oasis-schema-parser-plugin </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>Specialised magres parser + custom schema package for the CCP-NC NOMAD Oasis.</td>
<td><small>—</small></td>
<td><a href="https://github.com/CCP-NC/nomad-oasis-schema-parser-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-73">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> CCP-NC<br>
<strong>Authors:</strong> Sathya Sai Seetharaman<br>
<strong>Maintainers:</strong> Sathya Sai Seetharaman<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-08-19 | <strong>Last Updated:</strong> 2025-08-19
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-74" data-entry-point-types="parser|schema package" data-owner="JosePizarro3" data-owner-group="other">
<td><strong>nomad-parser-dmft </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A compilation of NOMAD parsers for input/output files of DMFT codes.</td>
<td><small>—</small></td>
<td><a href="https://github.com/JosePizarro3/nomad-parser-dmft" target="_blank" rel="noopener">Code</a> | <a href="https://josepizarro3.github.io/nomad-parser-dmft/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-74">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> JosePizarro3<br>
<strong>Authors:</strong> Jose Pizarro<br>
<strong>Maintainers:</strong> Jose Pizarro<br>
<strong>Entry Points:</strong> <code>edmft_parser_entry_point</code>, <code>soliddmft_parser_entry_point</code>, <code>w2dynamics_parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code>, <code>nomad-schema-plugin-simulation-workflow</code>, <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2024-09-11 | <strong>Last Updated:</strong> 2024-09-12
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-75" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-edmft </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-edmft" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-75">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-76" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-fhiaims </strong>(⭐ 2)<br><small>Parser, Schema package</small></td>
<td>Standalone NOMAD plugin for parsing FHI-aims calculation files</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-fhiaims" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-76">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-77" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-gsd </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>Parser for trajectory files in GSD format (<https://gsd.readthedocs.io/en/v3.3.1/).></td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-gsd" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-77">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-78" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-h5md </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser plugin for h5md-based simulation files.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-h5md" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-78">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-79" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-molpro </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-molpro" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-79">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-80" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-orca </strong>(⭐ 2)<br><small>Parser, Schema package</small></td>
<td>nomad plugin for ORCA calculations</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-orca" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-80">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-81" data-entry-point-types="parser" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-plugin-boss </strong>(⭐ 1)<br><small>Parser</small></td>
<td>Plugin for parsing and displaying BOSS PES arftifacts</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-plugin-boss" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-81">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-82" data-entry-point-types="parser" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-parser-plugins-atomistic </strong>(⭐ 7)<br><small>Parser</small></td>
<td>Collection of NOMAD parsers for atomistic codes.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/atomistic-parsers" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-82">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-83" data-entry-point-types="parser" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-parser-plugins-electronic </strong>(⭐ 23)<br><small>Parser</small></td>
<td>Collection of NOMAD parsers for electronic structure codes.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/electronic-parsers" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-83">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-84" data-entry-point-types="parser" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-parser-plugins-workflow </strong>(⭐ 5)<br><small>Parser</small></td>
<td>Collection of NOMAD parsers for workflow engines.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/workflow-parsers" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-84">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-85" data-entry-point-types="parser|schema package" data-owner="aouinaayoub" data-owner-group="other">
<td><strong>nomad-parser-pwafqmc </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A parser for PWAFQMC code</td>
<td><small>—</small></td>
<td><a href="https://github.com/aouinaayoub/nomad-parser-pwafqmc" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-85">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> aouinaayoub<br>
<strong>Authors:</strong> Ayoub Aouina<br>
<strong>Maintainers:</strong> Ayoub Aouina<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code><br>
<strong>Created:</strong> 2024-09-05 | <strong>Last Updated:</strong> 2024-12-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-86" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-pwd </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A parser and schema for the Python workflow definition.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-python-workflow-definition" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-86">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-87" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-ro-crate </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>A parser for ro-crate schema plus.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-ro-crate" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-87">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-88" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-w2dynamics </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser plugin for w2dynamics input/output files.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-w2dynamics" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-88">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-89" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-wannier90 </strong>(⭐ 2)<br><small>Parser, Schema package</small></td>
<td>A NOMAD parser plugin for Wannier90 input/output files.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-wannier90" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-parser-wannier90/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-89">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-90" data-entry-point-types="parser|schema package" data-owner="caraortizmah" data-owner-group="other">
<td><strong>nomad-parser-xas </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser plugin for XAS simulations output in text file.</td>
<td><small>—</small></td>
<td><a href="https://github.com/caraortizmah/XAS_alldata" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-90">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> caraortizmah<br>
<strong>Authors:</strong> Carlos Mahecha<br>
<strong>Maintainers:</strong> Carlos Mahecha<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-simulations</code><br>
<strong>Created:</strong> 2024-09-05 | <strong>Last Updated:</strong> 2024-09-06
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-91" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-parser-yambo </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A NOMAD parser plugin for YAMBO input/outputs files.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-yambo" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-parser-yambo/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-91">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-92" data-entry-point-types="parser|schema package" data-owner="magr4826" data-owner-group="other">
<td><strong>nomad-parser-yambospectra </strong>(⭐ 2)<br><small>Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/magr4826/nomad-parser-yambospectra" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-92">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> magr4826<br>
<strong>Authors:</strong> Malte Grunert<br>
<strong>Maintainers:</strong> Malte Grunert<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2024-09-05 | <strong>Last Updated:</strong> 2024-09-08
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-93" data-entry-point-types="app|example upload|parser|schema package" data-owner="AG-SEK" data-owner-group="other">
<td><strong>nomad-perolab-umr </strong>(⭐ 0)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>Plugin for NOMAD Oasis at PeroLab Marburg</td>
<td><small>—</small></td>
<td><a href="https://github.com/AG-SEK/nomad-perolab-umr-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-93">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> AG-SEK<br>
<strong>Authors:</strong> Aaron Schüller-Ruhl<br>
<strong>Maintainers:</strong> Aaron Schüller-Ruhl<br>
<strong>Entry Points:</strong> <code>batch_schema</code>, <code>solar_cell_schema</code>, <code>substrate_schema</code>, <code>external_batch_plan_schema</code>, <code>internal_batch_plan_schema</code>, <code>baseclasses_schema</code>, <code>synthesis_schema</code>, <code>voila_schema</code>, <code>blade_coating_schema</code>, <code>cleaning_coating_schema</code>, <code>spin_coating_schema</code>, <code>spray_pyrolysis_schema</code>, <code>evaporation_schema</code>, <code>connection_test_schema</code>, <code>eqe_schema</code>, <code>jv_schema</code>, <code>mpp_tracking_schema</code>, <code>stability_test_schema</code>, <code>myparser</code>, <code>cicci_txt_parser_entry_point</code>, <code>chemicals_app_entry_point</code>, <code>voila_app_entry_point</code>, <code>example_upload_entry_point</code>, <code>voila_scripts_entry_point</code><br>
<strong>Created:</strong> 2024-09-27 | <strong>Last Updated:</strong> 2025-08-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-94" data-entry-point-types="app|parser|schema package" data-owner="nomad-hzb" data-owner-group="other">
<td><strong>nomad-perotf </strong>(⭐ 2)<br><small>App, Parser, Schema package</small></td>
<td>A schema package plugin for perotf at KIT.</td>
<td><small>—</small></td>
<td><a href="https://github.com/nomad-hzb/nomad-perotf" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-94">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-hzb<br>
<strong>Authors:</strong> Michael Götte, Felix Laufer<br>
<strong>Maintainers:</strong> Felix Laufer, Michael Götte<br>
<strong>Entry Points:</strong> <code>perotf_package</code>, <code>perotf_parser</code>, <code>perotf_experiment_parser</code>, <code>perotf_voila_app</code>, <code>solar_cell_overview_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code>, <code>nomad-luqy-plugin</code>, <code>nomad-measurements</code><br>
<strong>Created:</strong> 2023-08-02 | <strong>Last Updated:</strong> 2025-12-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-95" data-entry-point-types="app|parser|schema package" data-owner="andreaa93" data-owner-group="other">
<td><strong>nomad-plugin-aatest </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/andreaa93/nomad-plugin-aatest" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-95">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> andreaa93<br>
<strong>Authors:</strong> Andrea Albino<br>
<strong>Maintainers:</strong> Andrea Albino<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2025-01-15 | <strong>Last Updated:</strong> 2025-01-15
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-96" data-entry-point-types="api|app|example upload|schema package" data-owner="Bondoki" data-owner-group="other">
<td><strong>nomad-plugin-gui </strong>(⭐ 0)<br><small>API, App, Example upload, Schema package</small></td>
<td>The NOMAD plugin for the new NOMAD GUI.</td>
<td><small>—</small></td>
<td><a href="https://github.com/Bondoki/nomad-gui-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-96">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Bondoki<br>
<strong>Authors:</strong> NOMAD Laboratory<br>
<strong>Entry Points:</strong> <code>gui_api</code>, <code>app_api</code>, <code>demo_schema</code>, <code>values_test_schema</code>, <code>excercise_schema</code>, <code>ui_demonstration_example_upload</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-schema-plugin-run</code><br>
<strong>Created:</strong> 2025-06-12 | <strong>Last Updated:</strong> 2025-06-12
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-97" data-entry-point-types="app|parser|schema package" data-owner="leonardomusini" data-owner-group="other">
<td><strong>nomad-plugin-mbe </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>Plugin for MBE sample growths</td>
<td><small>—</small></td>
<td><a href="https://github.com/leonardomusini/nomad-plugin-mbe" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-97">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> leonardomusini<br>
<strong>Authors:</strong> Leonardo Musini<br>
<strong>Maintainers:</strong> Leonardo Musini<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>app_entry_point</code>, <code>mbe_schema_entry_point</code>, <code>mbe_parser_entry_point</code>, <code>mbe_app_entry_point</code><br>
<strong>Created:</strong> 2025-01-15 | <strong>Last Updated:</strong> 2025-04-23
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-98" data-entry-point-types="app|parser|schema package" data-owner="mattiamare9" data-owner-group="other">
<td><strong>nomad-plugin-mm </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/mattiamare9/nomad-plugin-mm" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-98">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> mattiamare9<br>
<strong>Authors:</strong> Mattia Marella<br>
<strong>Maintainers:</strong> Mattia Marella<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>cams_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2025-01-15 | <strong>Last Updated:</strong> 2025-02-16
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-99" data-entry-point-types="app|normalizer|parser|schema package" data-owner="PyMoDAQ" data-owner-group="other">
<td><strong>nomad-plugin-sintering </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/PyMoDAQ/nomad_plugin_sintering" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-99">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> PyMoDAQ<br>
<strong>Authors:</strong> Paul Levasseur<br>
<strong>Maintainers:</strong> Paul Levasseur<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>sintering_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2024-09-20 | <strong>Last Updated:</strong> 2024-09-20
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-100" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="Henroc" data-owner-group="other">
<td><strong>nomad-plugin-test </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>asdf</td>
<td><small>—</small></td>
<td><a href="https://github.com/Henroc/nomad-plugin-test" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-100">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Henroc<br>
<strong>Authors:</strong> Corne Frijters<br>
<strong>Maintainers:</strong> Corne Frijters<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2024-11-27 | <strong>Last Updated:</strong> 2024-11-27
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-101" data-entry-point-types="app|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-plugins </strong>(⭐ 1)<br><small>App, Schema package</small></td>
<td>A plugin for discovering other plugins.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-plugins" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-101">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-102" data-entry-point-types="app|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-polymerization-reactions </strong>(⭐ 2)<br><small>App, Schema package</small></td>
<td>A NOMAD plugin for polymerization reactions.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-polymerization-reactions" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-102">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-103" data-entry-point-types="app|normalizer" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-porous-materials </strong>(⭐ 0)<br><small>App, Normalizer</small></td>
<td>NOMAD plugin for porous materials</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-porous-materials" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-103">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-104" data-entry-point-types="app|normalizer|parser|schema package" data-owner="seb5g" data-owner-group="other">
<td><strong>nomad-pymodaq </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>nomad plugin for PyMoDAQ</td>
<td><small>—</small></td>
<td><a href="https://github.com/seb5g/pymodaq_nomad" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-104">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> seb5g<br>
<strong>Authors:</strong> Sebastien Weber<br>
<strong>Maintainers:</strong> Sebastien Weber<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code>, <code>mynormalizer</code>, <code>myapp</code><br>
<strong>Created:</strong> 2024-05-31 | <strong>Last Updated:</strong> 2024-05-31
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-105" data-entry-point-types="schema package" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-schema-plugin-run </strong>(⭐ 1)<br><small>Schema package</small></td>
<td>Run schema plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-schema-plugin-run" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-schema-plugin-run/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-105">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-106" data-entry-point-types="schema package" data-owner="nomad-coe" data-owner-group="fairmat">
<td><strong>nomad-schema-plugin-simulation-workflow </strong>(⭐ 2)<br><small>Schema package</small></td>
<td>Simulation workflow schema plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/nomad-coe/nomad-schema-plugin-simulation-workflow" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-coe.github.io/nomad-schema-plugin-simulation-workflow/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-106">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-107" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="edbarnard" data-owner-group="other">
<td><strong>nomad-scopefoundry </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>NOMAD schemas and parsers for ScopeFoundry HDF5 data files</td>
<td><small>—</small></td>
<td><a href="https://github.com/edbarnard/nomad-scopefoundry" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-107">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> edbarnard<br>
<strong>Authors:</strong> Edward S. Barnard<br>
<strong>Maintainers:</strong> Edward S. Barnard<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>scopefoundry_h5_schema_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-05-21 | <strong>Last Updated:</strong> 2025-05-22
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-108" data-entry-point-types="app" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-simulation-apps </strong>(⭐ 2)<br><small>App</small></td>
<td>A repository for housing NOMAD's collection of simulation app plugins.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-app-plugins-simulation" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-app-plugins-simulation/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-108">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-109" data-entry-point-types="example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-simulation-examples </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>Example uploads for multiple simulation codes for NOMAD development.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-simulation-examples" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-109">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-110" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-simulation-parsers </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A repository for housing NOMAD's collection of simulation parser plugins.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-parser-plugins-simulation" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-parser-plugins-simulation/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-110">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-111" data-entry-point-types="normalizer|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-simulation-workflow </strong>(⭐ 0)<br><small>Normalizer, Schema package</small></td>
<td>Schema defintions and normalizer for NOMAD simulation workflows</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-simulation-workflow" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-111">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-112" data-entry-point-types="schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-simulations </strong>(⭐ 7)<br><small>Schema package</small></td>
<td>A NOMAD plugin for FAIR schemas for simulation data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-simulations" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-simulations/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-112">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-113" data-entry-point-types="schema package" data-owner="hampusnasstrom" data-owner-group="other">
<td><strong>nomad-sintering </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>This is a schema package plugin for sintering.</td>
<td><small>—</small></td>
<td><a href="https://github.com/hampusnasstrom/nomad-sintering" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-113">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> hampusnasstrom<br>
<strong>Authors:</strong> Hampus Näsström<br>
<strong>Maintainers:</strong> Hampus Näsström<br>
<strong>Entry Points:</strong> <code>mypackage</code>, <code>sintering</code><br>
<strong>Created:</strong> 2024-05-15 | <strong>Last Updated:</strong> 2025-04-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-114" data-entry-point-types="app|schema package" data-owner="Pepe-Marquez" data-owner-group="other">
<td><strong>nomad-solar-cells-efficiency-tables </strong>(⭐ 0)<br><small>App, Schema package</small></td>
<td>This is a schema package to digitiz solar</td>
<td><small>—</small></td>
<td><a href="https://github.com/Pepe-Marquez/solar-cells-efficiecny-tables" target="_blank" rel="noopener">Code</a> | <a href="https://pepe-marquez.github.io/solar-cells-efficiecny-tables/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-114">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Pepe-Marquez<br>
<strong>Authors:</strong> Pepe Marquez<br>
<strong>Maintainers:</strong> Pepe Marquez<br>
<strong>Entry Points:</strong> <code>mypackage</code>, <code>efficiency_tables</code>, <code>myapp</code><br>
<strong>Created:</strong> 2024-05-15 | <strong>Last Updated:</strong> 2024-05-27
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-115" data-entry-point-types="normalizer" data-owner="lauri-codes" data-owner-group="other">
<td><strong>nomad-summary </strong>(⭐ 0)<br><small>Normalizer</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/lauri-codes/nomad-summary" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-115">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> lauri-codes<br>
<strong>Authors:</strong> Lauri Himanen<br>
<strong>Maintainers:</strong> Lauri Himanen<br>
<strong>Entry Points:</strong> <code>summarynormalizer</code><br>
<strong>Created:</strong> 2024-07-22 | <strong>Last Updated:</strong> 2024-08-19
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-116" data-entry-point-types="parser|schema package" data-owner="AddMorePower" data-owner-group="other">
<td><strong>nomad-SXDM_parser </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A parser plugin for SXDM processed files</td>
<td><small>—</small></td>
<td><a href="https://github.com/AddMorePower/nomad-SXDM_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-116">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> AddMorePower<br>
<strong>Authors:</strong> Guillaume Gaisné<br>
<strong>Maintainers:</strong> Guillaume Gaisné<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code><br>
<strong>Created:</strong> 2024-08-01 | <strong>Last Updated:</strong> 2025-07-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-117" data-entry-point-types="schema package" data-owner="CAU-Kiel" data-owner-group="other">
<td><strong>nomad-synthesis-plugin </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>plugin for synthesis data for Huyana Terraschke's workgroup at CAU Kiel</td>
<td><small>—</small></td>
<td><a href="https://github.com/CAU-Kiel/nomad-synthesis-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-117">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> CAU-Kiel<br>
<strong>Authors:</strong> Sebastian Brueckner<br>
<strong>Maintainers:</strong> Sebastian Brueckner<br>
<strong>Entry Points:</strong> <code>crystallization</code><br>
<strong>Created:</strong> 2024-07-10 | <strong>Last Updated:</strong> 2024-07-18
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-118" data-entry-point-types="app|example upload|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-tadf-molecules </strong>(⭐ 2)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>NOMAD plugin for thermally activated delayed fluorescent molecules</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-tadf-molecules" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-118">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-119" data-entry-point-types="app|parser|schema package" data-owner="nomad-hzb" data-owner-group="other">
<td><strong>nomad-tfsc-general </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>General nomad classes for thin film solar cells</td>
<td><small>—</small></td>
<td><a href="https://github.com/nomad-hzb/nomad-tfsc-general" target="_blank" rel="noopener">Code</a> | <a href="https://nomad-hzb.github.io/nomad-tfsc-general/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-119">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> nomad-hzb<br>
<strong>Authors:</strong> Michael Götte<br>
<strong>Maintainers:</strong> Michael Götte<br>
<strong>Entry Points:</strong> <code>tfsc_general_parser_entry_point</code>, <code>tfsc_general_experiment_experiment_parser_entry_point</code>, <code>tfsc_general_package_entry_point</code>, <code>tfsc_voila_documentation_app_entry_point</code>, <code>tfsc_perseus_search_app_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2025-03-13 | <strong>Last Updated:</strong> 2025-12-15
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-120" data-entry-point-types="example upload|parser|schema package" data-owner="pozzo-research-group" data-owner-group="other">
<td><strong>nomad-theia-plugin </strong>(⭐ 0)<br><small>Example upload, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/pozzo-research-group/theia" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-120">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> pozzo-research-group<br>
<strong>Authors:</strong> Erin Mee<br>
<strong>Maintainers:</strong> Erin Mee<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-02-28 | <strong>Last Updated:</strong> 2025-08-01
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-121" data-entry-point-types="schema package" data-owner="budschi" data-owner-group="other">
<td><strong>nomad-tutorial13following </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/budschi/tutorial13handson" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-121">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> budschi<br>
<strong>Authors:</strong> Sebastian Brueckner<br>
<strong>Maintainers:</strong> Sebastian Brueckner<br>
<strong>Entry Points:</strong> <code>mypackage</code>, <code>sintering</code><br>
<strong>Created:</strong> 2024-05-15 | <strong>Last Updated:</strong> 2024-05-15
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-122" data-entry-point-types="parser|schema package" data-owner="AddMorePower" data-owner-group="other">
<td><strong>nomad-TXRM_parser </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>A NOMAD parser for TXRM files (for IKTS)</td>
<td><small>—</small></td>
<td><a href="https://github.com/AddMorePower/nomad-TXRM_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-122">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> AddMorePower<br>
<strong>Authors:</strong> Guillaume Gaisné<br>
<strong>Maintainers:</strong> Guillaume Gaisné<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2024-12-10 | <strong>Last Updated:</strong> 2025-12-08
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-123" data-entry-point-types="app|parser|schema package" data-owner="Thin-Layers-Technology-Innsbruck" data-owner-group="other">
<td><strong>nomad-uibk-plugin </strong>(⭐ 1)<br><small>App, Parser, Schema package</small></td>
<td>UIBK schema and parser collection for NOMAD plattform.</td>
<td><small>—</small></td>
<td><a href="https://github.com/Thin-Layers-Technology-Innsbruck/nomad-UIBK-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://thin-layers-technology-innsbruck.github.io/nomad-UIBK-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-123">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Thin-Layers-Technology-Innsbruck<br>
<strong>Authors:</strong> Fabian Schöppach, Lev Ginzburg<br>
<strong>Maintainers:</strong> Lev Ginzburg<br>
<strong>Entry Points:</strong> <code>sample</code>, <code>xrfschema</code>, <code>ifmschema</code>, <code>effschema</code>, <code>xrfparser</code>, <code>ifmparser</code>, <code>ifmmodelparser</code>, <code>jvjsonparser</code>, <code>ifm_inference</code>, <code>ifmanalysisapp</code>, <code>uibksamplesapp</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code>, <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2024-05-16 | <strong>Last Updated:</strong> 2025-12-12
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-124" data-entry-point-types="app|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-unisyscat </strong>(⭐ 1)<br><small>App, Parser, Schema package</small></td>
<td>A example plugin for a demonstration for UniSysCat.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-unisyscat-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-unisyscat-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-124">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-125" data-entry-point-types="parser|schema package" data-owner="fabianschoeppach" data-owner-group="other">
<td><strong>nomad-UNITOV-plugin </strong>(⭐ 1)<br><small>Parser, Schema package</small></td>
<td>UNITOV schema and parser collection for the NOMAD platform.</td>
<td><small>—</small></td>
<td><a href="https://github.com/fabianschoeppach/nomad-UNITOV-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-125">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> fabianschoeppach<br>
<strong>Authors:</strong> Fabian Schöppach<br>
<strong>Maintainers:</strong> Fabian Schöppach<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>solution_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2024-09-26 | <strong>Last Updated:</strong> 2024-11-06
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-126" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad-utility-workflows </strong>(⭐ 4)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>A module with utilities for interacting with NOMAD via, e.g., a workflow manager.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-utility-workflows" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-utility-workflows/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-126">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-127" data-entry-point-types="parser|schema package" data-owner="mdforti" data-owner-group="other">
<td><strong>nomad-workflow-parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>Workflow partser for amstools</td>
<td><small>—</small></td>
<td><a href="https://github.com/mdforti/nomad-plugin-workflow-parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-127">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> mdforti<br>
<strong>Authors:</strong> Mariano Forti<br>
<strong>Maintainers:</strong> Mariano Forti<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code>, <code>mynormalizer</code><br>
<strong>Created:</strong> 2024-08-02 | <strong>Last Updated:</strong> 2024-08-05
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-128" data-entry-point-types="parser|schema package" data-owner="AddMorePower" data-owner-group="other">
<td><strong>nomad_ebsd_parser </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD plugin for EBSD measurements within AddMorePower</td>
<td><small>—</small></td>
<td><a href="https://github.com/AddMorePower/nomad-EBSD_parser" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-128">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> AddMorePower<br>
<strong>Authors:</strong> Guillaume Gaisné<br>
<strong>Maintainers:</strong> Guillaume Gaisné<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-04-09 | <strong>Last Updated:</strong> 2025-08-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-129" data-entry-point-types="app|normalizer|parser|schema package" data-owner="lauri-codes" data-owner-group="other">
<td><strong>nomad_example </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>An example of a plugin repository for NOMAD.</td>
<td><small>—</small></td>
<td><a href="https://github.com/lauri-codes/nomad-example" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-129">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> lauri-codes<br>
<strong>Authors:</strong> The NOMAD Authors<br>
<strong>Entry Points:</strong> <code>myparser</code>, <code>mypackage</code>, <code>mynormalizer</code>, <code>myapp</code><br>
<strong>Created:</strong> 2024-04-26 | <strong>Last Updated:</strong> 2024-04-26
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-130" data-entry-point-types="parser|schema package" data-owner="ZBT-Tools" data-owner-group="other">
<td><strong>nomad_plugin_parser_example </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>NOMAD parser example</td>
<td><small>—</small></td>
<td><a href="https://github.com/ZBT-Tools/nomad-plugin-parser-example" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-130">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> ZBT-Tools<br>
<strong>Authors:</strong> Lukas Feierabend<br>
<strong>Maintainers:</strong> Lukas Feierabend<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2024-11-23 | <strong>Last Updated:</strong> 2025-07-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-131" data-entry-point-types="parser|schema package" data-owner="MPI-CPfS-Dresden" data-owner-group="other">
<td><strong>nomad_ppms_plugin </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>Can read and analyze PPMS files</td>
<td><small>—</small></td>
<td><a href="https://github.com/MPI-CPfS-Dresden/nomad-ppms-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-131">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> MPI-CPfS-Dresden<br>
<strong>Authors:</strong> Jonathan Noky<br>
<strong>Maintainers:</strong> Jonathan Noky<br>
<strong>Entry Points:</strong> <code>parser_entry_point_data_eto_default</code>, <code>parser_entry_point_data_eto_labview</code>, <code>parser_entry_point_data_act_default</code>, <code>parser_entry_point_data_mpms_default</code>, <code>parser_entry_point_data_acms_default</code>, <code>parser_entry_point_sqc</code>, <code>schema_entry_point_eto_default</code>, <code>schema_entry_point_eto_labview</code>, <code>schema_entry_point_act_default</code>, <code>schema_entry_point_mpms_default</code>, <code>schema_entry_point_acms_default</code><br>
<strong>Created:</strong> 2024-10-08 | <strong>Last Updated:</strong> 2025-01-22
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-132" data-entry-point-types="normalizer|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>nomad_topology_normalizer </strong>(⭐ 0)<br><small>Normalizer, Schema package</small></td>
<td>Topology Normalizer</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-topology-normalizer" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-132">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-133" data-entry-point-types="api" data-owner="rettigl" data-owner-group="other">
<td><strong>oasis_optimal_footer_pages </strong>(⭐ 0)<br><small>API</small></td>
<td>OPTIMAL Oasis footer pages</td>
<td><small>—</small></td>
<td><a href="https://github.com/rettigl/oasis_optimal_footer_pages" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-133">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> rettigl<br>
<strong>Authors:</strong> Laurenz Rettig<br>
<strong>Maintainers:</strong> Laurenz Rettig<br>
<strong>Entry Points:</strong> <code>oasis_optimal_footer_pages</code><br>
<strong>Created:</strong> 2025-08-22 | <strong>Last Updated:</strong> 2025-08-26
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-134" data-entry-point-types="app|example upload|normalizer" data-owner="Tanmay2028" data-owner-group="other">
<td><strong>ontology-service-plugin </strong>(⭐ 0)<br><small>App, Example upload, Normalizer</small></td>
<td>A normalizer plugin to populate NOMAD with semantic knowledge</td>
<td><small>—</small></td>
<td><a href="https://github.com/Tanmay2028/ontology-service-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-134">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Tanmay2028<br>
<strong>Authors:</strong> Tanmay Kulkarni<br>
<strong>Maintainers:</strong> Tanmay Kulkarni<br>
<strong>Entry Points:</strong> <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-11-20 | <strong>Last Updated:</strong> 2025-11-20
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-135" data-entry-point-types="app|normalizer|parser|schema package" data-owner="PauloGitHB" data-owner-group="other">
<td><strong>oscilloscope_plugin </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/PauloGitHB/Oscilloscope_plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-135">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> PauloGitHB<br>
<strong>Authors:</strong> Paul Levasseur<br>
<strong>Maintainers:</strong> Paul Levasseur<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2024-11-12 | <strong>Last Updated:</strong> 2025-01-15
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-136" data-entry-point-types="app|parser|schema package" data-owner="PDI-Berlin" data-owner-group="other">
<td><strong>pdi-nomad-plugin </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>A plugin for PDI NOMAD containing principal techniques.</td>
<td><small>—</small></td>
<td><a href="https://github.com/PDI-Berlin/pdi-nomad-plugin" target="_blank" rel="noopener">Code</a> | <a href="https://pdi-berlin.github.io/pdi-nomad-plugin/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-136">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> PDI-Berlin<br>
<strong>Authors:</strong> Andrea Albino, Hampus Näsström, Sarthak Kapoor, Sebastian Brückner<br>
<strong>Maintainers:</strong> Andrea Albino<br>
<strong>Entry Points:</strong> <code>general_schema</code>, <code>characterization_schema</code>, <code>materials_schema</code>, <code>instrument_schema</code>, <code>processes_schema</code>, <code>epic_mbe_parser</code>, <code>mbe_app</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-measurements</code>, <code>nomad-material-processing</code><br>
<strong>Created:</strong> 2024-07-17 | <strong>Last Updated:</strong> 2025-11-24
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-137" data-entry-point-types="app|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>perovskite-solar-cell-database </strong>(⭐ 8)<br><small>App, Parser, Schema package</small></td>
<td>Perovskite solar cell data schema plugin for NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/nomad-perovskite-solar-cells-database/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-137">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-138" data-entry-point-types="schema package" data-owner="Bondoki" data-owner-group="other">
<td><strong>plotsectiontest </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>Testing the schema based on the discussion on discord.</td>
<td><small>—</small></td>
<td><a href="https://github.com/Bondoki/PlotSectionSchema" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-138">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Bondoki<br>
<strong>Authors:</strong> Ron Dockhorn<br>
<strong>Maintainers:</strong> Ron Dockhorn<br>
<strong>Entry Points:</strong> <code>plotsectiontesting</code><br>
<strong>Created:</strong> 2025-06-04 | <strong>Last Updated:</strong> 2025-06-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-139" data-entry-point-types="app|normalizer|parser|schema package" data-owner="PauloGitHB" data-owner-group="other">
<td><strong>plugin_test </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/PauloGitHB/plugin_test" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-139">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> PauloGitHB<br>
<strong>Authors:</strong> Paul Levasseur<br>
<strong>Maintainers:</strong> Paul Levasseur<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2024-09-26 | <strong>Last Updated:</strong> 2025-01-30
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-140" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="paolog8" data-owner-group="other">
<td><strong>pv-workshop </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/paolog8/pv-workshop" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-140">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> paolog8<br>
<strong>Authors:</strong> Paolo Graniero<br>
<strong>Maintainers:</strong> Paolo Graniero<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>pg_pv_experiment_parser_entry_point</code>, <code>pg_pv_parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>pg_pv_schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>pg_pv_voila_app</code>, <code>example_upload_entry_point</code>, <code>voila_scripts_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2025-07-07 | <strong>Last Updated:</strong> 2025-07-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-141" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="Nikolai-KRAUS" data-owner-group="other">
<td><strong>pvworkshop </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>foobar</td>
<td><small>—</small></td>
<td><a href="https://github.com/Nikolai-KRAUS/nomad-pv-plugin-workshop" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-141">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Nikolai-KRAUS<br>
<strong>Authors:</strong> Nikolai Kraus<br>
<strong>Maintainers:</strong> Nikolai Kraus<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>container_experiment_parser_entry_point</code>, <code>container_parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>container_schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>container_voila_app</code>, <code>example_upload_entry_point</code>, <code>voila_scripts_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2025-07-07 | <strong>Last Updated:</strong> 2025-07-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-142" data-entry-point-types="app|normalizer|parser|schema package" data-owner="PauloGitHB" data-owner-group="other">
<td><strong>PyMoDAQ </strong>(⭐ 0)<br><small>App, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/PauloGitHB/PyMoDAQ" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-142">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> PauloGitHB<br>
<strong>Authors:</strong> Paul Levasseur<br>
<strong>Maintainers:</strong> Paul Levasseur<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code><br>
<strong>Created:</strong> 2024-10-24 | <strong>Last Updated:</strong> 2024-11-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-143" data-entry-point-types="app|example upload|parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools </strong>(⭐ 19)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>Extend NeXus for experiments and characterization in Materials Science and Materials Engineering and serve as a NOMAD parser implementation for NeXus.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-143">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-144" data-entry-point-types="example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-apm </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>A reader for transferring APM from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-apm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-apm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-144">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-145" data-entry-point-types="example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-ellips </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>A reader for transferring ellipsometry data from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-ellips" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-ellips/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-145">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-146" data-entry-point-types="example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-em </strong>(⭐ 3)<br><small>Example upload</small></td>
<td>A reader for transferring EM from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-em" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-em/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-146">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-147" data-entry-point-types="example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-igor </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>pynxtools plugin for reading igor pro waves and packed experiments</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-igor" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-igor/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-147">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-148" data-entry-point-types="app|example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-mpes </strong>(⭐ 0)<br><small>App, Example upload</small></td>
<td>—</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-mpes" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-mpes/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-148">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-149" data-entry-point-types="app" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-raman </strong>(⭐ 0)<br><small>App</small></td>
<td>A reader for transferring Raman data from vendor formats to NeXus and NOMAD.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-raman" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-raman/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-149">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-150" data-entry-point-types="app|example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-spm </strong>(⭐ 0)<br><small>App, Example upload</small></td>
<td>pynxtools-spm: A pynxtools plugin for SPM (Scanning Probe Microscopy) data readers</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-spm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-spm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-150">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-151" data-entry-point-types="example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-stm </strong>(⭐ 0)<br><small>Example upload</small></td>
<td>A plugin for pynxtools to convert sts and stm files</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-stm" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-stm/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-151">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-152" data-entry-point-types="example upload" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>pynxtools-xps </strong>(⭐ 5)<br><small>Example upload</small></td>
<td>pynxtools-xps is a pynxtools reader plugin for X-ray photoelectron spectroscopy (XPS) data.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/pynxtools-xps" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/pynxtools-xps/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-152">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-153" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>rtg-sims </strong>(⭐ 11)<br><small>Parser, Schema package</small></td>
<td>A plugin for RTG SIMS.</td>
<td><small>—</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/AreaA-data_modeling_and_schemas/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-153">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-154" data-entry-point-types="schema package" data-owner="Ved-Mahajan" data-owner-group="other">
<td><strong>sintering </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>tutorial to set up plugin</td>
<td><small>—</small></td>
<td><a href="https://github.com/Ved-Mahajan/nomad-sintering" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-154">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Ved-Mahajan<br>
<strong>Authors:</strong> Ved Mahajan<br>
<strong>Maintainers:</strong> Ved Mahajan<br>
<strong>Entry Points:</strong> <code>sintering</code><br>
<strong>Created:</strong> 2025-05-20 | <strong>Last Updated:</strong> 2025-05-20
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-155" data-entry-point-types="schema package" data-owner="AG-SEK" data-owner-group="other">
<td><strong>solar-repo-perolab </strong>(⭐ 0)<br><small>Schema package</small></td>
<td>This plugin contains plot and analysis functions.</td>
<td><small>—</small></td>
<td><a href="https://github.com/AG-SEK/solar-repository-nomad-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-155">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> AG-SEK<br>
<strong>Authors:</strong> Aaron Schüller-Ruhl<br>
<strong>Maintainers:</strong> Aaron Schüller-Ruhl<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-01-08 | <strong>Last Updated:</strong> 2025-06-24
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-156" data-entry-point-types="parser" data-owner="lokik" data-owner-group="other">
<td><strong>sprkkr2nomad </strong>(⭐ 1)<br><small>Parser</small></td>
<td>—</td>
<td><small>—</small></td>
<td><a href="https://github.com/lokik/sprkkr2nomad" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-156">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> lokik<br>
<strong>Authors:</strong> Matyáš Novák<br>
<strong>Entry Points:</strong> <code>sprkkr_parser</code><br>
<strong>Created:</strong> 2024-09-07 | <strong>Last Updated:</strong> 2024-09-17
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-157" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="RubelMozumder" data-owner-group="other">
<td><strong>test-north </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/RubelMozumder/test-north" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-157">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> RubelMozumder<br>
<strong>Authors:</strong> John Doe<br>
<strong>Maintainers:</strong> John Doe<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code>, <code>north_tool</code><br>
<strong>Plugin Dependencies:</strong> <code>pynxtools-spm</code><br>
<strong>Created:</strong> 2025-10-20 | <strong>Last Updated:</strong> 2025-12-11
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-158" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="GarzonDiegoFEUP" data-owner-group="other">
<td><strong>test-plugin-pv </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>Example PV template</td>
<td><small>—</small></td>
<td><a href="https://github.com/GarzonDiegoFEUP/test-plugin-pv" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-158">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> GarzonDiegoFEUP<br>
<strong>Authors:</strong> Diego Garzon<br>
<strong>Maintainers:</strong> Diego Garzon<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>INL_experiment_parser_entry_point</code>, <code>INL_parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>INL_schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>INL_voila_app</code>, <code>example_upload_entry_point</code>, <code>voila_scripts_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2025-07-07 | <strong>Last Updated:</strong> 2025-07-08
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-159" data-entry-point-types="app|parser|schema package" data-owner="Oliver24-hub" data-owner-group="other">
<td><strong>test-plugin-workshop </strong>(⭐ 0)<br><small>App, Parser, Schema package</small></td>
<td>wqe</td>
<td><small>—</small></td>
<td><a href="https://github.com/Oliver24-hub/test-pv-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-159">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> Oliver24-hub<br>
<strong>Authors:</strong> Oliver Klement<br>
<strong>Maintainers:</strong> Oliver Klement<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>LabTEST_experiment_parser_entry_point</code>, <code>LabTEST_parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>LabTEST_schema_package_entry_point</code>, <code>app_entry_point</code>, <code>LabTEST_voila_app</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2025-07-07 | <strong>Last Updated:</strong> 2025-07-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-160" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="blueraft" data-owner-group="other">
<td><strong>test-pv-plugin </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/blueraft/test-pv-plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-160">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> blueraft<br>
<strong>Authors:</strong> AHmed Ilyas<br>
<strong>Maintainers:</strong> AHmed Ilyas<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>fairmat_experiment_parser_entry_point</code>, <code>fairmat_parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>fairmat_schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>fairmat_voila_app</code>, <code>example_upload_entry_point</code>, <code>voila_scripts_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2025-07-07 | <strong>Last Updated:</strong> 2025-07-07
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-161" data-entry-point-types="app|example upload|normalizer|parser|schema package" data-owner="paolog8" data-owner-group="other">
<td><strong>test_nomad </strong>(⭐ 0)<br><small>App, Example upload, Normalizer, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/paolog8/test_nomad" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-161">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> paolog8<br>
<strong>Authors:</strong> Paolo Graniero<br>
<strong>Maintainers:</strong> Paolo Graniero<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-07-04 | <strong>Last Updated:</strong> 2025-07-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-162" data-entry-point-types="parser|schema package" data-owner="ccc3001" data-owner-group="other">
<td><strong>test_plugin </strong>(⭐ 0)<br><small>Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/ccc3001/test_plugin" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-162">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> ccc3001<br>
<strong>Authors:</strong> ccc3001<br>
<strong>Maintainers:</strong> ccc3001<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code><br>
<strong>Created:</strong> 2025-05-08 | <strong>Last Updated:</strong> 2025-12-02
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-163" data-entry-point-types="app|example upload|parser|schema package" data-owner="RoteKekse" data-owner-group="other">
<td><strong>test_pv_nomad </strong>(⭐ 0)<br><small>App, Example upload, Parser, Schema package</small></td>
<td>nomad example template</td>
<td><small>—</small></td>
<td><a href="https://github.com/RoteKekse/test_pv_nomad" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-163">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> RoteKekse<br>
<strong>Authors:</strong> Micha<br>
<strong>Maintainers:</strong> Micha<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>PVLab_experiment_parser_entry_point</code>, <code>PVLab_parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>PVLab_schema_package_entry_point</code>, <code>app_entry_point</code>, <code>PVLab_voila_app</code>, <code>example_upload_entry_point</code>, <code>voila_scripts_entry_point</code><br>
<strong>Plugin Dependencies:</strong> <code>nomad-baseclasses</code><br>
<strong>Created:</strong> 2025-07-04 | <strong>Last Updated:</strong> 2025-07-04
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-164" data-entry-point-types="parser|schema package" data-owner="FAIRmat-NFDI" data-owner-group="fairmat">
<td><strong>transmission </strong>(⭐ 11)<br><small>Parser, Schema package</small></td>
<td>A plugin for NOMAD containing base sections for transmission spectrophotometry.</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas" target="_blank" rel="noopener">Code</a> | <a href="https://fairmat-nfdi.github.io/AreaA-data_modeling_and_schemas/" target="_blank" rel="noopener">Docs</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-164">
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
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-165" data-entry-point-types="app|example upload|schema package" data-owner="budschi" data-owner-group="other">
<td><strong>unicornone-rheed </strong>(⭐ 0)<br><small>App, Example upload, Schema package</small></td>
<td>RHEED data from UnicornOne</td>
<td><small>—</small></td>
<td><a href="https://github.com/budschi/unicornone-rheed" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-165">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> budschi<br>
<strong>Authors:</strong> Sebastian Brückner<br>
<strong>Maintainers:</strong> Sebastian Brückner<br>
<strong>Entry Points:</strong> <code>schema_package_entry_point</code>, <code>app_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-03-19 | <strong>Last Updated:</strong> 2025-03-21
</p>
</div>
</details>
</td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="plugin-registry-row-166" data-entry-point-types="example upload|normalizer|parser|schema package" data-owner="16-vikrant" data-owner-group="other">
<td><strong>wannierberri </strong>(⭐ 0)<br><small>Example upload, Normalizer, Parser, Schema package</small></td>
<td>Wannier Berri parser</td>
<td><small>PyPI</small></td>
<td><a href="https://github.com/16-vikrant/nomad-parser-wannierberri" target="_blank" rel="noopener">Code</a></td>
</tr>
<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="plugin-registry-row-166">
<td colspan="4" style="padding: 0; border-top: none;">
<details style="margin: 0; padding: 12px 16px; border: 0px">
<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>
<div style="margin-top: 12px; padding-top: 12px;">
<p>
<strong>Owner:</strong> 16-vikrant<br>
<strong>Authors:</strong> Vikrant Chaudhary<br>
<strong>Maintainers:</strong> Vikrant Chaudhary<br>
<strong>Entry Points:</strong> <code>parser_entry_point</code>, <code>schema_package_entry_point</code>, <code>normalizer_entry_point</code>, <code>example_upload_entry_point</code><br>
<strong>Created:</strong> 2025-04-02 | <strong>Last Updated:</strong> 2025-07-31
</p>
</div>
</details>
</td>
</tr>
</tbody>
</table>
