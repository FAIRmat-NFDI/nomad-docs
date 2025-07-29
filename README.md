# `nomad-docs`

This repository contains the documentation for the central NOMAD distribution.

## Contributing

- Typos, corrections, and missing docs can be reported by [Creating an Issue](https://github.com/FAIRmat-NFDI/nomad-docs/issues/new)

- For internal contributions (write access to the repo required), please open a pull request (PR) with your changes. **At least one review from a FAIRmat co-worker is required before merging**. If you are not sure who to assign, please ask in the PR conversation by tagging @ahm531 or @JFRudzinski.

- For external contributions, please follow the [External Contribution Instructions](#external-contribution-instructions)

### Writing Guide

When contributing, please check the <a href="https://github.com/FAIRmat-NFDI/nomad-docs/blob/main/docs/writing_guide.md" target="_blank" rel="noopener">writing guide</a> for best practices.

---

## Running the Docs Server Locally

If you have a `nomad-dev-distro` setup, you can follow the [day to day development](https://github.com/FAIRmat-NFDI/nomad-distro-dev?tab=readme-ov-file#day-to-day-development) instructions to install `nomad-docs` as a submodule there.


If you *do not* have an up-to-date Python installation (3.11 or 3.12), see [Help to install Python](#help-to-install-python-311-or-312) below.

### 1. Install uv

#### (a) Standalone

**On macOS and Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Or, from PyPI:
```

#### (b) With pip
```bash
pip install uv
```

#### (c) With pipx
```bash
pipx install uv
```

If installed via the standalone installer, uv can update itself to the latest version:

```bash
uv self update
```

### 2. Run the Local Docs Server

Once `uv` is installed, you can start the MkDocs server with:

```bash
uv run mkdocs serve
```

This will install all requirements in a virtual environment and start the local development server.

> 💡 **Tip:** To compare your local docs with the latest version once you start making significant changes, use the [DEV Deployment DOCS](https://nomad-lab.eu/prod/v1/develop/docs/index.html).


### How to run the tests

```bash
uv run --extra dev pytest
```


### How to check and remove unused assets

This repository includes a utility to help keep the documentation tree clean by detecting and safely handling **unreferenced assets** such as files in `images/` and `data/` directories.

#### Tool: `utils/find_unused_assets.py`

This script checks whether files stored in `images/` or `data/` subdirectories (under `docs/`) are actually referenced by any Markdown files in the **same folder**. If not, they are considered unreferenced.

#### Usage

From the root of the repository:

```bash
# List all unreferenced assets
python utils/find_unused_assets.py
```

```bash
# Move unreferenced assets to .trash/ (safe mode)
python utils/find_unused_assets.py --remove
```
> By default, unreferenced files are **not deleted**. They are moved to a `.trash/` folder at the project root so you can review and recover them if needed.

Here you can check if the deletions have mistakenly broken any links before permanent deletion.

```bash
# Permanently delete all assets in .trash/
python utils/find_unused_assets.py --empty-trash
```

---
## Appendix

### External Contribution Instructions

#### 1. **Fork the Repository**

Click the **Fork** button at the top right of this page to create a copy of the repo under your GitHub account.

#### 2. **Clone Your Fork Locally**

```bash
git clone https://github.com/your-username/nomad-docs.git
cd nomad-docs
```

#### 3. **Create a New Branch for Your Changes**

```bash
git checkout -b my-feature-branch
```

#### 4. **Make and Commit Your Changes**

#### 5. **Push to Your Fork**
```bash
git push origin my-feature-branch
```

#### 6. **Open a Pull Request**
   - Go to your fork on GitHub.
   - Click **"Compare & pull request"**.
   - Choose the base repo (`FAIRmat-NFDI/nomad-docs`) and target branch (e.g., `main`).
   - Describe your changes and submit the PR.

> ✅ Your PR will be reviewed by the maintainers. You don’t need write access to contribute this way.

---

### Help to install Python 3.11 or 3.12

> **Note:** Replace `3.11` with `3.12` below if you prefer to use Python 3.12.

If Python 3.11 is not installed on your system, use the instructions below based on your OS:

**Debian Linux**

```bash
sudo apt install python3.11
```

**Red Hat Linux**

```bash
sudo dnf install python3.11
```

**macOS**

```bash
brew install python@3.11
```

**Windows PowerShell**

1. Download the installer from the [official Python website](https://www.python.org/downloads/release/python-3110/).
2. Run the installer.
3. Make sure to check the box **"Add Python 3.11 to PATH"** during installation.

