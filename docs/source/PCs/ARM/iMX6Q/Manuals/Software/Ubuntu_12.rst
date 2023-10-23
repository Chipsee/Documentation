.. include:: /PCs/Shared/pdf_options_software

.. |systemType| replace:: Ubuntu 12.04
.. |chip| replace:: iMX6Q

|systemType| OS
###############

.. centered:: |systemType| OS User Manual

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
   |   V1.0   | 2021-12-30|  Randy | Revised         |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

   *CS10600F070*   *CS12800F101*

.. _db_pkg_ubuntu_12:

**PREBUILT FILES PACKAGE:**

Prebuilt files for the various industrial PCs can be found in the :ref:`OS Downloads <IMX6Q_OSDownloads>`. |br|
Below are the links to the prebuilt files for each industrial PC model.

+ :ref:`CS10600F070 <CS10600F070-ubuntu>`
+ :ref:`CS12800F101 <CS12800F101-ubuntu>`

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
   | System        | |systemType| LTS                 |
   +---------------+----------------------------------+
   | Python        | Python 2.7.9 / Python 3.4.0      |
   +---------------+----------------------------------+
   | Qt            | Need to be installed by user     |
   +---------------+----------------------------------+
   | GCC           | 4.8.2                            |
   +---------------+----------------------------------+
   | Desktop       | matchbox                         |
   +---------------+----------------------------------+
   | user/password | [linaro/linaro] or [linaro/root] |
   +---------------+----------------------------------+

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Files Package to re-flash the system.

Power Supply Unit (PSU) with the appropriate voltages, as follows:

+ The CS12800F101 product needs a 12V to 36V power adapter.
+ The CS10600F070 product needs a 6V to 36V power adapter.

You need to prepare the Power Adapter by yourself

.. include:: Resources/Hardware_Req
* Mini-B USB OTG Cable
* TF Card (at least 4GB) and card reader

Software Requirements
---------------------

* |systemType| OS Prebuilt Files Package (from the link above)
* MFGTools
* QT4.8.4 for Linux


Getting Started and Tests
=========================

.. note::

    Throughout this section, the user can use both the pre-built |systemType| image files and the `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K3035-V2.1.zip>`_ software to burn files to the system, boot system and perform necessary software and hardware test.


Downloading images
------------------

Boot Switch Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

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

    The user can use both the pre-built |systemType| image files and the **MFGTools** software to download new images to the system, boot system and perform necessary software and hardware test.

