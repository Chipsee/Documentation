.. |systemType| replace:: Linux Qt 5.5

|systemType| OS
###############

.. centered:: Chipsee |systemType| OS User Manual

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual provides users with a fast guide of Chipsee Industrial Computer (Abbreviate as IPC) about |systemType| OS development. Through this manual, users can quickly understand the hardware resources; users can build a complete compilation of Linux development environment; users can debug |systemType| OS via serial and Internet.

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +----------+-----------+--------+-----------------+
   | Revision |    Date   | Author |   Description   |
   +==========+===========+========+=================+
   |   V1.1   | 2021-12-30|  Randy | Revised         |
   +----------+-----------+--------+-----------------+
   |   V1.0   | 2018-05-14|  Madi  | Initial Version |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

   *CS10600F070*    *CS10768F097*   *CS12800F101*   *CS10768F121*   *CS10768F121-U*   *CS10768F150*   *CS12102F170*   *CS14900F190*   *CS19108F215*

.. _db_pkg_linux_55:

**PREBUILT FILES PACKAGE:**

Prebuilt files for the various industrial PCs can be found in the :ref:`OS Downloads <IMX6Q_OSDownloads>`. |br|
Below are the links to the prebuilt files for each industrial PC model.

+ :ref:`CS10600F070 <CS10600F070-linuxQt>`
+ :ref:`CS10768F097 <CS10768F097-linuxQt>`
+ :ref:`CS12800F101 <CS12800F101-linuxQt>`
+ :ref:`CS10768F121 <CS10768F121-linuxQt>`
+ :ref:`CS10768F121-U <CS10768F121-U-linuxQt>`
+ :ref:`CS10768F150 <CS10768F150-linuxQt>`
+ :ref:`CS12102F170 <CS12102F170-linuxQt>`
+ :ref:`CS14900F190 <CS14900F190-linuxQt>`
+ :ref:`CS19108F215 <CS19108F215-linuxQt>`

.. rubric:: System Features

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | Kernel        | Kernel 3.14.52                   |
   +---------------+----------------------------------+
   | Bootloader    | Uboot 2015.04                    |
   +---------------+----------------------------------+
   | System        | |systemType|                     |
   +---------------+----------------------------------+
   | Python        | Python 2.7.9                     |
   +---------------+----------------------------------+
   | Qt            | Qt 5.5.1                         |
   +---------------+----------------------------------+
   | Desktop       | matchbox                         |
   +---------------+----------------------------------+
   | user/password | [root/root]                      |
   +---------------+----------------------------------+

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Files Package to re-flash the system.

Power Supply Unit (PSU) with the appropriate voltages, as follows:

+ These products: CS10768F121, CS10768F121-U, CS10768F150, CS12102F170, CS14900F190, and CS19108F215 requires a 15V to 36V power adapter.
+ These products: CS10768F097 and CS12800F101 product needs a 12V to 36V power adapter.
+ The CS10600F070 product needs a 6V to 36V power adapter.

You need to prepare the Power Adapter by yourself

.. include:: Resources/Hardware_Req
* Mini-B USB OTG Cable
* TF Card (at least 4GB) and card reader

Software Requirements
---------------------

* |systemType| OS Prebuilt Files Package (from the link above)
* `Xshell <https://xshell.en.softonic.com/>`_ or other terminal emulation software
* `VNC-Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_
* `Cross-toolchain <https://bit.ly/3FNAjeM>`_
* `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K31452-V1.3.zip>`_
* Useful tools for Qt development

.. note::

    * If you want to re-flash the system, you need the Prebuilt image package.
    * You can use MFGTools on the Windows PC to download system images to the IPC.
    * You can use Xshell or other terminal emulation software to debug Chipsee Industrial PC products in Windows.
    * You can use VNC-Viewer to to remote control Chipsee Industrial PC over Ethernet.
    * The cross-toolchain can compile a program for Chipsee Industrial PC.

.. note::

    In this documentation, all the commands are executed with ``root`` user privileges.

Debug
=====

In this document, we use Xshell to debug the Chipsee Industrial Computer. You can also use other tools such as Putty, Minicom, SecureCRT or any terminal emulation software.

Serial Debug
------------

You can refer to the RS232/RS485/CAN Connector section under the :ref:`EPC/PPC-A9-070-C <EPC/PPC-A9-070-C>` manual to understand the serial ports of the IPC.
The debug serial port of Chipsee Industrial Computer is the first RS232 port. You can use it to debug directly, and the default user and password is [root/root].
You can use RS232_1_TXD, RS232_1_RXD, GND. |br| |br|

