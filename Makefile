PROJECT = docs
SOURCEDIR = $(PROJECT)/source
BUILDDIR = $(PROJECT)/build
VENV = . venv/bin/activate

.PHONY: help clean html rebuild watch

help:
	@echo "Available targets:"
	@echo "  clean     - Remove build output"
	@echo "  html      - Build HTML documentation once"
	@echo "  rebuild   - Clean and rebuild everything"
	@echo "  watch     - Auto-build and serve with sphinx-autobuild"

clean:
	rm -rf $(BUILDDIR)/*

html:
	@echo "Building HTML with virtualenv..."
	$(VENV) && sphinx-build -b html $(SOURCEDIR) $(BUILDDIR)/html -E -a -j auto

rebuild: clean html

watch:
	@echo "Starting live auto-build with sphinx-autobuild..."
	$(VENV) && sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html -j 8
