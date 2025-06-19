# Documentation Development and Writing Guide

This is a guide for best practices when contributing to the NOMAD documentation.

## No broken links!

Before merging make sure that the mkdocs logs do not report any broken links. This applies even if these links are not relevant to your changes. If you do not know how to address the broken links, create an issue in the Github repo and tag someone who you think could be of assistance.

## Images and Data

All assets specific to an individual markdown file should be stored within an immediate sub-directory of the file, labeled accordingly. Please use `images/` and `data/` for the image and data files, respectively.

## Sections Hierarchy

single "#" sections should only be used at the beginning of the md file

## Standardized Internal and External Link Naming

Do not use `HERE` as a name for links. For internal links use the path hierarchy to the referenced page or section, separated by >'s. For example: `[Tutorial > Exploring Data > Search Interface & Filters](<path-to-referenced-section>)`. Long paths can be abbreviated to the first and last parts: by using `[Tutorial > ... > Search Interface & Filters](<path-to-referenced-section>)` If the referenced section belongs to the current page, drop the global path, i.e., `[Search Interface & Filters](<path-to-referenced-section>)`. External links to NOMAD plugins or other NOMAD-related documentation should follow the same syntax, with the name of the plugin as the root. For other external links provide some sort of descriptive name and use your discretion.

## External Links

Use [](){:target="_blank"} for external links to open a new browser window.

## Admonitions

Here is a list of currently used admonitions within the docs:

- !!! warning "Attention"

- !!! note

- !!! tip

- !!! tip "Important"

<!-- the following three were added in the preparation in the tutorials pages -->
- !!! info
- !!! task
- !!! example

## Adding image sliders
Image sliders can be added using the following syntax:

```html
<div class="image-slider" id="slider#*">
    <div class="nav-arrow left" id="prev#">←</div>
    <img src="" alt="" class="active">
    <img src="" alt="">
    <img src="" alt="">
    <div class="nav-arrow right" id="next#">→</div>
</div>
```
To minimize flickering effect during transitions, make all the sliding images of the same size. <!-- we may need to fix this issue from Java or CSS at some point -->

If you use more than one slider on the same page, make sure to give them different id. The same applies for the navigation arrows.