Follow these steps to perform serial debugging:

* Connect your Windows PC to the Chipsee IPC over a serial cable. Please reference the :download:`How To Connect Board By Serial </Media/How_To_Connect_Board_By_Serial.pdf>` manual to connect your PC and Chipsee Industrial Computer over a serial cable.
* Open XShell and use the session properties as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/Serial_Debug_1.jpeg
       :align: center
       :figclass: align-center

       *Add Session*

    .. figure:: /Media/Pi/Software/Serial_Debug.jpeg
       :align: center
       :figclass: align-center

       *Session Properties*

    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/Serial_Debug_3.jpeg
       :align: center
       :figclass: align-center

       *Serial Debug*

SSH Debug
---------

To perform SSH debugging on the Chipsee IPC, you must first connect the product to the Internet.

Continue the debugging by follow these steps:

* Get the IP address of the Chipsee IPC product.
* You can configure XShell or you can directly use the SSH tool in Linux OS. In this tutorial, we will use the XShell tool to perform SSH debugging.
* Open XShell and add a new session and set it as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/SSH_Debug_1.jpeg
       :align: center
       :figclass: align-center

       *SSH Setting*

* Now we can perform SSH debugging using XShell.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/SSH_Debug_2.jpeg
       :align: center
       :figclass: align-center

       *SSH Debug*

VNC Debug
---------


You can use the VNC-Viewer software in Windows to control Chipsee IPC over Ethernet.

* Open the VNC-Viewer software as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/VNC_Debug_1.jpeg
       :align: center
       :figclass: align-center

       *VNC Desktop*

* Click on the **X11VNC** icon to enable the X11VNC.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/VNC_Debug_2.jpeg
       :align: center
       :figclass: align-center

       *X11VNC Enable*

* Use VNC-Viewer in Windows to control it over Ethernet, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/VNC_Debug_3.jpeg
       :align: center
       :figclass: align-center

       *VNC-Viewer Connect*

    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/VNC_Debug_4.jpeg
       :align: center
       :figclass: align-center

       *Authentications*

Downloading images
==================

Boot Switch Configuration
-------------------------

CS-IMX6 has a boot configuration select switch, as shown on the figure below. You can use the boot select switch to change between three modes, namely：

+ TF Card
+ eMMC Boot
+ Download

.. figure:: /Media/ARM/A9/Others/BootSW.png
   :align: center
   :figclass: align-center

   Boot Mode Setup

.. table:: Boot Configuration Selection
    :align: center
    :width: 100%
    :widths: auto

    +-----------------------+-------+-------+-------+-------+
    | **SW Mode**           | **1** | **2** | **3** | **4** |
    +=======================+=======+=======+=======+=======+
    | **TF Card**           | 1     | 0     | 0     | 0     |
    +-----------------------+-------+-------+-------+-------+
    | **eMMC**              | 1     | 1     | 0     | 1     |
    +-----------------------+-------+-------+-------+-------+
    | **Download**          | 0     | 1     | 1     | 0     |
    +-----------------------+-------+-------+-------+-------+

.. note::

    The user can use both the pre-built |systemType| image files and the `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K31452-V1.3.zip>`_ software to download new images to the system, boot system and perform necessary software and hardware test.

Prebuilt Files Package
----------------------

You can get the Prebuilt Files Package for each model from links mentioned at the beginning of this documentation.
You can also get the Prebuilt Files Package from the DVD in /|systemType|/Prebuilds folder. However, it may be outdated so always
compare the versions (the last number in the filename is the release date).

The prebuilt package has the following content:

