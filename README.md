# ADA-1107

These are the souce files for the ADA-1107 standard document.

Sourcefiles located in `source/`.

Builds located in `dist/`.

## Building

Build is managed with `make` and targets are in `Makefile`.

This project makes use of Sphinx to build the documentation. All documents are
in reStructeredText and conversion is used using sphinx tools. An installation
of Python and Sphinx is therefore required.

In a UNIX environment with Python and pipenv installed, the following should
suffice to build the html version of this document.

    pipenv install
    pipenv run make html
