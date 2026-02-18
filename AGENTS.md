# AGENTS.md - Developer Guidelines for DENT-OIP

This document provides coding guidelines and conventions for AI coding agents and human developers working on the DENT-OIP (Dentistry Technical Framework Supplement Orthodontic Imaging Profile) project.

## Project Overview

DENT-OIP is an **IHE Profile** for orthodontic imaging standards, written in **reStructuredText (RST)** and built using Sphinx. The project follows IHE Profile conventions as defined in the [IHE Official Templates](https://wiki.ihe.net/index.php/Official_Templates).

**Version**: v0.2.7  
**Primary Language**: reStructuredText (`.rst`)  
**Support Code**: Python 3.13 (for building DICOM files, tables, and RST generation)  
**Documentation Tool**: Sphinx with sphinx-book-theme  
**Outputs**: HTML (primary), DOCX, PDF  
**Repository**: <https://github.com/open-ortho/dent-oip>

### Document Structure (IHE Profile Format)

- **Preamble**: Foreword, Scope, Normative References, Requirements
- **Volume 1**: Orthodontic Imaging Profile (actors, transactions, integration profile options, process flow, security)
- **Volume 2**: Transactions (detailed transaction specifications)
- **Volume 3**: DICOM specifications (conventions, definitions, IOD definitions, module definitions)
- **Appendices**: View examples, device examples, definitions, code tables

## Build Commands

### Local Development (Testing Only)

```bash
# Install dependencies using pipenv
pipenv install

# Build HTML documentation locally for testing
pipenv run make html

# Build all formats (HTML, DOCX, PDF)
pipenv run make dist

# Clean all generated files
make clean
```

### Deployment (Automated via GitHub Actions)

**Do not run make commands manually for deployment.** Builds and deployments are automated:

- **Nightly builds**: Automatically triggered on push to `develop` branch (see `.github/workflows/nightly.yml`)
- **Release builds**: Automatically triggered on push to `master` branch (see `.github/workflows/release.yml`)
- Both workflows build HTML, PDF, and DOCX, then deploy to GitHub Pages at:
  - Root landing page: <http://open-ortho.org/dent-oip/> (from `gh-pages-root/index.html`)
  - Nightly: <http://open-ortho.org/dent-oip/nightly/>
  - Release: <http://open-ortho.org/dent-oip/release/>
- **IMPORTANT**: The `gh-pages-root/index.html` file is the landing page that provides navigation to both nightly and release builds. Both workflows deploy this file to the root of gh-pages to ensure users can navigate between versions.

### Platform-Specific Notes (Local Testing)

- **macOS**: Requires `brew install coreutils` and replace `cut` with `gcut` in Makefile
- **macOS PDF**: Requires `brew install basictex` and LaTeX packages: `sudo tlmgr install latexmk tex-gyre fncychap wrapfig capt-of framed needspace tabulary varwidth titlesec`
- **Ubuntu/Debian**: May require `sudo apt install texlive libreoffice`

### Automated Build Process

The build automatically:

1. Initializes git submodules (for orthoviews-linedrawings)
2. Generates DICOM files from PNG images
3. Creates CSV tables from DICOM headers
4. Downloads FHIR ValueSets and converts to CSV
5. Generates RST pages for each view
6. Builds final documentation

## Test Commands

### Running Tests

```bash
# Run all tests (uses unittest)
python3 -m unittest test_view_maker.py

# Run specific test
python3 -m unittest test_view_maker.Test.test_generate_tables_in_csv
python3 -m unittest test_view_maker.Test.test_generate_rst_pages
python3 -m unittest test_view_maker.Test.test_generate_views_in_dicom

# Run with verbose output
python3 -m unittest test_view_maker.py -v
```

### Manual Module Execution

```bash
# Generate tables and views manually
PYTHONPATH=./source python3 ./dent_oip_builder/view_maker.py
PYTHONPATH=./source python3 ./dent_oip_builder/valueset_builder.py
```

## Code Style Guidelines

### Python Style

#### File Organization

- Module docstrings at the top using triple double-quotes (`"""`)
- Standard library imports first
- Third-party imports second
- Local imports last
- Separate import groups with blank lines

#### Example Import Order

```python
import logging
import sys
from pathlib import Path

from pydicom import dcmread
import csv

from conf import html_static_path
```

#### Naming Conventions

- **Functions**: `snake_case` (e.g., `generate_views_in_dicom()`)
- **Variables**: `snake_case` (e.g., `csv_header`, `file_stem`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `PATH_TABLES`, `SYSTEM_TO_CODESCHEMEDESIGNATOR_MAP`)
- **Classes**: `PascalCase` (e.g., `OrthodonticController`)
- **Private functions**: Single underscore prefix for internal helpers

#### Path Handling

- **Always** use `pathlib.Path` for file paths, never string concatenation
- Use `/` operator for path joining: `path / "subdir" / "file.txt"`
- Use `.resolve()` for absolute paths
- Use `.as_uri()` for file URIs
- Use `.as_posix()` for cross-platform path strings

#### String Formatting

- Prefer f-strings for all string formatting: `f"Converting {png} to DICOM"`
- Use triple-quoted strings for multi-line RST/template content
- Use single quotes for short strings, double quotes for longer strings or when containing single quotes

#### Logging

- Use Python's `logging` module, not `print()`
- Configure at module level: `logging.basicConfig(level=logging.INFO)`
- Use appropriate levels: `logging.info()`, `logging.warning()`, `logging.error()`
- Include context in messages: `logging.info(f"Converting {file} to CSV")`

#### Error Handling

- Use try/except for expected errors (e.g., `AttributeError` when view not found)
- Log warnings for non-critical errors: `logging.warning(f"View {png} not found")`
- Use `raise` for unrecoverable errors with descriptive messages
- Handle `FileNotFoundError` gracefully when appropriate

#### Type Hints

- Use type hints for function parameters when clear: `def func(dcm_filename: Path):`
- Not strictly enforced but encouraged for complex functions

#### Functions

- Keep functions focused and single-purpose
- Use nested functions for helpers only used within parent function
- Add docstrings for non-obvious functions (triple-quoted strings)
- Default to 4-space indentation

#### CSV Handling

- Use Python's `csv` module with explicit parameters:

  ```python
  csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  ```

- Always specify `encoding='utf-8'` when opening files
- Use `DictReader` and `DictWriter` for named columns

### reStructuredText (.rst) Style

#### Headings

```rst
Title (H1)
==========

Section (H2)
------------

Subsection (H3)
~~~~~~~~~~~~~~~
```

#### Key Principles

- Only edit `.rst` files in `source/` directory
- Keep to 80-character line width where practical
- Use relative paths for includes and images
- Follow existing patterns in the codebase

### CSV Table Format

#### views.csv Structure

- First two rows are headers
- Row 1: DICOM keyword (e.g., `PatientOrientation`)
- Row 2: DICOM tag (e.g., `(0020,0020)`)
- Use `^` (caret) to separate multiple values in same cell
- First column must be `keyword`

#### codes.csv Structure

- Columns: `keyword`, `code`, `codeset`, `meaning`
- `codeset` values: `SCT` (SNOMED-CT), `DCM` (DICOM), `CS` (Coded String)
- Special row: `__version__` for version tracking

## Project Structure

```
dent-oip/
├── source/              # Sphinx source files (.rst)
│   ├── conf.py         # Sphinx configuration
│   ├── index.rst       # Main entry point
│   ├── Preamble/       # Foreword, scope, references, requirements
│   ├── V1_Orthodontic_Imaging_Profile/  # Volume 1: actors, transactions, process flow
│   ├── V2_Transactions/                  # Volume 2: transaction details
│   ├── V3_07_DICOM/                     # Volume 3: DICOM specifications
│   │   ├── 01_Conventions/
│   │   ├── 02_General_Definitions/
│   │   ├── 03_VL_Photographic_Image_IOD_Definitions/
│   │   └── 04_Module_Definitions/       # Acquisition context, device, etc.
│   ├── V3_Appendix/    # View examples, device examples, definitions
│   ├── tables/         # Input CSV tables
│   │   ├── views.csv   # View definitions
│   │   ├── codes.csv   # Code definitions
│   │   └── generated/  # Auto-generated CSVs (DO NOT EDIT)
│   └── images/         # Auto-generated from submodule (gitignored)
├── gh-pages-root/      # Landing page for GitHub Pages
│   └── index.html     # Root page (DO NOT DELETE - deployed by both workflows)
├── dent_oip_builder/   # Python build scripts
│   ├── view_maker.py   # DICOM generation and RST creation
│   └── valueset_builder.py  # FHIR ValueSet processing
├── modules/            # Git submodules
│   └── orthoviews-linedrawings/  # PNG source images
├── dist/               # Build output (gitignored)
│   ├── html/
│   ├── pdf/
│   └── docx/
└── test/               # Test files
```

## Key Dependencies

- **sphinx**: Documentation generator
- **sphinx-book-theme**: Theme for HTML output
- **docxbuilder**: DOCX generation
- **dicom4ortho==0.3.12**: DICOM file creation (pinned version)
- **pydicom**: DICOM file handling
- **pynetdicom**: DICOM networking
- **fhir.resources**: FHIR ValueSet parsing

## Git Workflow

- **Main branch**: `master` (releases)
- **Development branch**: `develop` (nightly builds)
- Never commit `dist/`, `generated/`, `source/images/`, `.pyc`, `*.log`
- GitHub Actions automatically builds on push to `master` and `develop`

## Common Tasks

### Editing RST Documentation

1. Edit `.rst` files in `source/` directory
2. Follow IHE Profile structure (Preamble, Volume 1, Volume 2, Volume 3, Appendices)
3. Maintain consistent heading hierarchy (see RST Style section)
4. Test locally with `pipenv run make html`
5. Push to `develop` branch for nightly build
6. Push to `master` branch for release build

### Editing Tables

1. Edit `source/tables/views.csv` or `source/tables/codes.csv` (use spreadsheet app)
2. Save as CSV
3. Run `make html` to regenerate

### Adding a New View

1. Add row to `source/tables/views.csv` with all required DICOM tags
2. Ensure all code keywords exist in `source/tables/codes.csv`
3. Add corresponding PNG to `modules/orthoviews-linedrawings/images/png/`
4. Build will auto-generate DICOM, CSV, and RST files

### Debugging Build Issues

- Check `error.log` for Python errors
- Run builders individually: `python3 ./dent_oip_builder/view_maker.py`
- Ensure submodules are initialized: `git submodule update --init`

## Notes for AI Agents

- **Do not modify** generated files in `source/tables/generated/`
- **Do not modify** generated view RST files in `source/V3_Appendix/A_ViewExamples/generated/`
- **Do not delete** `gh-pages-root/index.html` - this is the landing page for GitHub Pages
- **Do not commit** files in `.gitignore`
- **Use pathlib.Path** for all file operations
- **Log operations** using `logging` module
- **Preserve CSV formatting** exactly (especially quotes and delimiters)
- **Test changes** with `make html` before committing
- When editing RST, maintain consistent heading hierarchy and indentation
