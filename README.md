# ADA-1107

These are the souce files for the ADA-1107 standard document.

Sourcefiles located in `source/`.

Builds located in `dist/`.

Sphinx is the tool used to build these files into HTML, PDF, etc. Sphinx uses
the restructured text language.

## Editing

### Using GitHub

If you are an editor, you can edit the document from within the `source/`
directory. The document contents are in the files with extension `.rst` which
stands for restructured text. [You can find a primer
here.](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

You do not need to worry about any other file which does _not_ have an `.rst` extension.

You can use the GitHub interface, to make modifications to the file by clicking
the pencil botton on the top right of the file, after you have opened it (by
clicking on the file you want to edit).

Saving in git is called "committing". So when you want to save, you add
commments to what you have changed on the bottom, then click on Commit.

### Not a git-lover?

If you don't feel like learning how git works (understandable), you can edit the
documents any way you like, then send them to Toni for the merging. You can copy
and paste the page as it appears in git in your own editor of choice, say word
or LibreOffice, then make modifcations, and when done, you can send Toni the
.docx file, which he can then convert back to .rst.

## Building

Build is managed with `make` and targets are in `Makefile`.

This project makes use of Sphinx to build the documentation. All documents are
in reStructeredText and conversion is used using sphinx tools. An installation
of Python and Sphinx is therefore required.

In a UNIX environment with Python and pipenv installed, the following should
suffice to build the html version of this document.

    pipenv install
    pipenv run make html

## Deployment

Deployment is done with

    pipenv run make deploy

Deployment currently configured in `Makefile` to use rsync. You will need to
customize, or gain access to deployment server to deploy.

Deployment also deploys an `.htaccess` and `.htpasswd` file with loose security.
Username and password both are `scdi116`.