.. table:: Prebuilt Files Package
  :width: 100%
  :align: center
  :widths: auto

  +--------------------------------------------------------+--------------------------------------+
  | Contents                                               | Comment                              |
  +========================================================+======================================+
  | boot/imx6q-eisd.dtb                                    | TF Card boot dtb file                |
  +--------------------------------------------------------+--------------------------------------+
  | boot/u-boot-sd.imx                                     | TF Card boot bootloader              |
  +--------------------------------------------------------+--------------------------------------+
  | boot/zImage                                            | TF Card boot kernel file             |
  +--------------------------------------------------------+--------------------------------------+
  | boot/logo.bmp                                          | TF Card boot logo file               |
  +--------------------------------------------------------+--------------------------------------+
  | filesystem/rootfs-emmc-flasher.tar.bz2                 | TF Card boot rootFS                  |
  +--------------------------------------------------------+--------------------------------------+
  | mksdcard.sh                                            | Shell tools to make bootable TF Card |
  +--------------------------------------------------------+--------------------------------------+
  | README                                                 | Simple guidelines                    |
  +--------------------------------------------------------+--------------------------------------+
  | S1.jpg                                                 | Boot Switch Config Figure            |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/emmc/rootfs.tar.bz2                         | RootFS in target eMMC                |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/emmc/u-boot-emmc.imx                        | Bootloader in target eMMC            |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/emmc/zImage                                 | Kernel file in target eMMC           |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/emmc/zImage_framebuffer                     | Kernel file with frame-buffer        |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/emmc/imx6q-eisd.dtb                         | Dtb file in target eMMC              |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/emmc/imx6q-eisd.dtb_framebuffer             | Dtb file with frame-buffer           |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/emmc/logo.bmp                               | Logo file in eMMC                    |
  +--------------------------------------------------------+--------------------------------------+
  | emmc-flash/mkemmc.sh                                   | Shell tool to download images to eMMC|
  +--------------------------------------------------------+--------------------------------------+

.. note::

   * The default ``zImage`` and ``imx6q-sabresd.dtb`` files support *'keep the logo from uboot to kernel'* but don't support framebuffer.
   * We also provide ``zImage_framebuffer`` and ``imx6q-eisd.dtb_framebuffer`` file versions that support the framebuffer function but do not support the *'keep the logo from uboot kernel'* feature. If you need the framebufer, just rename these two files to ``zImage`` and ``imx6q-eisd.dtb``.

Downloading Images by using MFGTool
-----------------------------------

The `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K31452-V1.3.zip>`_ can be used to download images into a target device.
It is a quick and easy tool for downloading images. 

.. note::
    The operator should use the prebuilt file we provided in the CD to test the hardware before re-flashing the system.

Before downloading images with the `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K31452-V1.3.zip>`_, set the boot switch to download mode. (refer to `Boot Switch Configuration`_ above)

Configuring MFGTool
^^^^^^^^^^^^^^^^^^^

To configure MFGTool, follow these steps:

* Untar ``Mfgtools-K31452-Vx.x.tar.gz`` file.
* Open the extracted folder ``Mfgtools-K31452-Vx.x`` and edit ``cfg.ini`` file.
* In the ``cfg.ini`` file, ensure the ``name`` and ``display`` variables are set to ``eMMC-Linux`` and ``1024600`` respectively, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/mfgtools_1.jpeg
   :align: center
   :figclass: align-center

   *Cfg.ini file*

.. note::

   You can get the supported display from `Mfgtools-K31452-V1.0\\Profiles\\Linux\\OS Firmware\\firmware` directory. |br|
   Modify config ``UICfg.ini`` file. This file has only one line: ``PortMgrDlg=1`` that indicates you can download the images to one board at the same time. The max value is 4.

Copy Image To Android Directory
+++++++++++++++++++++++++++++++

Follow these steps to copy image to Linux directory:

* Copy the images from `prebuilt-xxx/emmc-flash/emmc/` to `Mfgtools-K31452-V1.0\\Profiles\\Linux\\OS Firmware\\files\\linux` directory.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/mfgtools_2.jpeg
   :align: center
   :figclass: align-center

   *Prepare Images*

Using MFGTool
+++++++++++++

#) Connect a USB OTG cable from a Windows PC to the USB OTG port on the IPC.
#) Change the boot select configuration to **0 1 1 0**, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Android_43/use_mfgtool_1.png
       :align: center
       :figclass: align-center

       *Boot Switch Config*

#) Connect a 12V-2A power adapter to the IPC and power ON.
#) On your Windows PC, open the ``Mfgtools-Rel-XXX_XXXXXX_MX6Q_UPDATER_VXX`` directory and run the ``MfgTool2.exe`` file, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Android_60/use_mfgtool_2.png
       :align: center
       :figclass: align-center

       *Run* **MfgTools2.exe** *file*

    .. figure:: /Media/ARM/A9/Software/Android_43/use_mfgtool_3.png
       :align: center
       :figclass: align-center

       *Prepare to start*

    .. note::

        If you get a message saying *No Device Connected*, check the USB-OTG cable to ensure it is ready. |br|

        .. figure:: /Media/ARM/A9/Software/Android_43/use_mfgtool_4.png
           :align: center
           :figclass: align-center

           *The USB-OTG cable is not connected correctly.*

