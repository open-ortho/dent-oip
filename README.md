# Dentistry - Orthodontic Imaging Technical Implementation Profile

Version: DENT-OIP v0.2.7

These are the source files for the DENT-OIP standard document.

- [DENT-OIP latest release](http://open-ortho.org/dent-oip/release/index.html)
- [DENT-OIP nightly build](http://open-ortho.org/dent-oip/nightly/index.html)

Source files located in `source/`.

Builds located in `dist/`.

[Sphinx](https://www.sphinx-doc.org/) is the tool used to build these files into HTML, PDF, etc. Sphinx uses the reStructuredText language.


## Requirements

* Python3: the whole thing runs in Python3
* orthoviews-linedrawings: all the line drawings which represent the orthodontic views, come from these line drawings. They are also used to create the DICOM sample files.
* dicom4ortho: used to generate the DICOM files. The orthoviews-linedrawings are used as `PixelValue`.
* pynetdicom: used to convert the DICOM files into tables for the example views in the appendix section of this document.

## Editing

Whoever is willing to make content contributions to the document is considered an editor.

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

#### Viewset layout CSV format

The files in `source/tables/viewset_layouts/` are the source of truth for the
normative viewset geometry and the generated normalized-layout diagrams.
`geometry.csv` defines dimensions shared by every viewset. Each viewset also
has an arrangement file named `<viewset>.csv`, such as `VS-04.csv`.

These CSV files are used in two places:

- Volume 2 includes the CSV files as normative geometry and arrangement tables.
- `dent_oip_builder/viewset_layout_maker.py` reads it to generate the SVG
  diagram used in Appendix B.

This prevents the dimensions stated in the document from diverging from the
diagram.

`geometry.csv` contains the fixed inputs from which the generator calculates
the box dimensions and complete layouts. ADA 1100 does not prescribe numeric
margin or gap dimensions; it requires spacing that aids visualization without
interfering with the images. The values in `geometry.csv` were calculated from
the example graphics in ADA 1100, which in turn were based on commonly used
American Board of Orthodontics (ABO) case presentations and existing
commercially produced presentations. The reference width of `1000` is an
arbitrary scale-independent unit used to express those measured proportions.

`geometry.csv` uses `Parameter` and `Value` columns. Its parameters are:

| Parameter | Meaning |
| --- | --- |
| `Reference Viewset` | Viewset used to establish the common physical box width. This is VS-01. |
| `Reference Layout Width` | Width assigned to the reference layout in arbitrary scale-independent units. |
| `Horizontal Margin` | Common left and right margin in reference-layout units. |
| `Vertical Margin` | Common top and bottom margin in reference-layout units. |
| `Horizontal Gap` | Common gap between boxes in reference-layout units. |
| `Vertical Gap` | Common gap between rows in reference-layout units. |
| `<Row Type> Box Width:Height` | Physical box proportion for the `Top`, `Middle`, or `Bottom` row type. |

The viewset arrangement CSVs define physical rows from top to bottom:

| Column | Meaning |
| --- | --- |
| `Row` | One-based physical row number, from top to bottom. |
| `Row Type` | `Top`, `Middle`, or `Bottom`; selects the corresponding common box proportion. A viewset may repeat a row type. |
| `Boxes` | Number of boxes in the row. All boxes in all viewsets have the common physical box width. |
| `First ILC` | Image Location Code assigned to the leftmost box. Following boxes are numbered consecutively. |

All dimensions are scale-independent. Calling them pixels is convenient when
reasoning about the layout, but the resulting SVG can be rendered at any size.

From these fixed inputs, the generator calculates each layout as follows:

1. Calculate the common box width from the VS-01 reference width, its three
   columns, and the common horizontal margins and gaps.
2. Calculate the three box heights from that width and the common top, middle,
   and bottom width-to-height ratios.
3. Assemble each viewset in common physical units using its row arrangement.
4. Center rows with fewer boxes under the widest row.
5. Count the resulting physical width and height of the complete layout.
6. Normalize every corner coordinate independently to that layout's calculated
   width and height, and print it to three decimal places in the SVG.

The box dimensions, margins, gaps, and text sizes therefore stay proportional
across all diagrams. A viewset with more columns becomes physically wider
before normalization instead of shrinking its boxes or enlarging its padding.

Do not edit files in `source/images-static/generated/`. They are ignored by
Git and recreated during every Makefile build target by:

```bash
python3 dent_oip_builder/viewset_layout_maker.py
```

The canonical generated format is SVG so that dimensions remain precise at any
output resolution. Sphinx copies the SVG into the HTML build. Other formats,
such as PNG for a word-processing workflow, should be derived from the generated
SVG rather than maintained as separate drawings.

Run the focused generator tests with:

```bash
python3 -m unittest test_viewset_layout_maker.py -v
```

The tests validate the calculated proportions and normalized coordinates and
confirm that the output is valid SVG with coordinate-corner markers.

### Using GitHub

Editors can edit the document from within the `source/` directory. The document content is only in files with extension `.rst`, which stands for restructured text. [a primer here.](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

Editors should only be concerned with files with an `.rst` extension and do not need to worry about any other file.

To make modifications using the GitHub interface, the editor can click the pencil on the top right of the screen, after having clicked on the file to edit.

Saving in git is called "committing". When it is time to save, the editor should add comments describing what has changed (on the bottom of the screen) before clicking on Commit.

### Not a git-lover?

If you don't feel like learning how git works (understandable), editing the documents can be done any way then sent Toni for the merging. 

For example, copy the page as it appears here in GitHub and paste it in your own editor of choice, (MS-Word, Pages, Google Docs, LibreOffice, etc), then make modifications. When done, send Toni the .docx file, which he can then convert back to `.rst`.

You can also work off of the docx build: you can find a link to it on the first page of the released HTML document: [here](http://open-ortho.org/dent-oip/release/index.html) . When doing so, make strict use of heading formatting to divide sections and paragraphs, and do not worry about any formatting: this will facilitate merging the modifications back
in `.rst`.

## Building

Build is managed with `make` and targets are in `Makefile`. Building is taken care of by Github using Github Actions. See `.github/workflows/`.

This project makes use of Sphinx to build the documentation. All documents are in a text format called _reStructuredText_ and conversion to other formats (like HTML, PDF or .docx) is used using `sphinx` tools. An installation of Python and [Sphinx](https://www.sphinx-doc.org/) is therefore required.

In a UNIX environment with Python and `pipenv` installed, the following should suffice to build the `html` version of this document.

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
