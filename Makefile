# Minimal makefile for Sphinx documentation
#


BUILDDIR      = dist/
VIEWSDB = views.db
GENERATED_TABLES = source/tables/generated
INTRAORAL_VIEWS = source/Appendix/intraoral_views.rst
EXTRAORAL_VIEWS = source/Appendix/extraoral_views.rst
IMAGES = source/images
IMAGES_ORIGIN = modules/orthoviews-linedrawings/images/png

PIPENV = python3 -m pipenv
VIEWBUILDER = $(PIPENV) run python3 ./view_maker.py


# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= $(PIPENV) run sphinx-build
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
genereted_tables:
	rm -f $(VIEWSDB)
	$(VIEWBUILDER)
	rm $(VIEWSDB) 

clean:
	rm -rf "$(BUILDDIR)" "$(GENERATED_TABLES)" "$(IMAGES)"
	rm -f "$(VIEWSDB)" "$(INTRAORAL_VIEWS)" "$(EXTRAORAL_VIEWS)"

deploy: html docx latexpdf 
	cp htaccess "$(BUILDDIR)/.htaccess"
	cp htpasswd "$(BUILDDIR)/.htpasswd"
	ssh -p $(SSH_PORT) $(SSH_USER)@$(SSH_IP) "mkdir -p $(REMOTE_PATH)"
	rsync -auv -e "ssh -p $(SSH_PORT)" --delete "$(BUILDDIR)" "$(DESTDIR)"

$(IMAGES):
	git submodule init
	git submodule update
	mkdir -p "$(IMAGES)"
	cd $(IMAGES_ORIGIN) && for image in $$(ls); do cp -v $${image:?} $${OLDPWD}/$(IMAGES)/$$(echo $${image} | gcut --characters='1-5').png; done

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile $(IMAGES) genereted_tables 
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
