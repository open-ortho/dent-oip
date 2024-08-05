OS := $(shell uname -s)
DATESTAMP := $(shell date -u +"%Y%m%d%H%M%S")
VERSION := $(shell cat VERSION)
NIGHTLY_VERSION := $(VERSION)-nightly.$(DATESTAMP)

# In Windows, calling python3 will default to the system path. But regular python will pick up the path of the python inside the virtual environment. This might not be the case for 
ifeq ($(OS), Darwin)
	PYTHON=python3
	CUT=gcut
	LIBREOFFICE=/Applications/LibreOffice.app/Contents/MacOS/soffice
else
	OS := $(shell uname -o)
	ifeq ($(OS), Msys)
		PYTHON=python
		CUT=cut
	else ifeq ($(OS), GNU/Linux)
		PYTHON=python3
		CUT=cut
		LIBREOFFICE=libreoffice
	endif
endif

BUILDDIR      = ./dist
GENERATED_TABLES = source/tables/generated
SAMPLE_DICOM_FILES = source/_static/dicom_samples
VIEW_EXAMPLES = source/Appendix/ViewExamples
IMAGES = source/images
IMAGES_ORIGIN = modules/orthoviews-linedrawings/images/png

PIPENV = $(PYTHON) -m pipenv
# PIPENV_RUN = $(PIPENV) run
VIEWBUILDER = $(PIPENV_RUN) $(PYTHON) ./view_maker.py

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= $(PIPENV_RUN) sphinx-build
SOURCEDIR     = source
VERSION_FILE  = $(SOURCEDIR)/_VERSION

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile deploy genereted_tables dist

# This will get executed automatically for each target routed to Sphinx. See catchall target below.
$(GENERATED_TABLES): $(IMAGES)
	$(VIEWBUILDER)

clean:
	rm -rf "$(BUILDDIR)" "$(GENERATED_TABLES)" "$(IMAGES)" "$(VIEW_EXAMPLES)/generated" "$(SAMPLE_DICOM_FILES)" "$(VERSION_FILE)"

deploy:
	cp VERSION $(VERSION_FILE)
	$(MAKE) dist

git-tag:
	git tag $(shell cat $(VERSION_FILE))
	git push --tags

# Don't run locally, will change rst files. Intended for github actions only.
nightly:
	printf "%s" $(NIGHTLY_VERSION) > $(VERSION_FILE)
	sed -i "s|RELEASE_TAG_PLACEHOLDER|$(NIGHTLY_VERSION)|g" ./source/index.rst
	sed -i "s|DENT-OIP.docx|nightly-DENT-OIP.docx|g" ./source/index.rst
	sed -i "s|DENT-OIP.pdf|nightly-DENT-OIP.pdf|g" ./source/index.rst

	$(MAKE) dist git-tag
	cp ./source/tables/views.csv $(BUILDDIR)/nightly-views.csv
	cp ./source/tables/codes.csv $(BUILDDIR)/nightly-codes.csv
	mv $(BUILDDIR)/docx/DENT-OIP.docx $(BUILDDIR)/docx/nightly-DENT-OIP.docx
	mv $(BUILDDIR)/pdf/DENT-OIP.pdf $(BUILDDIR)/pdf/nightly-DENT-OIP.pdf


dist: html docx pdf

$(IMAGES):
	git submodule init
	git submodule update
	mkdir -p "$(IMAGES)"
	cd $(IMAGES_ORIGIN) && for image in $$(ls); do cp -v $${image:?} $${OLDPWD}/$(IMAGES)/$$(echo $${image} | $(CUT) --characters='1-5' | sed 's/-//').png; done

.PHONY: pre_requisites
pre_requisites: $(SAMPLE_DICOM_FILES)

$(SAMPLE_DICOM_FILES): $(GENERATED_TABLES)
	mkdir -p $@
	mv -v $(IMAGES)/*.dcm $@

# both using latexpdf and sphinx -b pdf proved to be unstable. Too much maintenance. Resorting to LibreOffice.
pdf: docx
	mkdir -p $(BUILDDIR)/pdf/
	$(LIBREOFFICE) --headless --convert-to pdf --outdir $(BUILDDIR)/pdf/ $(BUILDDIR)/docx/*.docx

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile $(SAMPLE_DICOM_FILES) 
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