Prebuilt Files Package
^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K3035-V2.1.zip>`_ can be used to download images into a target device.
It is a quick and easy tool for downloading images.

Before downloading images with the MFGTools, set the boot switch to download mode. (refer to `Boot Switch Configuration`_ above)

Configuring MFGTool
+++++++++++++++++++

To configure MFGTool, follow these steps:

* Untar ``Mfgtools-K3035-Vx.x.zip`` file.
* Open the extracted folder ``Mfgtools-K3035-Vx.x`` and edit ``cfg.ini`` file.
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/mfgtools_1.png
       :align: center
       :figclass: align-center

       *Extracted Folder*

* In the ``cfg.ini`` file, ensure the ``name`` variable is set to ``Ubuntu-SabreSD-eMMC``, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/mfgtools_2.png
       :align: center
       :figclass: align-center

       *Cfg.ini file*

    .. note::

       The default uImage disable the Frame buffer function. If you want to use Frame buffer, please rename the ``uImage_has_console`` to ``uImage`` to replace the default ``uImage``.

Copy Image To Android Directory
+++++++++++++++++++++++++++++++

Follow these steps to copy image to Linux directory:

* Copy the images from `prebuilt-xxx/emmc-flash/emmc/` to `Mfgtools-K3035-Vx.x\\Profiles\\Linux\\OS Firmware\\files\\ubuntu` directory. Copy the logo file to `Mfgtools-K3035-Vx.x\\Profiles\\MX6Q Linux Update\\OS Firmware\\files\\logo` directory and rename it to `logo.bmp`.

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/mfgtools_3.png
   :align: center
   :figclass: align-center

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/mfgtools_4.png
   :align: center
   :figclass: align-center

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/mfgtools_5.png
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
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/mfgtools_6.png
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Booting Ubuntu OS and Test
--------------------------

.. note::

   If you want to use root, use this command: `$ sudo passwd root`

The first time you start |systemType| OS on the industrial PC will take a little time. But after the first time, |systemType| OS will start quickly.
It is a successful start if you see the |systemType| OS desktop such as the one shown in the figure below:

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/ubuntu_screen.png
   :align: center
   :figclass: align-center

   *Ubuntu 12 Desktop Screen*


SD Test
^^^^^^^

The IPC supports SD card hot-plug. The figure below shows the message when you plug the SD card into IPC.
The IPC will mounts the SD Card to `/media/xxxx-xxxx` directory.

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/sd_1.png
   :align: center
   :figclass: align-center

   *Serial Message*

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/sd_1.png
   :align: center
   :figclass: align-center

   *SD Card*

USB Flash Disk Test
^^^^^^^^^^^^^^^^^^^

The USB Flash Disk is like the SD Card. The IPC mounts the USB Flash Disk to `/mnt/media_rw/` and `/storage/` directory.

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/udisk_1.png
   :align: center
   :figclass: align-center

   *USB flash disk test*

SATA Test
^^^^^^^^^

The SATA does not support hot-plug, but the |systemType| OS supports NTFS, EXT3, and FAT.

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/sata_1.png
   :align: center
   :figclass: align-center

   *SATA test*

Network Test
^^^^^^^^^^^^

The network uses DHCP to get IP Addresses. You can get network access if you connect a LAN cable from the IPC to a router. |br|
You can change the IP Address with this command.

.. code-block:: bash

   # ifconfig eth0 down
   # ifconfig eth0 192.168.xx.xxx up

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/network.png
   :align: center
   :figclass: align-center

   *Network Test*

Sound Card Test
^^^^^^^^^^^^^^^

Please open an audio file in Rhythmbox to test the Sound.

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/sound.png
   :align: center
   :figclass: align-center

   *Sound Test*

Video Test
^^^^^^^^^^

Please open a video file to test the Video.

.. figure:: /Media/ARM/A9/Software/Ubuntu_12/video.png
   :align: center
   :figclass: align-center

   *Video Test*

HDMI Test
^^^^^^^^^

You can reference this document, :download:`IMX6Q U-boot Setting HDMI Output For Android.pdf <https://chipsee-tmp.s3.amazonaws.com/DVD/IMX6Q/7/Android4.3/Documents/IMX6Q U-boot Setting Hdmi Output For Android.pdf>`, to learn about performing HDMI tests.

.. note::

    HDMI does not support hot-plug. The sound comes from the HDMI monitor, neither the speaker nor the headset on board.

WIFI Test
^^^^^^^^^

You must ensure the IPC has an SDIO Wi-Fi module integrated before performing the Wi-Fi test. If the IPC has an SDIO Wi-Fi Module, you can connect to the Wi-Fi and open a browser to test.

Serial Test
^^^^^^^^^^^

There are five serial ports on the Chipsee IPC: 2 x RS232 and 3 x RS485 (can be customised). Refer to the table below for the available serial device nodes.

.. include:: Resources/serial_table

You can install the **SecureCRT** or **Putty** software on a Windows 7 PC to test the serial ports by following these steps:

* Connect COM1 on industrial PC board to Windows 7 PC.
* Run **Serial Port API** App to communicate with Windows 7 PC, as shown on the figure below.

CAN Test
^^^^^^^^

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

    OR

    .. code-block:: bash

       $ sudo canconfig can0 bitrate 50000 ctrlmode triple-sampling on

* Bring up the device using the command:
    .. code:: bash

        $ sudo ip link set can0 up

    OR

    .. code:: bash

        $ sudo canconfig can0 start

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

GPIO
----

There are 8 GPIOs, 4 Output, and 4 Input, they are all isolated. You can control the output or input pin voltage by feeding the VDD_ISO suite voltage. The pin voltage should be from 5V to 24V. Refer to the tables below for a detailed port definition:

.. table:: CS80480F070 – V1.0 P11 Port
   :align: center
   :width: 100%
   :widths: auto

   +-----------------------------+-------------------------------+
   | Pin Number                  | GPIO Number                   |
   +=============================+===============================+
   | 11                          | 205                           |
   +-----------------------------+-------------------------------+
   | 12                          | 106                           |
   +-----------------------------+-------------------------------+
   | 13                          | 29                            |
   +-----------------------------+-------------------------------+
   | 14                          | 30                            |
   +-----------------------------+-------------------------------+
   | 15                          | 28                            |
   +-----------------------------+-------------------------------+
   | 16                          | 204                           |
   +-----------------------------+-------------------------------+
   | 17                          | 94                            |
   +-----------------------------+-------------------------------+
   | 18                          | 95                            |
   +-----------------------------+-------------------------------+

