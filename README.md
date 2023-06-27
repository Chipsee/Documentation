![Chipsee Logo](https://github.com/iSOLveIT/Documentation/blob/main/docs/source/Media/Chipsee_Logo_Full.png)
## Chipsee Documentation
This documentation repository contains all marketing collateral (manuals, certifications, 3D files, brochures, whitepapers) and custom OS downloads related to the Chipsee products portfolio.

### Industrial Panel & Embedded PCs :

* Powered by Arm® Cortex®
* Powered by Intel
* Powered by Raspberry PI

### Robust Industrial Monitors

* Monitors with Capacitive Touch

### High-performance System on Modules (SOMs)
* Systems on Module


**Note**
* For product-specific software documentation, visit the related product link

## Sphinx-PDF Generate Integration

This PR integrates the Sphinx PDF-Generate plugin with our project's documentation. 

### How to enable PDF generation for an RST file
1. First, you must configure the Sphinx-PDF Generate plugin in the `conf.py` file. For more information on how to configure Sphinx-PDF Generate, refer to the [Quickstart page](https://isolveit.github.io/sphinx-pdf-generate/quickstart.html#quickstart).
2. For every RST file, we set some metadata which the Sphinx-PDF will use Generate plugin. The metadata should be placed at the beginning of the RST file. Below is an example of the metadata to add to your RST file.
```rst
:pdf-title: PIM-101-C
:pdf-subtitle: PN: CS-D101
:pdf-filename: PIM-101-C
:pdf-type: monitors
:pdf-revision: 1.1
```
3.  Next, add the `html-only` class to some directives in your RST file.
```rst
.. rubric:: *Version 1.1*
    :class: html-only

.. You must add `html-only` to the div under the raw directive to hide the div in the PDF output

.. raw:: html

    <div class="row html-only" id="gallery" data-bs-toggle="modal" data-bs-target="#imageModal">
```
4. For the image thumbnails, you can add the `pdf-width-**` (where: ** - a number which is a multiply of 5 but between 5-100) class to the image directive. For example:
```rst
.. image:: /Media/Monitors/PIM-101-C/pim-101-front.png
   :class: product-img img-thumbnail mx-auto d-block pdf-width-70
   :alt: Front View
```
6. You can use the **:pagebreak:`True`** role provided by the Sphinx-PDF Generate plugin which allows you to add page breaks between the generated PDF output.
7. When editing a single RST file, you can use the [debug](https://isolveit.github.io/sphinx-pdf-generate/options.html#pdfgen-debug-for-development-purposes-only) and [debug_target](https://isolveit.github.io/sphinx-pdf-generate/options.html#pdfgen-debug-target-for-development-purposes-only) options to help you debug the PDF generated for that RST file.

**Note**:  The size of a product image shouldn't be > 1.5mb.

Resources on how to use the Sphinx PDF-Generate plugin:
- Docs -  https://isolveit.github.io/sphinx-pdf-generate/