#) Click on **Start** button to download the Image.
    .. figure:: /Media/ARM/A9/Software/Android_43/use_mfgtool_5.png
       :align: center
       :figclass: align-center

       *Downloading Images*

    .. note::

        If you are using a Window 7 PC, you will receive a prompt that asks you to format the disk. Please ignore or cancel it. |br|

        .. figure:: /Media/ARM/A9/Software/Android_43/use_mfgtool_6.png
           :align: center
           :figclass: align-center

           *Cancel format disk*

#) When the process is complete, you click the **Stop** button to stop downloading Image and exit.
    .. figure:: /Media/ARM/A9/Software/Android_43/use_mfgtool_7.png
       :align: center
       :figclass: align-center

       *Download Image is finished*

Downloading Images by using the TF card
---------------------------------------

Follow the steps below to download images onto the eMMC by using the TF Card:

#) Copy the Prebuilt Files Package to a Linux environment (such as Ubuntu 14.04).
#) Insert the SD card into your computer. If you are using virtual machines, please ensure the SD card is mounted to the Linux operating system.
#) Confirm the SD card mount point, ``/dev/sdX``，(e.g., ``/dev/sdc`` or ``/dev/sdb``, be sure to use the right one). In a Linux system, you can use the command below to find out what *X* is.
    .. code:: bash

        $ sudo fdisk –l

#) Copy the ``prebuilt-imxv1-csXXXXXfXXXvX-android6-emmc-YYYYMMDD.tar.gz`` to somewhere(such as $HOME) on the Ubuntu PC.
#) Extract the ``prebuilt-imxv1-csXXXXXfXXXvX-android6-emmc-YYYYMMDD.tar.gz``
    .. code-block:: bash

        $ tar -xzvf prebuilt-imxv1-csXXXXXfXXXvX-android6-emmc-YYYYMMDD.tar.gz

#) Go to the folder
    .. code-block:: bash

        $ cd prebuilt-imxv1-csXXXXXfXXXvX-android6-emmc-YYYYMMDD

#) Use the following command to flash the |systemType| OS to the SD card
    .. code-block:: bash

        $ sudo ./mksdcard.sh --device /dev/sd<?>

    .. note::

        * sd<?> means the SD card mount point, (e.g., ``/dev/sdc`` or ``/dev/sdb``) in Ubuntu system.
        * The recommended SD card should be Sandisk Class4 level SD card or above.

#) The bootable SD Card is now ready. Power OFF the industrial PC and insert the SD Card.
#) Set the switch S1 to TF card boot mode. (refer to `Boot Switch Configuration`_ above)
#) Connect the industrial PC to PC via COM1. Power ON the IPC.
#) After 20 minutes, if the LED on industrial PC stays lit, flashing is completed. Using COM1, you can also find this message **>>>>>>> eMMC Flashing Completed <<<<<<<** which indicates that the system image was downloaded correctly to the eMMC.
#) Power OFF and set the switch S1 to eMMC boot mode. (refer to `Boot Switch Configuration`_ above)


System Resource
===============

TF Card/USB/SATA Disk
---------------------

The TF Card and USB Storage supports hot-plug but the SATA Disk does not support hot-plug.
These devices will be automatically mounted on `/run/media/mmcblk0P*`, as shown in the figure.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/TF_Card.jpeg
   :align: center
   :figclass: align-center

   *TF Card*

.. note::

   The TF card and USB Storage do not support NTFS format. Please format it to FAT32 first before plugging into IPC.

Network
-------

This system uses a networking service to control Ethernet and uses ``wpa_supplicant`` to control the WIFI network.

Wired Ethernet
^^^^^^^^^^^^^^

You can get the IP address from the following application, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/wired_1.jpeg
   :align: center
   :figclass: align-center

   *Wired Connection*

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/wired_2.jpeg
   :align: center
   :figclass: align-center

   *Ethernet Information*

Wi-Fi
^^^^^

You can configure the Wi-Fi using these methods:

* Config Wi-Fi by GUI
* Config Wi-Fi by Command

**Config Wi-Fi by GUI**

* Click the **terminal** on the desktop
* Use the following command to generate network config information.

