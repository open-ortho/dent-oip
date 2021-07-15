# ADA-1107

These are the souce files for the ADA-1107 standard document.

## Building

This project makes use of Sphinx to build the documentation. All documents are
in reStructeredText and conversion is used using sphinx tools.

In a UNIX environment with Python and pipenv installed, the following should
suffice to build the html version of this document.

    pipenv install
    pipenv run make html
