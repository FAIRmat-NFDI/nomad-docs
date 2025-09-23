# Documentation Development and Writing Guide

This is a guide for best practices when contributing to the NOMAD documentation. Our goal is to make the documentation consistent, clear, and easy to navigate for all users.

## Philosophy: Diátaxis

The NOMAD Docs follow the [Diátaxis framework](https://diataxis.fr/) for technical documentation. This framework organizes content into four distinct types, each serving a different user need:

- **Tutorials**: learning-oriented, step-by-step introductions.
- **How-to guides**: goal-oriented, practical instructions.
- **Explanations**: understanding-oriented, clarifications and context.
- **Reference**: information-oriented, precise and authoritative.

When contributing, identify which type of documentation your addition belongs to. A clear separation will help users quickly find what they need.

> **Tip:** Contributions often span multiple types. For example, a new *How-to* may also require a supporting *Explanation* page. It may help you to first draft all of your material in one place, and then reorganize it according to the Diátaxis structure.

## Best Practice

- **Set the context clearly.** For Tutorials and How-tos, define prerequisite knowledge and list additional resources at the top of the page. For Explanations, provide enough background to orient the reader.
- **Think in user flows.** Imagine how a user encounters problems or tasks, not how the codebase is organized.
- **Be as detailed as required, as concise as possible.** Include all steps or context the user needs, but avoid unnecessary narrative.
- **Prefer clarity over cleverness.** Simple, direct wording beats jargon, metaphors, or over-complicated phrasing.
- **Stay consistent.** Follow existing terminology, formatting, and naming conventions; introduce new terms sparingly and define them clearly. When in doubt, cross-check other docs pages or ask the managerial team.
- **Keep essential context in place, centralize reusable content.** Provide enough information directly on the page so the user can follow without friction. For reused, larger blocks of content, keep a single authoritative version and link to it.
- **Check accuracy with the actual system.** Verify commands, screenshots, and examples against the current NOMAD deployment.

## Styling & Conventions

### Headings & Structure

**One H1 per page:** Use single `#` sections only at the top of the file for the page title.

**Order and depth:** Don’t skip levels (e.g., go ## → ####). Keep sections short; one idea per section.

**Auto-TOC awareness:** Headings populate the ToC; admonition titles do not. Use real headings for navigable sections.

## No broken links!

Before merging make sure that the mkdocs logs do not report any broken links. This applies even if these links are not relevant to your changes. If you do not know how to address the broken links, create an issue in the GitHub repo and tag someone who you think could be of assistance.

## Images and Data

All assets specific to an individual markdown file should be stored within an immediate sub-directory of the file, labeled accordingly. Please use `images/` and `data/` for the image and data files, respectively.

## Sections Hierarchy

single "#" sections should only be used at the beginning of the md file

## File organization should mirror the navigation bar

Files and sub-folders should be stored according to the navigation bar organization in `mkdocs.yml`.

## Maintain the accuracy of the overview pages

If you add a new page to the docs, make sure to add this page to the corresponding overview page (when applicable).

## Standardized Internal and External Link Naming

Do not use `HERE` as a name for links. For internal links use the path hierarchy to the referenced page or section, separated by >'s. For example: `[Tutorial > Exploring Data > Search Interface & Filters](<path-to-referenced-section>)`. Long paths can be abbreviated to the first and last parts: by using `[Tutorial > ... > Search Interface & Filters](<path-to-referenced-section>)` If the referenced section belongs to the current page, drop the global path, i.e., `[Search Interface & Filters](<path-to-referenced-section>)`. External links to NOMAD plugins or other NOMAD-related documentation should follow the same syntax, with the name of the plugin as the root. For other external links provide some sort of descriptive name and use your discretion.

## External Links

Use `[](){:target="_blank"}` for external links to open a new browser window.

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
