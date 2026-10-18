PROJECT = docs
SOURCEDIR = $(PROJECT)/source
BUILDDIR = $(PROJECT)/build
VENV = . venv/bin/activate

.PHONY: help clean html rebuild watch pull-specs pdf

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build output"
	@echo "  html      - Build HTML documentation once"
	@echo "  rebuild   - Clean and rebuild everything"
	@echo "  watch     - Auto-build and serve with sphinx-autobuild"
	@echo "  pull-specs - Pull product specs from the website into docs/source/_data/specs"
	@echo "  pdf       - Build HTML, then the PDF manuals that changed"

clean:
	rm -rf $(BUILDDIR)/*

html:
	@echo "Building HTML with virtualenv..."
	$(VENV) && sphinx-build -b html $(SOURCEDIR) $(BUILDDIR)/html -E -a -j auto -W --keep-going

rebuild: clean html

watch:
	@echo "Starting live auto-build with sphinx-autobuild..."
	$(VENV) && sphinx-autobuild --host 0.0.0.0 --port 8000 $(SOURCEDIR) $(BUILDDIR)/html -j 8

pull-specs:
	$(VENV) && python tools/pull_specs.py --summary -

pdf: html
	$(VENV) && python tools/build_pdfs.py $(BUILDDIR)/html
