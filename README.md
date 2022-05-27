# ADA-1107

These are the source files for the ADA-1107 standard document. You can find the built versions here:

- [HTML build](http://brillig.org/~afm/ada-1107/html/index.html)
- [docx build](http://brillig.org/~afm/ada-1107/docx/ADA-1107.docx)


Source files located in `source/`.

Builds located in `dist/`.

[Sphinx](https://www.sphinx-doc.org/) is the tool used to build these files into
HTML, PDF, etc. Sphinx uses the reStructuredText language.

A development build of the document is available
[here](http://brillig.org/~afm/ada-1107/html/)

## Known Issues

There is a potential problem with the SQL script: apparently while it works fine
with Python 3.10 and sqlite 3.37, the script bonks with an SQL error when around
FROM clause. See PANIO-227.

## Editing

Whoever is willing to make content contributions to the document is considered
an editor.

### Editing Tables

To make modifications to the tables, edit the files in `source/tables/*.csv` (a spreadsheet will make this easy) then save back in CSV format.

For more information on how this process works, see section View Tables Generation below.

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
