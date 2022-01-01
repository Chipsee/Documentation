.. |systemType| replace:: Debian 10 (buster)
.. |user| replace:: pi
.. |pswd| replace:: raspberry


|systemType| OS
###############

.. centered:: |systemType| OS User Manual

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual provides users with a fast guide of Chipsee Raspberry Pi Computer (Abbreviated as RPC) running a |systemType| OS. Through this manual, users can quickly understand the hardware resources; users can debug |systemType| OS via serial, SSH, and VNC.

.. table::
   :align: center
   :width: 100%

   +----------+-----------+--------+-----------------+
   | Revision |    Date   | Author |   Description   |
   +==========+===========+========+=================+
   |   V2.1   | 2021-04-28| Chipsee| Revision        |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

   *CS10600RA4070*   *CS10600RA070*   *CS12800RA101*   *CS12800RA4101A*   *CS19108RA4156A*

.. _db_pkg_pi_debian:

**PREBUILT IMAGES PACKAGE:**

Below are the links to the prebuilt images for the Raspbian Buster operating system on the various industrial Pi PC's.

+ :download:`Raspbian Buster with desktop and recommended software <https://chipsee-tmp.s3.amazonaws.com/RaspberryPi/20200213/2020-02-13-raspbian-buster-full-chipsee.img.xz>`
+ :download:`Raspbian Buster with desktop and recommended software V2 <https://chipsee-tmp.s3.amazonaws.com/RaspberryPi/20200213/2020-02-13-raspbian-buster-full-chipsee-v2.img.xz>`
+ :download:`Raspbian Buster with desktop and recommended software V3 <https://chipsee-tmp.s3.amazonaws.com/RaspberryPi/20200213/2020-02-13-raspbian-buster-full-chipsee-v3.img.xz>` |br| |br|
+ :download:`Raspbian Buster with desktop <https://chipsee-tmp.s3.amazonaws.com/RaspberryPi/20200213/2020-02-13-raspbian-buster-chipsee.img.xz>`
+ :download:`Raspbian Buster with desktop V2 <https://chipsee-tmp.s3.amazonaws.com/RaspberryPi/20200213/2020-02-13-raspbian-buster-chipsee-v2.img.xz>` |br| |br|
+ :download:`Raspbian Buster Lite <https://chipsee-tmp.s3.amazonaws.com/RaspberryPi/20200213/2020-02-13-raspbian-buster-lite-chipsee.img.xz>`
+ :download:`Raspbian Buster Lite V2 <https://chipsee-tmp.s3.amazonaws.com/RaspberryPi/20200213/2020-02-13-raspbian-buster-lite-chipsee-v2.img.xz>` |br| |br|


.. rubric:: System Features

.. table::
   :align: center
   :width: 100%

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | Kernel        | Kernel 5.4.79                    |
   +---------------+----------------------------------+
   | System\ [#d]_ | Based on raspios 2020-12-02      |
   +---------------+----------------------------------+
   | Python        | Python 2.7.16 / Python 3.7.3     |
   +---------------+----------------------------------+
   | Qt            | Needs to be installed by the user|
   +---------------+----------------------------------+
   | GCC           | 8.3.0                            |
   +---------------+----------------------------------+
   | Debian Version| Debian 10 (Buster)               |
   +---------------+----------------------------------+
   | User/Password | [pi/raspberry]                   |
   +---------------+----------------------------------+

-----

.. [#d] Chipsee uses the Raspberry official OS on the product. We add Chipsee hardware drivers to the Raspberry official system. For more information, please refer to `Industrial Pi <https://github.com/Chipsee/industrial-pi>`_.

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Images Package to re-flash the system.

Power Supply Unit (PSU) with the appropriate voltages, as follows:

+ These products: CS10600RA070, CS10600RA4070, and CS12800RA101 requires a 6V to 36V power adapter. You must provide the power adapter since Chipsee does not ship these products with a power adapter.
+ The CS12800RA4101 RPC needs a 12V power adapter. Chipsee provides the power adapter.

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

Debug
=====

In this document, we use Xshell to debug the Chipsee Raspberry Pi products. You can also use other tools such as Putty or another terminal emulation software.

.. include:: Resources/Serial_Debug

.. include:: Resources/SSH_Debug

.. include:: Resources/VNC_Debug

.. include:: Resources/Download_IMG

.. include:: Resources/System_Resource

.. include:: Resources/support
