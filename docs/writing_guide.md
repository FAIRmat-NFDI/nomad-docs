# Documentation Development and Writing Guide

This is a guide for best practices when contributing to the NOMAD documentation. Our goal is to make the documentation consistent, clear, and easy to navigate for all users.

## Philosophy: Diátaxis

The NOMAD Docs follow the [Diátaxis framework](https://diataxis.fr/){:target="_blank" rel="noopener"} for technical documentation. This framework organizes content into four distinct types, each serving a different user need:

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
- **Stay consistent.** Follow existing terminology, formatting, and naming conventions; introduce new terms sparingly and define them clearly. When in doubt, cross-check other docs pages or ask the documentation maintainers.
- **Keep essential context in place, centralize reusable content.** Provide enough information directly on the page so the user can follow without friction. For reused, larger blocks of content, keep a single authoritative version and link to it.
- **Check accuracy with the actual system.** Verify commands, screenshots, and examples against the current NOMAD deployment. *Only merge a docs PR after the corresponding code changes have been merged into `nomad-lab`’s `develop` branch*.

## Styling & Conventions

### Headings & Structure

**Auto-TOC awareness:** Headings populate the Table of Contents; admonition titles do not. Use real headings for navigable sections.

### Links

**Link checks.** Broken internal or external links will cause CI/CD to fail. Try to fix them when possible. If you cannot resolve a broken link, create an issue and tag a maintainer.

**Descriptive link naming.** Use descriptive link text (instead of `here/link`).

**Internal links: standardized naming.** Use the path hierarchy to the referenced page or section, separated by >'s. For example: `[Tutorial > Exploring Data > Search Interface & Filters](<path-to-referenced-section>)`. Long paths can be shortened with `...`, e.g., `[Tutorial > ... > Search Interface & Filters](<path-to-referenced-section>)`, using your best judgement.

If the referenced section belongs to the current page, drop the global path, i.e., `[Search Interface & Filters](<path-to-referenced-section>)`.

**External links to NOMAD-related documentation.** External links to, e.g., NOMAD plugin documentation should follow the same syntax as internal link names, with the name of the plugin as the root. For example, `[NOMAD Utility Workflows > How-to Guides > Create Custom Workflows](https://fairmat-nfdi.github.io/nomad-utility-workflows/how_to/create_custom_workflows.html){:target="_blank" rel="noopener"}`.

**Other external links: descriptive text + new tab.** For other external links, use descriptive names, not raw URLs.

**New window for external links.** All external links should use `[](){:target="_blank" rel="noopener"}` to open a new browser window.

### Terminology, capitalization, and text stylizing

**Use consistent, canonical names.** NOMAD, NOMAD Oasis, MongoDB, Elasticsearch, etc.

**Backticks, quotes, bold, and italics.**

- Use `backticks` for:
    - Code (e.g., inline commands, file names, parameters, API endpoints, config options, environment variables).
    - Literal values the user must type, e.g., in the UI.

- Use "double quotes" when quoting actual text strings (e.g., labels in the UI, button names, error messages).

<!-- TODO check bold and it usage and try to be more specific -->
- Use **bold** for:
    - Certain UI elements (buttons, menu items, field names).
    - Bullet list labels for clarity.
    - Important emphasis (but use sparingly).

- Use *italics* for:
    - Emphasis in narrative text.
    - Terms being introduced for the first time.

**Add new terms to glossary.** Add new NOMAD-specific terms to the [Glossary](https://github.com/FAIRmat-NFDI/nomad-docs/blob/main/docs/reference/glossary.md){:target="_blank" rel="noopener"}. External terms/concepts should link to external definitions, when appropriate (use your best judgement).

### Code, commands, and UI text

**Blocks & highlighting.** Use fenced code blocks with a language tag (e.g., \`\`\`bash, \`\`\`python).

**Copy-paste ready.** Commands should run as-is. If a placeholder is required, surround it with angle brackets and use a descriptive name with hyphens separating words. Like this: `<your-token>`.

**UI copy.** Quote exact button/label text in bold or code.

### Admonitions

> ⚠️ **Attention:** An admonition is a highlighted block in documentation used to draw attention to important information, such as notes, warnings, tips, or examples.

<!-- TODO Do we want to restrict to only these? Or allow custom naming? -->
**Do not use custom titles for admonitions.**
Any of the standard admonition titles are allowed. Additionally, here is a list of "custom" titles that can be used within the docs:

- !!! warning "Attention"

- !!! tip "Important"

If you would like to propose a standard extension, create an issue with your suggestion and an example image of the new admonition.

## Images

Images should be used sparingly. Each image that is added should be seen as a costly investment: keeping images up-to-date is very hard when thinking long-term upkeep of the documentation.

Images that can be represented in code should be preferred. The docs support [Mermaid](https://mermaid.js.org/){:target="_blank" rel="noopener"}, and you can add mermaid images inside markdown with:

````md
<figure markdown style="width: 100%">
  ``` mermaid
  %%{init:{'flowchart':{'nodeSpacing': 25}}}%%
  graph LR
    subgraph NOMAD Distribution
      subgraph NOMAD Plugin A
        ro1(Entry point: Schema)
      end
    end
  ```
  <figcaption>Relation between NOMAD distributions, plugins and entry points.</figcaption>
</figure>
````

The second best format is SVG. SVG files scale to different resolutions, produce small file sizes, and are easy to modify later. It is recommended to use [draw.io](https://www.drawio.com/){:target="_blank" rel="noopener"} to produce any complex diagrams, and then export them in the SVG format using the "Include a copy of my diagram" option which allows for easy editing later.

When other options are not suitable, the preferred raster image format is JPG.

### Adding image sliders

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

If you use more than one slider on the same page, make sure to give them different ids. The same applies for the navigation arrows.

## Repo Organization

**Keep the navigation structure.** The location of docs .md files should mirror the navigation bar, with subfolders named after the organizational subsections of the bar.

**Images and data.** All assets specific to an individual markdown file should be stored within an immediate sub-directory of the file, labeled accordingly. Please use `images/` and `data/` for the image and data files, respectively. Sharing assets between .md files in different locations is currently not allowed. If there is an exceptional case, please create a GitHub issue and tag a relevant maintainer.