.. code-block:: bash

   # wpa_passphrase "Chipsee" "1chipsee234567890"

* Replace the information in `/etc/wpa_supplicant.conf` by setting the ``ssid=Chipsee`` and ``psk=1chipsee234567890``, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/wifi_config_1.jpeg
   :align: center
   :figclass: align-center

   *Wi-Fi Config File*

* Open the **Wi-Fi** icon on the desktop, then click the **Enable** button. Wait for some time to get the Wi-Fi working. The Wi-Fi is working when the network tab displays the *WIFI Enabled!* message, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/wifi_config_2.jpeg
   :align: center
   :figclass: align-center

   *Wi-Fi Enable*

**Config Wi-Fi by Command**

* Use the command below to enable Wi-Fi.

.. code-block:: bash

   # wifienable.sh

* List available network and remove default if exist using these commands

.. code-block:: bash

   # wpa_cli list_network
   # wpa_cli remove_network
   # wpa_cli scan
   # wpa_cli scan_result // get latest scan results
   # wpa_cli ap_scan 1

* Add a new network and list added network using these commands

.. code-block:: bash

   # wpa_cli add_network
   # wpa_cli list_network

* Set SSID, Password, and key management using these commands

.. code-block:: bash

   # wpa_cli set_network 0 ssid "Chipsee"
   # wpa_cli set_network 0 key_mgmt WPA-PSK
   # wpa_cli set_network 0 psk "1chipsee234567890"

* Enable the ``network 0`` with this command

.. code-block:: bash

   # wpa_cli select_network 0

* Save config

.. code-block:: bash

   # wpa_cli save_config

* Re-enable Wi-Fi

.. code-block:: bash

   # wifienable.sh

Multimedia
----------

This system supports NXP Gstreamer-imx Multimedia library and its various plugins.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/multimedia_1.jpeg
   :align: center
   :figclass: align-center

   *GStreamer Plugins*

Audio Test
^^^^^^^^^^

You can use the command below to record music. The ``-d`` parameter means *interrupt after # seconds*. In this example, ``-d`` is equal to 18 seconds.

.. code-block:: bash

   $ sudo  arecord  -N  -M  -r  44100  -f  S16_LE  -c  2  -d  18  test.wav

You can use the command below to playback the recorded sound above.

.. code-block:: bash

   $ sudo  aplay  -N  -M  test.wav

You can also use the **QT Test Application** to record and playback audio. |br|

On the **QT Test Application** desktop, click on the **HT** button to perform a hardware test, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/multimedia_2.jpeg
   :align: center
   :figclass: align-center

   *Hardware Test*

You can click the **Audio** button to playback audio. You can also click the **Record** button to record 18 seconds of audio then the application will playback the audio automatically.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/multimedia_3.jpeg
   :align: center
   :figclass: align-center

   *Audio Test*

HDMI
----

You can follow the steps below to display the IPC output onto an external display via HDMI.

* Power OFF IPC. Connect the external display to the IPC using an HDMI cable.
* Refer to the `Serial Debug`_ section to set serial debug.
* Power ON IPC. In XShell, hit any key to stop auto boot and input the uboot command mode, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/hdmi.jpeg
       :align: center
       :figclass: align-center

       *Uboot*

    .. note::

        HDMI does not support hot-plug. The sound comes from the HDMI monitor, neither the speaker nor the headset on board.

* Use the following command to set different resolution
    + For 1080p
        .. code-block:: bash

           => setenv displayargs video=mxcfb0:dev=hdmi,1920x1080M@60 video=mxcfb1:dev=off video=mxcfb2:off
           => saveenv
           => boot

    + For 720p
        .. code-block:: bash

           => setenv displayargs video=mxcfb0:dev=hdmi,1280x720M@60 video=mxcfb1:dev=off video=mxcfb2:off
           => saveenv
           => boot

    + For 480p
        .. code-block:: bash

           => setenv displayargs video=mxcfb0:dev=hdmi,800x480M@60 video=mxcfb1:dev=off video=mxcfb2:off
           => saveenv
           => boot

    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/hdmi_2.jpeg
       :align: center
       :figclass: align-center

       *HDMI Output Setting*

* Reboot the IPC.
* Use the following command to reset the output from LDB.
    .. code-block:: bash

       => setenv  displayargs  video=mxcfb0:dev=ldb  video=mxcfb1:dev=off  video=mxcfb2:off
       => saveenv
       => boot

