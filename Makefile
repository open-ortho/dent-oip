# Minimal makefile for Sphinx documentation
#


VIEWSDB = views.db
GENERATED_TABLES = source/tables/generated

PIPENV = python3 -m pipenv
VIEWBUILDER = $(PIPENV) run python3 ./view_maker.py


# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= $(PIPENV) run sphinx-build
SOURCEDIR     = source
BUILDDIR      = dist/

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
	rm -rf "$(BUILDDIR)" "$(GENERATED_TABLES)"
	rm -f "$(VIEWSDB)" 

deploy: html docx
	cp htaccess "$(BUILDDIR)/.htaccess"
	cp htpasswd "$(BUILDDIR)/.htpasswd"
	ssh -p $(SSH_PORT) $(SSH_USER)@$(SSH_IP) "mkdir -p $(REMOTE_PATH)"
	rsync -auv -e "ssh -p $(SSH_PORT)" --delete "$(BUILDDIR)" "$(DESTDIR)"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile genereted_tables
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
