# Minimal makefile for Sphinx documentation
#


BUILDDIR      = dist/
GENERATED_TABLES = source/tables/generated
SAMPLE_DICOM_FILES = source/_static/dicom_samples
VIEW_EXAMPLES = source/Appendix/ViewExamples
IMAGES = source/images
IMAGES_ORIGIN = modules/orthoviews-linedrawings/images/png

# In Windows, calling python3 will default to the system path. But regular python will pick up the path of the python inside the virtual environment. This might not be the case for 
ifeq ($(OS), Windows_NT)
	PYTHON=python
else
	PYTHON=python3
endif

PIPENV = $(PYTHON) -m pipenv
# PIPENV_RUN = $(PIPENV) run
VIEWBUILDER = $(PIPENV_RUN) $(PYTHON) ./view_maker.py

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= $(PIPENV_RUN) sphinx-build
SOURCEDIR     = source

SSH_USER			= afm
SSH_IP				= brillig.org
REMOTE_PATH			= public_html/ada-1107/
SSH_PORT			= 22

DESTDIR = $(SSH_USER)@$(SSH_IP):$(REMOTE_PATH)
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile deploy genereted_tables

# This will get executed automatically for each target routed to Sphinx. See catchall target below.
$(GENERATED_TABLES): $(IMAGES)
	$(VIEWBUILDER)

clean:
	rm -rf "$(BUILDDIR)" "$(GENERATED_TABLES)" "$(IMAGES)" "$(VIEW_EXAMPLES)/generated" "$(SAMPLE_DICOM_FILES)"

deploy: html docx latexpdf 
	cp htaccess "$(BUILDDIR)/.htaccess"
	cp htpasswd "$(BUILDDIR)/.htpasswd"
	ssh -p $(SSH_PORT) $(SSH_USER)@$(SSH_IP) "mkdir -p $(REMOTE_PATH)"
	rsync -auv -e "ssh -p $(SSH_PORT)" --delete "$(BUILDDIR)" "$(DESTDIR)"

$(IMAGES):
	git submodule init
	git submodule update
	mkdir -p "$(IMAGES)"
	cd $(IMAGES_ORIGIN) && for image in $$(ls); do cp -v $${image:?} $${OLDPWD}/$(IMAGES)/$$(echo $${image} | cut --characters='1-5' | sed 's/-//').png; done

$(SAMPLE_DICOM_FILES): $(GENERATED_TABLES)
	mkdir -p $@
	mv -v $(IMAGES)/*.dcm $@


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile $(SAMPLE_DICOM_FILES) 
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