Serial Port
-----------

There are five serial ports on the Chipsee IPC: 2 x RS232 and 3 x RS485 (can be customised). Refer to the table below for the available serial device nodes.

The default serial port configuration is 2 x RS232, 2 x RS485, 1 x RS485 which is shared with Bluetooth. |br|
|contact| if you need help with changing the default serial port configuration

.. include:: Resources/serial_table

You can test the serial port by using the **HT_Serial Application** in the desktop, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/serial_1.jpeg
   :align: center
   :figclass: align-center

   *HT_Serial Test*

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/serial_2.jpeg
   :align: center
   :figclass: align-center

   *HT_Serial Test*

CAN Bus
-------

Chipsee Industrial PC is equipped with two CAN busses (CAN1 and CAN2). Two devices can be interconnected.
You can test the CAN buses by using the **HT application** but you must add one 120Ω resistor between CAN_H and CAN_L on one of the two Boards, as shown on the figure below.

.. figure:: /Media/Pi/Software/CAN.jpeg
   :align: center
   :figclass: align-center

   *CAN Connect*

.. note::

   The Chipsee IPC does not mount the 120Ω matched resistor on all CAN signals by default.

Here are a few examples to test CAN by using CAN units

* Install `can-utils`
    .. code:: bash

        $ sudo apt install can-utils

* Set the bit-rate to **50Kbits/sec** with triple sampling using the following command (use ROOT user):
    .. code:: bash

        $ sudo ip link set can0 type can bitrate 50000 triple-sampling on

* Bring up the device using the command:
    .. code:: bash

        $ sudo ip link set can0 up

* Transfer packets
    + Transmit 8 bytes with standard packet id number as 0x10

    .. code:: bash

        $ sudo cansend can0 -i 0x10 0x11 0x22 0x33 0x44 0x55 0x66 0x77 0x88

    + Transmit 8 bytes with extended packet id number as 0x800

    .. code:: bash

        $ sudo cansend can0 -i 0x800 0x11 0x22 0x33 0x44 0x55 0x66 0x77 0x88 - e

    + Transmit 20 8 bytes with extended packet id number as 0xFFFFF

    .. code:: bash

        $ sudo cansend can0 -i 0xFFFFF 0x11 0x22 0x33 0x44 0x55 0x66 0x77 0x88 -e --loop=20

* Receive data from CAN bus
    .. code:: bash

        $ sudo candump can0

* Bring down the device
    .. code:: bash

        $ sudo ip link set can0 down

You can use the **HT application** to test CAN. To perform the CAN test, you need two Chipsee IPC boards to perform the test. |br|
Follow these steps to perform the CAN test:

* Connect the two IPC boards and select the CAN port ``can0`` or ``can1`` simultaneously on both IPC boards.
* Click on the **CanStart** button simultaneously on both IPC boards.

Refer to the figure below for the CAN part in the HT application.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/can_1.jpeg
   :align: center
   :figclass: align-center

   *CAN*

GPIO
----

There are 8 GPIOs, 4 Output, and 4 Input, they are all isolated. You can control the output or input pin voltage by feeding the VDD_ISO suite voltage. The pin voltage should be from 5V to 24V. Refer to the tables below for a detailed port definition:

.. include:: Resources/gpio_table

Set `gpio106 Output` to high or low using this command

.. code-block:: bash

   # echo  106  > /sys/class/gpio/export                //export gpio106
   # echo  out  > /sys/class/gpio/gpio106/direction     //set gpio106 Output
   # echo  1  > /sys/class/gpio/gpio106/value           //Set gpio106 high
   # echo  0  > /sys/class/gpio/gpio106/value           //Set gpio106 low

Set `gpio30 Input` using this command

.. code-block:: bash

   # echo  30  > /sys/class/gpio/export                  //export  gpio30
   # echo  in  > /sys/class/gpio/gpio30/direction        //Set  gpio30 input

Un-export `gpio30` using this command

.. code-block:: bash

   # echo  30  > /sys/class/gpio/unexport                 //un-export  gpio30

You can use the **HT application** to test GPIO. |br|
Follow these steps to perform the GPIO test:

* Before you test, you need to connect the output gpio and input gpio, like `out 1 — in 1` / `out 2 — in 2` / `out 3 — in 3` / `out 4 — out 4`.
* Click on the **SetAllHigh** or **SetAllLow** button to check the right light status.
* Also, you can set the `output gpio` to high or low respectively. Then check the right `input gpio` status, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/gpio_1.jpeg
   :align: center
   :figclass: align-center

   *GPIO Test*

