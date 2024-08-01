# ADA-1107 v0.1.0

These are the source files for the ADA-1107 standard document. You can find the nightly [nightly builds here](http://brillig.org/~afm/ada-1107/html/index.html). Username: `scdi116` Password: `scdi116`.

Source files located in `source/`.

Builds located in `dist/`.

[Sphinx](https://www.sphinx-doc.org/) is the tool used to build these files into
HTML, PDF, etc. Sphinx uses the reStructuredText language.


## Requirements

* Python3: the whole thing runs in Python3
* orthoviews-linedrawings: all the line drawings which represent the orthodontic views, come from these line drawings. They are also used to create the DICOM sample files.
* dicom4ortho: used to generate the DICOM files. The orthoviews-linedrawings are used as `PixelValue`.
* pynetdicom: used to convert the DICOM files into tables for the example views in the appendix section of this document.

## Editing

Whoever is willing to make content contributions to the document is considered
an editor.

### Editing Tables

To make modifications to the tables, edit the files in `source/tables/*.csv` (a spreadsheet will make this easy) then save back in CSV format.

- The `views.csv` file, contains all views and their codes.
- The codes used in `views.csv` are referred to using keywords.
- The keywords used must match those expressed in `codes.csv`.

For more information on how this process works, see section View Tables Generation below.

#### views.csv format

- First two rows are header rows
- First row contains the DICOM keyword for the DICOM tag.
- Second row contains the DICOM tag number.
- _AcquisitonContextSequence_ has various columns, one for each concept name.
- The first row of the _AcquisitionContextSequence_ column has the format `AcquisitionContextSequnce^[concept name]`, where `[concept name]` is the keyword for the code that goes in _Concept Name Code Sequence Attribute (0040,A043)_.
- The second row of the _AcquisitionContextSequence_ columns are always `(0040,0555)`.
- The subsequent rows of the _AcquisitionContextSequence_ column contain the keyword for the concept value.
- If more than one concept name/concept value pairs is required, multiple concepts value keywords are entered in the same cell, separated by the caret `^` character.

#### codes.csv format

- The _codeset_ column contains the abbreviation for the codeset used, i.e. `SCT` for SNOMED-CT, `DCM` for DICOM.
- The codes which are not part of a real codeset and are considered CS (Coded String) in DICOM, have `CS` in the _codeset_ column.

### Using GitHub

Editors can edit the document from within the `source/` directory. The document
content is only in files with extension `.rst`, which stands for restructured
text. [a primer
here.](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

Editors should only be concerned with files with an `.rst` extension and do not
need to worry about any other file.

To make modifications using the GitHub interface, the editor can click the
pencil on the top right of the screen, after having clicked on the file to edit.

Saving in git is called "committing". When it is time to save, the editor should
add comments describing what has changed (on the bottom of the screen) before
clicking on Commit.

### Not a git-lover?

If you don't feel like learning how git works (understandable), editing the
documents can be done any way then sent Toni for the merging. 

For example, copy the page as it appears here in GitHub and paste it in your own
editor of choice, (MS-Word, Pages, Google Docs, LibreOffice, etc), then make
modifications. When done, send Toni the .docx file, which he can then convert
back to `.rst`.

You can also work off of the [docx
build](http://brillig.org/~afm/ada-1107/docx/ADA-1107.docx). When doing so, make
strict use of heading formatting to divide sections and paragraphs, and do not
worry about any formatting: this will facilitate merging the modifications back
in `.rst`.

## Building

Build is managed with `make` and targets are in `Makefile`.

This project makes use of Sphinx to build the documentation. All documents are
in a text format called _reStructuredText_ and conversion to other formats (like
HTML, PDF or .docx) is used using `sphinx` tools. An installation of Python and
[Sphinx](https://www.sphinx-doc.org/) is therefore required.

In a UNIX environment with Python and `pipenv` installed, the following should
suffice to build the `html` version of this document.

    pipenv install
    pipenv run make html

### Building on Ubuntu/Debian

This section wasn't required until recently the latexpdf target stopped working on my machine. I still haven't figured out the steps to fix.

    sudo apt install texlive



### Building on macOS

The `Makefile` makes use of gnu cut. You need to install `brew install coreutils`, then replace the `cut` instance in `Makefile` with `gcut`.

To build the PDF, you will need LaTeX. 

        brew install basictex
        sudo tlmgr update --self
        sudo tlmgr install latexmk tex-gyre fncychap wrapfig capt-of framed needspace tabulary varwidth titlesec

## Deployment

Deployment is done with

    pipenv run make deploy

Deployment currently configured in `Makefile` to use rsync. You will need to
customize, or gain access to deployment server to deploy.

Deployment also deploys an `.htaccess` and `.htpasswd` file with loose security.
Both username and password are `scdi116`.

## View Tables Generation

The CSV files in `source/tables/*.csv` are used to automatically generate another set of CSV files located in `source/tables/generated/*.csv`. The final tables in the appendices are built from CSV files `source/tables/generated/*.csv`. 

`view_maker.py` contains instructions to 

- import the `source/tables/generated/*.csv` into an SQLite database
- build the tables into a `_temp` table, looping row by row with a large SQL command.

The temp tables are then exported into CSV in the `generated` folder. And that's where the RestructuredText files refer to.

This process is very inefficient, but optimization is not needed since execution is only done once at build time.

## Image generation

The images of the tables in the appendix are imported automatically by `make` from the `open-ortho/orthoviews-linedrawings` GitHub repository, which is a submodule of this repository. You will therefore find  the `sources/images` folder excluded from `.gitignore`.