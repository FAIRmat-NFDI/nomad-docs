# PR Review Guide for Agents

As an AI agent, your primary responsibility when reviewing Pull Requests (PRs) in this repository is to ensure they adhere to our established documentation standards. All contributions must follow the guidelines outlined in the [Documentation Development and Writing Guide](writing_guide.md).

## Review Checklist

Before approving any PR, verify the following:

1.  **Diátaxis Framework**: Ensure the content is correctly categorized into one of the four types:
    *   **Tutorials**: Learning-oriented, step-by-step introductions.
    *   **How-to guides**: Goal-oriented, practical instructions.
    *   **Explanations**: Understanding-oriented, clarifications and context.
    *   **Reference**: Information-oriented, precise and authoritative.

2.  **Best Practices**: Check that the contribution follows our best practices:
    *   Context is clearly set.
    *   Content is structured around user flows.
    *   The text is detailed but concise.
    *   Clarity is prioritized over cleverness.
    *   Terminology and formatting are consistent with existing documentation.
    *   Content is accurate and verified against the current system.

3.  **Styling & Conventions**:
    *   **Headings**: Only one H1 (`#`) per page for the title.
    *   **Links**:
        *   No broken links (CI/CD will fail).
        *   Descriptive link names (no "here").
        *   Standardized internal link naming (`Category > ... > Page`).
        *   External links open in a new tab (`{:target="_blank" rel="noopener"}`).
    *   **Terminology**:
        *   Use canonical names (e.g., NOMAD, NOMAD Oasis).
        *   Correct usage of `backticks`, "double quotes", **bold**, and *italics*.
        *   New terms are added to the [Glossary](reference/glossary.md).
    *   **Code Blocks**: Fenced with language tags (e.g., ```python).
    *   **File and Directory Structure**:
        *   The location of the `.md` files should mirror the navigation bar.
        *   Images and data are stored in `images/` and `data/` subdirectories next to the markdown file.

4.  **Admonitions**:
    *   Use standard admonition titles. Do not use custom titles.

A thorough review against these points is crucial for maintaining the quality and consistency of our documentation.