.. note::

   The default gpio has 4 Outputs and 4 Inputs. If you want a custom solution, please check the `/etc/init.d/chipsee-init` file for details.

Buzzer
------

The buzzer is one GPIO, which has the GPIO Number as 80.

You can test the buzzer with the following commands.

.. code-block:: bash

   # echo  80  > /sys/class/gpio/export                 //export gpio80
   # echo  out  > /sys/class/gpio/gpio80/direction      //set gpio80 output
   # echo  1  > /sys/class/gpio/gpio80/value            //Open Buzzer
   # echo  0  > /sys/class/gpio/gpio80/value            //Close Buzzer

You also can use the HT application to test the buzzer.

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/buzzer.jpeg
   :align: center
   :figclass: align-center

   *Buzzer*

Modify Logo
-----------

This system supports changing the logo by yourself. There are two ways:

* Replace the logo file in prebuilt images packages, and download images.
* Change the logo without downloading images.

.. note::

   Logo file is one 32bpp, format is bmp.

Method 1 - Downloading images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replace the `prebuilt-xxx/emmc-flash/emmc/logo.bmp` and reference `Downloading Images by using MFGTool`_ to flash the image.

Method 2 - Don't Download Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will use **MFGTools** and the **Logoflasher** apps to change the logo.

**Use MFGTools to Change LOGO**

* Replace the ``logo.bmp`` file in `Mfgtools-K31452-V1.0\\Profiles\\Linux\\OS Firmware\\files\\ubuntu` with your customised logo file.
* Open and edit the `Mfgtools-K31452-V1.0\\cfg.ini` file and set the ``name`` variable to ``eMMC-Linux-Logo`` as shown below.
   .. figure:: /Media/ARM/A9/Software/Linux_Qt55/logo_1.png
      :align: center
      :figclass: align-center

      *Change name*

.. figure:: /Media/ARM/A9/Software/Linux_Qt55/logo_2.png
   :align: center
   :figclass: align-center

   *Logo Modify with MFGTool*

**Use Logoflasher to Change Logo**

You can get the `Logoflasher <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/prebuilt-imx6qdl-bootfile-update-20220323.tar.gz>`_ file and use this tool to make one bootable TF card. |br|
Follow the steps below to change logo

* Use the following commands to make bootable TF card.
     .. code-block:: bash

        $ sudo  tar  zxvf  prebuilt-imx6qdl-bootfile-update-xxx.tar.gz
        $ sudo  cd  prebuilt-imx6qdl-bootfile-update-xxx
        $ sudo  ./mksdcard.sh  --device  /dev/sdX --display 1024600     // resolution

* Put your custom logo file in the first partition ``boot-flash`` directory on the TF Card.
* Set boot mode to **TF card**. You can reference `Boot Switch Configuration`_.
* Power ON the IPC. If you see this message, **>>>>>>> eMMC Flashing Completed <<<<<<<**, you are done:

Development
===========

In this chapter, you will learn how to set up the QT development environment, and develop the first QT application on Chipsee IPC boards.

Host system requirements
------------------------

#) Ubuntu 14.04 LTS 64bit system should be installed on the host machine.
#) Qtcreator is optional to develop application, you can download QT5.5.1 which will install Qtcreator. Other Qt version should ok as we only need Qtcreator.

Preparation
-----------

#) Download `QT5.5.1 <https://download.qt.io/new_archive/qt/5.5/5.5.1/>`_ and install it on the system. Other Qt version should ok as we only need Qtcreator. Install it in the `/home/<user>/program` directory.
#) Install SDK. Get the `SDK <https://chipsee-tmp.s3.amazonaws.com/DVD/IMX6Q/Tools/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1.sh>`_ and install it using this command:
    .. code-block:: bash

       # chmod +x fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1.sh
       # ./ fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1.sh

    |br| The default install directory is `/opt/fsl-imx-x11/3.14.52-1.1.1`. You can install it in this directory or you can also use another directory.

#) Use the following command to test SDK:
    .. code-block:: bash

       # source /opt/fsl-imx-x11/3.14.52-1.1.1/ environment-setup-cortexa7hf-vfp-neon-poky-linux-gnueabi
       # echo ${CC}

