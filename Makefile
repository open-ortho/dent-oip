OS := $(shell uname -s)
DATESTAMP := $(shell date -u +"%Y%m%d%H%M%S")
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

BUILDDIR      = dist/
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

.PHONY: help Makefile deploy genereted_tables

# This will get executed automatically for each target routed to Sphinx. See catchall target below.
$(GENERATED_TABLES): $(IMAGES)
	$(VIEWBUILDER)

clean:
	rm -rf "$(BUILDDIR)" "$(GENERATED_TABLES)" "$(IMAGES)" "$(VIEW_EXAMPLES)/generated" "$(SAMPLE_DICOM_FILES)" "$(VERSION_FILE)"

deploy:
	cp VERSION $(VERSION_FILE)
	$(MAKE) _deploy

git-tag:
	git tag $(shell cat $(VERSION_FILE))
	git push --tags

nightly:
	printf "%s-nightly.$(DATESTAMP)" $(shell cat VERSION) > $(VERSION_FILE)
	$(MAKE) _deploy git-tag

_deploy: html docx latexpdf 

$(IMAGES):
	git submodule init
	git submodule update
	mkdir -p "$(IMAGES)"
	cd $(IMAGES_ORIGIN) && for image in $$(ls); do cp -v $${image:?} $${OLDPWD}/$(IMAGES)/$$(echo $${image} | $(CUT) --characters='1-5' | sed 's/-//').png; done

$(SAMPLE_DICOM_FILES): $(GENERATED_TABLES)
	mkdir -p $@
	mv -v $(IMAGES)/*.dcm $@

pdf: docx
	mkdir -p $(BUILDDIR)/pdf/
	$(LIBREOFFICE) --headless --convert-to pdf --outdir $(BUILDDIR)/pdf/ $(BUILDDIR)/docx/*.docx

# override the latexpdf target to launch ignoring errors with the - as prefix.
.PHONY: _latexpdf
_latexpdf:
	-$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	-$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile $(SAMPLE_DICOM_FILES) 
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
