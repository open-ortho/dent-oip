## Building

### Requirements

#### xslTNG

- Download the xslTNG style sheet from github. Don't clone the repository, just
get the [latest release from the release
page](https://github.com/docbook/xslTNG/releases). 
- unpack the zip file somewhere of your choosing. I placed them in a subfolder
here called `resources/`.
- modify the `make.sh` file to make sure the `$DOCBOOK_XSLTNG` is pointing to
the correct path.

#### docbook DTD and XSD

- install the `docbook` package with the package manager, like:

    brew install dockbook

#### pandoc

Install pandoc with the package manager, like:

    brew install pandoc