#) Setting Qtcreator. If you installed ``qt-opensource-linux-x64-5.5.1.run``, the Qtcreator will be installed automatically.
    * Before you open QtCreator, you need to add the following code-block in the first line of `/home/<user>/program/Qt5.5.1/Tools/QtCreator/bin/qtcreator.sh`, as shown on the figure below.
        .. code-block:: bash

           $ source /opt/fsl-imx-x11/3.14.52-1.1.1/ environment-setup-cortexa7hf-vfp-neon-poky-linux-gnueabi


        .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_1.jpeg
           :align: center
           :figclass: align-center

           *Setting QtCreator*

#) Use the following command to open Qtcreator.
    .. code-block:: bash

       # /home/program/Qt5.5.1/Tools/QtCreator/bin/qtcreator.sh

#) Open the QtCreator Options, then click on Tools->Options->Build & Run. Set the Debuggers/Compilers/Qt Versions/Kits as shown on the figures below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_2.jpeg
       :align: center
       :figclass: align-center

       *Debuggers*

    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_3.jpeg
       :align: center
       :figclass: align-center

       *Compilers*

    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_4.jpeg
       :align: center
       :figclass: align-center

       *Qt Versions*

    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_5.jpeg
       :align: center
       :figclass: align-center

       *Kits*

Example — Develop a ``HelloWorld`` Program
------------------------------------------

#) Use QtCreator to create a new Qt Widgets Application, named ``HelloWorld``, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_6.jpeg
       :align: center
       :figclass: align-center

       *Qt Widgets Application*

#) Select IMX kits, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_7.jpeg
       :align: center
       :figclass: align-center

       *Kit Selection*

#) Use QMainWindow as the Base class, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_8.jpeg
       :align: center
       :figclass: align-center

       *Base Class*

#) Click the **Design** icon to add one label widget, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_9.jpeg
       :align: center
       :figclass: align-center

       *Add Label Widget*

#) Click on the **Build** icon to build app, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Linux_Qt55/app_dev_10.jpeg
       :align: center
       :figclass: align-center

       *Build App*

#) Copy the ``Helloworld`` app to the IPC board's `/home/root/` directory and use the following command to run it:
    .. code-block:: bash

       # export DISPLAY=:0.0
       # ./HelloWorld

You can get the ``HelloWorld`` app from the `/home/leave/build-HelloWorld-imx-Debug` directory, but your directory might not be the same as this one.


Q&A
===

In this chapter, you can learn how to set up the QT development environment, and develop the first QT application on Chipsee IPC boards.

How to Change psplash's
-----------------------

* Install IMX SDK and some Packages. Reference the install SDK point under the **Preparation** section above to install IMX SDK and install some recommends packages using this command:
    .. code-block:: bash

       $ sudo  apt-get  install  autoconf  libgdk-pixbuf2.0-dev

* Generate psplash of your own.
    + Get `psplash <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/psplash_imx6.zip>`_ and extract it.
        .. code-block:: bash

           $ sudo tar zxvf psplash.tar.gz

    + Prepare a PNG file, such as ``chipsee.png``
        .. code-block:: bash

           $ sudo cp chipsee.png psplash/
           $ sudo cd psplash

    + Setting environment
        .. code-block:: bash

           $ source /opt/fsl-imx-x11/3.14.52-1.1.1/environment-setup-cortexa9hf-vfp-neon-poky-linux-gnueabi

        .. figure:: /Media/ARM/A9/Software/Linux_Qt55/qa.png
           :align: center
           :figclass: align-center

    + Generate header file and modify the psplash.c, then config and make:
        .. code-block:: bash

           $ ./make-image-header.sh chipsee.png POKY  //you will find a new file named chipsee-img.h
           $ vi psplash.c  // replace the header file name (psplash-poky-img.h) in psplash.c with chipsee-img.h
           $ ./autogen.sh
           $ make  // you will generate the file psplash

    + Then you will find the file ``psplash``, replace the one in ``rootfs`` `/usr/bin/psplash`. Reboot your IPC board to apply the changes made to the psplash.
    + You can remove the `/etc/init.d/psplash.sh` file in ``rootfs`` to disable it.
    + If you want to rotate the psplash screen, just do the following in the system:
        .. code-block:: bash

           # echo 180 > /etc/rotation   // rotate  180  angle
           # echo 0 > /etc/rotation	    // reset to default.

.. include:: Resources/support