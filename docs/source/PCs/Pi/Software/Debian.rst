.. include:: /PCs/Shared/pdf_options_software

.. _rpi_os:

.. |systemType| replace:: Raspberry Pi
.. |chip| replace:: CM4


.. |user| replace:: pi
.. |pswd| replace:: raspberry


|systemType| OS
###############

.. centered:: |systemType| OS User Manual

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual provides users with a quick start guide of Chipsee Raspberry Pi Computer (Abbreviated as RPC) running a |systemType| OS (raspios-debian-buster, raspios-debian-bullseye). Through this manual, users can quickly understand the hardware resources; users can debug |systemType| OS via serial, SSH, and VNC.

.. table::
   :align: center
   :width: 100%

   +----------+-----------+--------+------------------------+
   | Revision |    Date   | Author |   Description          |
   +==========+===========+========+========================+
   |   V2.1   | 2021-04-28| Chipsee| Revision               |
   +----------+-----------+--------+------------------------+
   |   V2.2   | 2023-11-09| Chipsee| Update Supported Boards|
   +----------+-----------+--------+------------------------+

**SUPPORTED BOARDS:**

  * CS10600RA070
  * CS12800RA101
  * CS12720RA4050
  * CS10600RA4070
  * CS10600RA4070P-D
  * CS12800RA4101A
  * CS12800RA4101P
  * CS10768RA4121
  * CS19108RA4133
  * CS10768RA4150
  * CS19108RA4156
  * CS12102RA4170
  * CS12102RA4190
  * CS19108RA4215
  * CS19108RA4236
  * CSRA4BOX


.. _db_pkg_pi_debian:

**PREBUILT IMAGES PACKAGE:**

Below are the links to the prebuilt images for the Raspbian operating system on the various industrial Pi PC's.

+ :download:`Latest system image for Chipsee Industrial Pi products <https://github.com/Chipsee/industrial-pi#latest-system-images>` |br| |br|

.. rubric:: System Features

.. note::

  | Chipsee uses the Raspberry official OS on the product.
  | We add Chipsee hardware drivers to the Raspberry official system.
  | For more information, please refer to `Industrial Pi <https://github.com/Chipsee/industrial-pi>`_.

:pagebreak:`True`

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Images Package to re-flash the system.

Power Supply Unit (PSU) with the appropriate voltages, as follows:

+ These products: CS12720RA4050, CS10600RA070, CS10600RA4070, CS10600RA4070P-D, CSRA4BOX and CS12800RA101 requires a 6V to 36V power adapter. You must provide the power adapter since Chipsee does not ship these products with a power adapter.
+ The CS12800RA4101A RPC needs a 12V power adapter. Chipsee provides the power adapter.
+ The CS12800RA4101P, CS10768RA4121, CS19108RA4133, CS10768RA4150, CS19108RA4156, CS19108RA4215, CS19108RA4236 RPC need 12V to 36V power adapter.

.. include:: Resources/Hardware_Req

Software Requirements
---------------------

* |systemType| OS Prebuilt Images Package (from the link above)
* `7zip <https://www.7-zip.org/download.html>`_
* `XShell <https://xshell.en.softonic.com/>`_ or other terminal emulation software
* `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_
* `BalenaEtcher <https://www.balena.io/etcher/>`_
* :download:`Rpiboot <https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe>`

.. note::

    * If you want to change the system, you need 7zip, a Prebuilt image, balenaEtcher, and rpiboot.
    * You can use Xshell or other terminal emulation software to debug Chipsee Raspberry Pi products in Windows.
    * You can use VNC-Viewer to control Chipsee Raspberry Pi products over Ethernet.


.. note::

    In this documentation, all the commands are executed with ``root`` user privileges.

:pagebreak:`True`

Debug
=====

In this document, we use Xshell to debug the Chipsee Raspberry Pi products. You can also use other tools such as Putty or another terminal emulation software.

.. include:: Resources/Serial_Debug

.. include:: Resources/SSH_Debug

.. include:: Resources/VNC_Debug

:pagebreak:`True`

.. include:: Resources/Download_IMG

:pagebreak:`True`

.. include:: Resources/System_Resource

:pagebreak:`True`

.. include:: Resources/Faq

:pagebreak:`True`

.. include:: /PCs/Shared/support