.. table:: CS12800F010 – V1.0 P28 Port
   :align: center
   :width: 100%
   :widths: auto

   +-----------------------------+-------------------------------+
   | Pin Number                  | GPIO Number                   |
   +=============================+===============================+
   | 3                           | 106                           |
   +-----------------------------+-------------------------------+
   | 4                           | 30                            |
   +-----------------------------+-------------------------------+
   | 6                           | 95                            |
   +-----------------------------+-------------------------------+
   | 7                           | 87                            |
   +-----------------------------+-------------------------------+
   | 8                           | 29                            |
   +-----------------------------+-------------------------------+
   | 9                           | 28                            |
   +-----------------------------+-------------------------------+
   | 11                          | 94                            |
   +-----------------------------+-------------------------------+
   | 12                          | 130                           |
   +-----------------------------+-------------------------------+
.. note::

    You need ``ROOT`` permissions to control GPIO.

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


|systemType| system debug in Windows
====================================

In this section, we will discover how to view the |systemType| system via the serial port and debug the system via USB OTG. |br|
Also, we will discover how to install and uninstall applications via USB OTG. |br|
The following operation is under the Windows 7 x64 environment, similar to other Windows platforms.

View |systemType| system via the serial port
--------------------------------------------

Install the **SecureCRT** or **Putty** software on a Windows 7 PC to view the |systemType| system via the serial ports. |br|
Follow these steps to view |systemType| system via the serial port:

* Connect COM1 on the industrial PC board to Windows 7 PC.
* Open the **SecureCRT** or **Putty** software on the Windows 7 PC and configure it as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Android_43/android_debug_1.png
       :align: center
       :figclass: align-center

       *SecureCRT configuration*

* Power ON the industrial PC. You will see the serial output information as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Android_43/android_debug_2.png
       :align: center
       :figclass: align-center

       *Serial output information*

* You can communicate with the system when system boot is complete.

QT development
==============

In this chapter, you will learn how to set up the QT development environment, and develop the first QT application on Chipsee IPC boards.

Preparation
-----------

#) Download and install `QT4.8.4 <https://download.qt.io/archive/qt/4.8/4.8.4/>`_ and `QTCreator2.6.2 <https://download.qt.io/archive/qtcreator/2.6/2.6.2/>`_.

Example — Develop a ``HelloWorld`` Program
------------------------------------------

#) Use QtCreator to create a project, named ``HelloWorld``, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_1.png
       :align: center
       :figclass: align-center

    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_2.png
       :align: center
       :figclass: align-center

    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_3.png
       :align: center
       :figclass: align-center

       *Create Application*


#) Select IMX kits, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_4.png
       :align: center
       :figclass: align-center

       *Kit Selection*

#) Use QMainWindow as the Base class, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_5.png
       :align: center
       :figclass: align-center

       *Base Class*

#) Click the **Design** icon to add one label widget, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_6.png
       :align: center
       :figclass: align-center

    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_7.png
       :align: center
       :figclass: align-center

    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_8.png
       :align: center
       :figclass: align-center


       *Add Label Widget*

#) Click on the **Build** icon to build app, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_9.png
       :align: center
       :figclass: align-center

    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_10.png
       :align: center
       :figclass: align-center

       *Build App*

#) Copy the ``Helloworld`` app from the `/home/leave/qt-creator2.6.2/helloworld` to the IPC board's `/home/root/` directory and use the following command to run it:
    .. code-block:: bash

       # export DISPLAY=:0.0
       # ./HelloWorld

    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_11.png
       :align: center
       :figclass: align-center

       *Install app on IPC*

    .. note::

       The command `qmake -project`, `qmake`, & `make` must be done on board, like above.

#) Add a startup icon for ``helloworld``.
    .. code-block:: bash

       $ cd /usr/share/applications
       $ sudo vi helloworld.desktop

#) Add the following content in the ``helloworld.desktop`` file, as shown on the figure below.
    .. code-block:: text

       [Desktop Entry]
       Version=1.0
       Encoding=UTF-8
       Type=Application
       Name=helloworld
       Comment=helloworld
       NoDisplay=true
       Exec=/home/linaro/Desktop/helloworld/helloworld %f   // the path of qt binary.
       Icon=/home/linaro/Desktop/helloworld/helloworld.png  // you can replace it by you own icon.
       Name[en_US]=helloworld

    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_12.png
       :align: center
       :figclass: align-center

       *Add app to desktop*

#) Locate the directory with app icon and copy it to the desktop, as shown on the figure below:
    .. figure:: /Media/ARM/A9/Software/Ubuntu_12/app_dev_13.png
       :align: center
       :figclass: align-center

       *Copy app icon*

.. include:: /PCs/Shared/support