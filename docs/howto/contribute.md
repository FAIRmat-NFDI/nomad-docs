# How to contribute

This guide applies to every repository in the NOMAD ecosystem, including the core `nomad-lab` package, plugins, distributions, and this documentation. Individual repositories may add their own requirements on top of these guidelines. In this guide, *pull request (PR)* also covers GitLab *merge requests (MRs)*.

!!! tip "Adding custom features? Write a plugin."

    To extend NOMAD with your own functionality, such as schemas, parsers, normalizers, apps, or APIs, write a plugin instead of opening a PR against the core `nomad-lab` repository (`nomad-FAIR`). Plugins can be developed, released, and installed on their own schedule. See {{ nav_link("howto/plugins/plugins.md", breadcrumb=True) }} to get started. Contributions to the core repository should focus on bug fixes and on general-purpose improvements that benefit all users.

!!! warning "Found a security issue?"

    Do not open a public issue or PR. See [Report security issues](#report-security-issues) instead.

## Where to contribute

Open PRs, and issues where needed, on GitHub. Most repositories, such as plugins, distributions, and this documentation, are developed directly on GitHub, and their CI runs there.

The core `nomad-lab` package is the exception: its main development happens on the [MPCDF GitLab](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR){:target="_blank" rel="noopener"}, which requires an MPCDF account. External contributors should use its GitHub mirror, [FAIRmat-NFDI/nomad](https://github.com/FAIRmat-NFDI/nomad){:target="_blank" rel="noopener"}. PRs opened there are automatically copied to GitLab, where the CI pipeline runs and the change is merged. Your authorship is preserved.

## Report bugs and request features

Report bugs, request features, and ask questions primarily on our [Discord server](https://discord.gg/Se9qHracC8){:target="_blank" rel="noopener"}, and discuss them there. The maintainers and the community can often help quickly, point you to the right repository, or suggest an existing solution. If the problem needs to be tracked, the maintainers may ask you to open an issue in the relevant repository.

- **Bugs**: describe what you observed and how to reproduce it. Include the NOMAD version or URL you are using, any relevant upload or entry IDs, and example files or code snippets. Paste code and error messages as text, not as screenshots.
- **Features**: describe the use case behind the feature, not only the proposed solution.

**Discuss larger changes on Discord before you start working on them.** For new features, refactorings, or changes to public interfaces, agree on the approach with the maintainers first. This avoids spending time on a PR that cannot be merged, for example because the feature would be better implemented as a plugin.

Do not report security issues on Discord. See [Report security issues](#report-security-issues) instead.

## Set up a development environment

Use [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"} to set up a local development environment for NOMAD and its plugins. Follow the instructions in its [README](https://github.com/FAIRmat-NFDI/nomad-distro-dev#readme){:target="_blank" rel="noopener"}.

## Branching model

Our repositories follow [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/){:target="_blank" rel="noopener"}:

- `develop` is the integration branch. **All PRs must target `develop`.**
- Changes that are merged into `develop` are included in the next release.
- `main` reflects the latest release. Release and hotfix branches are managed by the maintainers. Do not open PRs against `main` or against release branches, not even for urgent fixes. Target `develop`, and say in the PR description if the fix should be included in a patch release.
- Create your feature or bugfix branch from an up-to-date `develop`. If you do not have write access to the repository, work on a branch in your own fork.

## Code guidelines

### Mandatory guidelines are enforced by CI

All mandatory code guidelines are implemented as checks in each repository's CI pipeline. This is the only way to keep them up to date: the CI configuration and the tool settings in the repository, such as in `pyproject.toml`, are the authoritative definition of the rules. If CI passes, your code meets the mandatory guidelines. Depending on the repository, the checks include:

- formatting and linting with [ruff](https://docs.astral.sh/ruff/){:target="_blank" rel="noopener"} (`ruff format` and `ruff check`)
- static type checking with [mypy](https://mypy.readthedocs.io/){:target="_blank" rel="noopener"}
- spell checking with [typos](https://github.com/crate-ci/typos){:target="_blank" rel="noopener"}
- the test suite with [pytest](https://docs.pytest.org/){:target="_blank" rel="noopener"}

Run these checks locally before you push, because they are a common reason for failing pipelines.

### Recommended practices

The following guidelines are not enforced automatically, but reviewers will look for them:

- **Keep it simple.** Only make code complicated when it is really necessary.
- **Avoid circular dependencies.** Dependencies between modules should only go in one direction.
- **Test the public interface** of each module.
- **Document the public interface** of each module with [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings){:target="_blank" rel="noopener"}. Keep Markdown in docstrings to a minimum.
- **Write code that explains itself.** Only comment individual lines when there is no simpler way to write them, for example for workarounds to known issues in dependencies, non-obvious interactions between parts of the code, or performance optimizations.
- **Do not commit commented-out code.** Git keeps the history.
- **Use descriptive names.** Avoid abbreviations, except for well-established ones such as `exc` or `e` (exception), `repo` (repository), `utils` (utilities), `f` (file-like objects), and `i` (index variables).
- **Use NOMAD terminology consistently**, such as *upload*, *entry*, and *mainfile*. See the {{ nav_link("reference/glossary.md") }}.
- **Log sensibly.** Follow {{ nav_link("howto/plugins/tools/logging.md", breadcrumb=True) }}.

## Open a pull request

1. Push your branch and open a PR against `develop`. If your work is not ready for review yet, open it as a draft PR.
2. Fill in the PR description using the repository's default template. If the repository does not have one yet, use the following:

    ```markdown
    ## Summary

    <!-- What does this change do and why? A few sentences. Reviewers read this first. -->

    ## Related issues / MRs / PRs

    <!-- Optional, delete this section if not applicable. Use "Closes #123" so the issue closes automatically on merge. -->

    -

    ## What changed

    <!-- The main changes, as bullets. Point out anything non-obvious or where you'd like extra attention. -->

    -

    ## How to test

    <!-- Point to unit/e2e tests that verify the behaviour, or to any manual steps that can be taken to verify the change. -->

    1.

    ## Screenshots / output

    <!-- Optional, delete this section if not applicable. Before/after for UI changes, or sample output for CLI/API changes. -->

    ## Notes for reviewers

    <!-- Optional, delete this section if not applicable. Open questions, trade-offs you considered, follow-up work planned, areas outside your expertise. -->
    ```

3. Make sure the CI pipeline passes. **All existing tests must pass** before a PR can be merged.
4. Add tests for your changes. Most new features and bug fixes need accompanying tests. Reviewers may ask for more tests before approving.
5. Update the documentation if your change affects users, for example new or changed APIs, CLI commands, configuration options, schema annotations, or UI behaviour. Documentation lives in the [`nomad-docs`](https://github.com/FAIRmat-NFDI/nomad-docs){:target="_blank" rel="noopener"} repository, so open a separate PR there and link the two PRs.
6. Do not edit `CHANGELOG.md` by hand. Where a repository has one, it is generated at release time.
7. Most PRs are squash-merged into a single commit, so you do not need to clean up the individual commits on your branch.

Keep each PR focused on a single change, and explain both what it changes and why. Small PRs get reviewed faster.

## AI-generated contributions

You may use AI tools to help write code, tests, or documentation. However:

- **You are responsible for everything you submit.** Review AI-generated content yourself, understand it, and be prepared to explain and defend it during review.
- Make sure AI-generated content meets the same quality and testing standards as any other contribution, and that you have the right to submit it under the repository's [license](#licensing).
- Repositories in the NOMAD ecosystem may provide an [`AGENTS.md`](https://agents.md/){:target="_blank" rel="noopener"} file at the repository root with instructions for AI coding agents. If one is present, make sure your agent reads it and follows its instructions.
- **Do not let AI agents act on your behalf without supervision.** A human must review every issue, PR, and review comment before it is posted.
- If a project gets flooded with low-quality, AI-generated issues or PRs, maintainers may restrict or disable issues and PRs for that project.

## Licensing

By contributing, you agree that your contribution is released under the license of the repository you contribute to, as given in its `LICENSE` file. For example, `nomad-FAIR` is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0){:target="_blank" rel="noopener"}.

## Report security issues

If you find a vulnerability or other security-related problem, **do not open a public issue or PR**, because that would disclose the problem before a fix is available.

Instead, email us at [support@nomad-lab.eu](mailto:support@nomad-lab.eu). Include a description of the problem, the affected repository and version, and steps to reproduce it.
