#!/bin/sh

NAME="TR-1107"
MAIN="docbook/${NAME}.xml"
DIST="./dist"


LINTER="$(which xmllint)" || {
    echo "Cannot find xmllint. Install first."
    exit 1
}
PANDOC="$(which pandoc)" || {
    echo "Cannot find pandoc. Install first"
    exit 1
}
DOCBOOK_XSD="/usr/local/Cellar/docbook/5.1_1/docbook/xml/5.0/xsd/docbook.xsd"
DOCBOOK_XSL=""
DOCBOOK_DTD="/usr/local/Cellar/docbook/5.1_1/docbook/xml/5.0/dtd/docbook.dtd"

print_help() {
    echo
    echo "Available commands:"
    echo "  clean   : Remove dist/ folders for modules"
    echo "  build   : Builds distribution packages in dist/"
    echo "  all     : clean then build"
    echo
}

lint() {
    if [ ! -f "$DOCBOOK_DTD" ]; then
        echo "Can't find XML definition file $DOCBOOK_DTD. Please install first."
        exit 1
    fi

    # According to http://www.sagehill.net/docbookxsl/ValidXinclude.html
    # $LINTER --noout --xinclude --postvalid --noent --dtdvalid "$DOCBOOK_DTD" "${MAIN}"
    $LINTER --noout --xinclude --postvalid --noent --schema "$DOCBOOK_XSD" --dtdvalid "$DOCBOOK_DTD" "${MAIN}"
}

make_pdf() {
    $LINTER --xinclude "${MAIN}" | $PANDOC --from="docbook" --to="pdf" --output="${DIST}/${NAME}.pdf"
    echo "Build PDF."
}

make_docx() {
    $LINTER --xinclude "${MAIN}" | $PANDOC --from="docbook" --to="docx" --output="${DIST}/${NAME}.docx"
    echo "Build DOCX."
}

make_html() {
    $LINTER --xinclude "${MAIN}" | $PANDOC --from="docbook" --to="html" --output="${DIST}/${NAME}.html"
    echo "Build HTML."
}

make_txt() {
    $LINTER --xinclude "${MAIN}" | $PANDOC --from="docbook" --to="plain" --output="${DIST}/${NAME}.txt"
    echo "Build TXT."
}

make_rtf() {
    $LINTER --xinclude "${MAIN}" | $PANDOC --from="docbook" --to="rtf" --output="${DIST}/${NAME}.rtf"
    echo "Build RTF."
}

clean() {
    rm -rf "${DIST}" || exit
    echo "Cleaned up ${DIST} folder."
}

build() {
    mkdir ${DIST} 2> /dev/null
    lint || exit
    make_docx || exit
    make_pdf || exit
    make_html || exit
    make_rtf || exit
    make_txt || exit
}

all() {
    clean || exit
    build || exit
}

case $1 in
clean)
    clean
    exit
    ;;
build)
    build
    exit
    ;;
all)
    clean || exit
    build || exit
    exit
    ;;
*) # Default case: If no more options then break out of the loop.
    print_help ;;
esac

# Rest of the program here.
