.. |systemType| replace:: Android 6.0

|systemType| OS
###############

.. centered:: |systemType| OS User Manual

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual is used to provide users with a fast guide of Chipsee Industrial Computers (Abbreviated as IPC) about |systemType| OS development. Through this manual, users can quickly understand the hardware resources; users can build a complete compilation of Android development environment; users can debug |systemType| OS via serial, USB OTG and Internet.

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +----------+-----------+--------+-----------------+
   | Revision |    Date   | Author |   Description   |
   +==========+===========+========+=================+
   |   V1.0   | 2021-12-30|  Randy | Initial Version |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

   *CS10600F070*    *CS10768F097*   *CS12800F101*   *CS10768F121*   *CS10768F121-U*   *CS10768F150*   *CS12102F170*   *CS14900F190*   *CS19108F215*

.. _db_pkg_android_60:

**PREBUILT FILES PACKAGE:**

Prebuilt files for the various industrial PCs can be found in the :ref:`OS Downloads <IMX6Q_OSDownloads>`. |br|
Below are the links to the prebuilt files for each industrial PC model.

+ :ref:`CS10600F070 <CS10600F070-android>`
+ :ref:`CS10768F097 <CS10768F097-android>`
+ :ref:`CS12800F101 <CS12800F101-android>`
+ :ref:`CS10768F121 <CS10768F121-android>`
+ :ref:`CS10768F121-U <CS10768F121-U-android>`
+ :ref:`CS10768F150 <CS10768F150-android>`
+ :ref:`CS12102F170 <CS12102F170-android>`
+ :ref:`CS14900F190 <CS14900F190-android>`
+ :ref:`CS19108F215 <CS19108F215-android>`

.. rubric:: System Features

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | System        | |systemType|                     |
   +---------------+----------------------------------+

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Files Package to re-flash the system.

Power Supply Unit (PSU) with the appropriate voltages, as follows:

+ These products: CS10768F121, CS10768F121-U, CS10768F150, CS12102F170, CS14900F190, and CS19108F215 requires a 15V to 36V power adapter.
+ These products: CS10768F097 and CS12800F101 product needs a 12V to 36V power adapter.
+ The CS10600F070 product needs a 6V to 36V power adapter.


.. include:: Resources/Hardware_Req
* TF Card (at least 4GB) and card reader

Software Requirements
---------------------

* |systemType| OS Prebuilt Files Package (from the link above)
* :download:`Android Studio 2.3.3 for Windows <https://redirector.gvt1.com/edgedl/android/studio/install/2.3.3.0/android-studio-bundle-162.4069837-windows.exe>`
* Android USB driver (for Windows)
* MFGTools_Kernel3.14.52

Getting Started and Tests
=========================

.. note::

    Throughout this section, the user can use both the pre-built |systemType| image files and the `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K31452-V1.3.zip>`_ software to burn files to the system, boot system and perform necessary software and hardware test.

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

Prepare Manufacturing Tool and Image
------------------------------------

The manufacturing tool, referred to as `MFGTools <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/MFGTools/Mfgtools-K31452-V1.3.zip>`_, is a tool that runs on a Windows PC. You can use it to download pre-built images to the eMMC on a Chipsee board. The tools directory contains the ``tar.gz`` file.

.. table::
    :align: center
    :width: 100%
    :widths: auto

    +-------------------------------------------------+-------------------------------------+
    | .. centered:: **MFGTool**                       | **Windows download tool**           |
    +=================================================+=====================================+
    | **Kernel Image**                                | emmc-flash/emmc/boot-imx6q.img      |
    +-------------------------------------------------+-------------------------------------+
    | **U-boot Image**                                | emmc-flash/emmc/u-boot-imx6q.imx    |
    +-------------------------------------------------+-------------------------------------+
    | **Recovery Image**                              | emmc-flash/emmc/recovery-imx6q.img  |
    +-------------------------------------------------+-------------------------------------+
    | **Android File System**                         | emmc-flash/emmc/system.img          |
    +-------------------------------------------------+-------------------------------------+
    | **Android Logo**                                | emmc-flash/emmc/xxx.bmp             |
    +-------------------------------------------------+-------------------------------------+
    | **Industrial Computer**                         | One                                 |
    +-------------------------------------------------+-------------------------------------+
    | **USB OTG Cable**                               | One                                 |
    +-------------------------------------------------+-------------------------------------+
    | **12V-2A power adapter**                        | One                                 |
    +-------------------------------------------------+-------------------------------------+

Downloading Images
------------------

Chipsee IPC supports booting from an integrated eMMC or an external TF Card (also known as the micro SD card).
Booting from the external TF Card allows flashing the system OS.

Downloading Images by using MFGTool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chipsee IPC supports booting from an integrated eMMC.

Configuring MFGTool
+++++++++++++++++++

To configure MFGTool, follow these steps:

* Unzip ``Mfgtools_Kernel3.14.52_V1.0.rar`` file.
* Open the extracted folder ``Mfgtools_Kernel3.14.52_V1.0`` and edit ``cfg.ini`` file.

.. figure:: /Media/ARM/A9/Software/Android_60/mfgtools_1.png
   :align: center
   :figclass: align-center

   *Extracted folder content*

* In the ``cfg.ini`` file, ensure the ``name`` variable is set to ``eMMC-Android``, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Android_60/mfgtools_2.png
   :align: center
   :figclass: align-center

   *Cfg.ini file*

Copy Image To Android Directory
+++++++++++++++++++++++++++++++

Follow these steps to copy image to Android directory:

* Unzip ``prebuilt-imxv1-csXXXXXfXXXvX-android6-emmc-YYYYMMDD.tar.gz`` file. The extracted folder will contain these files: ``boot-imx6q.img``, ``recovery-imx6q.img,``, ``system.img``, and ``u-boot-imx6q.imx``. The logo file, ``android6_xxx.bmp``, is located in the `emmc-flash/emmc` directory.
* Copy the files listed above from the extracted folder to `Mfgtools_Kernel3.14.52_V1.0\\Profiles\\Linux\\OS Firmware\\files\\android` directory.

.. figure:: /Media/ARM/A9/Software/Android_60/mfgtools_3.png
   :align: center
   :figclass: align-center

   *Extracted folder with files*

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

       *Loading Kernel and Formatting rootfs partition*

    .. note::

        If you are using a Window 7 PC, you will receive a prompt that asks you to format the disk. Please ignore or cancel it. |br|

        .. figure:: /Media/ARM/A9/Software/Android_43/use_mfgtool_6.png
           :align: center
           :figclass: align-center

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
        :substitutions:

        $ tar -xzvf prebuilt-imxv1-csXXXXXfXXXvX-android6-emmc-YYYYMMDD.tar.gz

#) Go to the folder
    .. code-block:: bash
        :substitutions:

        $ cd prebuilt-imxv1-csXXXXXfXXXvX-android6-emmc-YYYYMMDD

#) Use the following command to flash the |systemType| OS to the SD card
    .. code-block:: bash
        :substitutions:

        $ sudo ./mksdcard.sh --device /dev/sd<?>

    .. note::

        * sd<?> means the SD card mount point, (e.g., ``/dev/sdc`` or ``/dev/sdb``) in Ubuntu system.
        * The recommended SD card should be Sandisk Class4 level SD card or above.

#) The bootable SD Card is now ready. Power OFF the industrial PC and insert the SD Card.
#) Set the switch S1 to TF card boot mode. (refer to `Boot Switch Configuration`_ above)
#) Connect the industrial PC to PC via COM1. Power ON the IPC.
#) After 20 minutes, if the LED on industrial PC stays lit, flashing is completed. Using COM1, you can also find this message **>>>>>>> eMMC Flashing Completed <<<<<<<** which indicates that the system image was downloaded correctly to the eMMC.
#) Power OFF and set the switch S1 to eMMC boot mode. (refer to `Boot Switch Configuration`_ above)

Booting Android OS And Test(Using 7inch as example)
---------------------------------------------------

The first time you start |systemType| OS on the industrial PC will take a little time. But after the first time, |systemType| OS will start quickly.
It is a successful start if you see the |systemType| OS desktop such as the one shown in the figure below:

.. figure:: /Media/ARM/A9/Software/Android_43/android_screen.png
   :align: center
   :figclass: align-center

   *Android Desktop Screen*

SD Test
^^^^^^^

The IPC supports SD card hot-plug. The figure below shows the message when you plug the SD card into IPC.
The IPC will mounts the SD Card to `/mnt/media_rw/` and `/storage/` directory.

.. figure:: /Media/ARM/A9/Software/Android_60/sd_1.png
   :align: center
   :figclass: align-center

   *Serial Message*


USB Flash Disk Test
^^^^^^^^^^^^^^^^^^^

The USB Flash Disk is like the SD Card. The IPC mounts the USB Flash Disk to `/mnt/media_rw/` and `/storage/` directory.

.. figure:: /Media/ARM/A9/Software/Android_60/udisk_1.png
   :align: center
   :figclass: align-center

   *USB flash disk test*

Network Test
^^^^^^^^^^^^

The network uses DHCP to get IP Addresses. You can use the **ethernet app** to set a static IP, to check the obtained IP from the router, and to set the proxy. |br|

.. figure:: /Media/ARM/A9/Software/Android_60/network.png
   :align: center
   :figclass: align-center

   *Ethernet App*

Sound Card Test
^^^^^^^^^^^^^^^

Please open an audio file to test the Sound Card.

.. figure:: /Media/ARM/A9/Software/Android_43/sound.png
   :align: center
   :figclass: align-center

Video Test
^^^^^^^^^^

Please open a video file to test the Video.

.. figure:: /Media/ARM/A9/Software/Android_43/vid_1.png
   :align: center
   :figclass: align-center

.. figure:: /Media/ARM/A9/Software/Android_43/vid_2.png
   :align: center
   :figclass: align-center

HDMI Test
^^^^^^^^^

You can reference this document, :download:`IMX6Q U-boot Setting HDMI Output For Android.pdf <https://chipsee-tmp.s3.amazonaws.com/DVD/IMX6Q/7/Android4.3/Documents/IMX6Q U-boot Setting Hdmi Output For Android.pdf>`, to learn about performing HDMI tests.

.. note::

    HDMI does not support hot-plug. The sound comes from the HDMI monitor, neither the speaker nor the headset on board.

WIFI Test
^^^^^^^^^

You must ensure the IPC has an SDIO Wi-Fi module integrated before performing the Wi-Fi test. If the IPC has an SDIO Wi-Fi Module, you can connect to the Wi-Fi and open a browser to test.

ADB Test
^^^^^^^^

|systemType| OS enables USB Debug by default. |br|
You just need to insert the OTG cable into the IPC, and allow USB debugging. |br|

Also, you can use the ADB tool in the tools directory to test the ADB.

* Unzip it to the root directory of your Windows PC (Drive C), as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Android_43/adb_test_5.png
       :align: center
       :figclass: align-center

       *Unzip adb.rar to c:\\*

* You need to add path of the ADB directory to system's environment variable. Follow the steps described in the figures below to set the environment variable.
    .. figure:: /Media/ARM/A9/Software/Android_43/adb_test_6.png
       :align: center
       :figclass: align-center

       *Open Advance system settings*

    .. figure:: /Media/ARM/A9/Software/Android_43/adb_test_7.png
       :align: center
       :figclass: align-center

       *Open and edit the **Path** system variable*

    .. figure:: /Media/ARM/A9/Software/Android_43/adb_test_8.png
       :align: center
       :figclass: align-center

       *Add path of the ADB directory to the* **Path** *system variable*

* Open the command-prompt on Windows and enter this command `adb version`, as shown on the figure below. The process is successful, if the command-prompt displays the version number of ADB.
    .. figure:: /Media/ARM/A9/Software/Android_43/adb_test_9.png
       :align: center
       :figclass: align-center

       *ADB tool is working*

* Connect the USB-OTG cable from the Windows PC to IPC. You will get a message **Allow USB debugging?**. Please select **Always allow from this computer** and click **Ok**.
    .. figure:: /Media/ARM/A9/Software/Android_60/adb_test_10.png
       :align: center
       :figclass: align-center

       *Enable USB debugging*

You can list the devices attached to the Windows PC with this command.

.. code-block:: powershell

    $ adb devices

.. figure:: /Media/ARM/A9/Software/Android_43/adb_test_11.png
   :align: center
   :figclass: align-center

   *Checking devices attached*

You can install an android app from the Windows PC onto the IPC with this command.

.. code-block:: powershell

    $ adb  install  XXX.apk

.. figure:: /Media/ARM/A9/Software/Android_43/adb_test_12.png
   :align: center
   :figclass: align-center

.. figure:: /Media/ARM/A9/Software/Android_43/adb_test_13.png
   :align: center
   :figclass: align-center

   *Install android app*

Touch Screen Test
^^^^^^^^^^^^^^^^^

Run **MultiTouch** Tester App. |br|
The screen will show the number and position of the touch point when touching the screen.

.. note::

    * Resistive screen expansion board only supports single-touch, and capacitive screen expansion board supports five-point touch as described in the figure below.
    * The 21.5", 19", and 17" capacitive screen supports a ten-point touch.

.. figure:: /Media/ARM/A8/Software/Android/Touch_Test.jpeg
   :align: center
   :figclass: align-center

   Touch screen test (Capacitive touch)

Serial Test
^^^^^^^^^^^

There are five serial ports on the Chipsee IPC: 2 x RS232 and 3 x RS485 (can be customised). Refer to the table below for the available serial device nodes.

.. include:: Resources/serial_table

You can install the **SecureCRT** or **Putty** software on a Windows 7 PC to test the serial ports by following these steps:

* Connect COM1 on industrial PC board to Windows 7 PC.
* Run **Serial Port API** App to communicate with Windows 7 PC, as shown on the figure below.
    .. figure:: /Media/ARM/A9/Software/Android_43/serial_test_1.png
       :align: center
       :figclass: align-center

    .. figure:: /Media/ARM/A9/Software/Android_43/serial_test_2.png
       :align: center
       :figclass: align-center

       *Serial settings*

* Push the button with the label "Send 01010101", you will see something on the Windows 7 PC that looks similar to the figure below.
    .. figure:: /Media/ARM/A8/Software/Android/Serial_Port_Settings_2.jpeg
       :align: center
       :figclass: align-center

       *Serial send test*

* Push the button with the label "Console", to send whatever you like as shown on the figure below.
    .. figure:: /Media/ARM/A8/Software/Android/Serial_Port_Settings_3.jpeg
       :align: center
       :figclass: align-center

       *Serial receive test*

GPIO
^^^^

For the **CS12800F101** IPC, there are 8 GPIO ports that you can set as output or input with LOW as 0V; the HIGH as 3.3V. |br|
Please check the **GPIO Connector** section in :ref:`CS12800F101 <EPC/PPC-A9-101-C>` to know the position of the GPIO Connector. Refer to the table below for the available GPIO nodes on system.

For the **CS10600F070** IPC, there are 8 GPIO ports that you can set as output or input with LOW as 0V; the HIGH as 3.3V. |br|
Please check the **GPIO Connector** section in :ref:`CS10600F070 <EPC/PPC-A9-070-C>` to know the position of the GPIO Connector. Refer to the table below for the available GPIO nodes on system.

.. note::

   The V1 and V2 of CS10600F070 GPIO is not same.

You can use **GPIODemo** app to test the GPIO.

.. figure:: /Media/ARM/A9/Software/Android_60/gpio.png
   :align: center
   :figclass: align-center

   *GPIODemo app*

Modify Logo
+++++++++++

This system supports changing the logo by yourself. There are two ways:

* Replace the logo file in prebuilt images packages, and download images.
* Change the logo without downloading images.

.. note::

   Logo file is one 32bpp, format is bmp.

**Method 1 - Downloading images**

Replace the `prebuilt-xxx/emmc-flash/emmc/logo.bmp` and reference `Prepare Manufacturing Tool and Image`_ and `Downloading Images by using MFGTool`_ to flash the image.

**Method 2 - Don't Download Images**

We will use **MFGTools** and the **Logoflasher** apps to change the logo.

**Use MFGTools to Change LOGO**

* Replace the ``logo.bmp`` file in `Mfgtools-K31452-V1.0\\Profiles\\Linux\\OS Firmware\\files\\ubuntu` with your customised logo file.
* Open and edit the `Mfgtools-K31452-V1.0\\cfg.ini` file and set the ``name`` variable to ``eMMC-Android-Logo`` as shown below.
   .. figure:: /Media/ARM/A9/Software/Android_60/logo_1.png
      :align: center
      :figclass: align-center

.. table:: CS12800F101 P18
   :align: center
   :width: 100%
   :widths: auto

   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | PIN Number                  | GPIO Number                   | Devices File                | Direction                     |
   +=============================+===============================+=============================+===============================+
   | 3                           | gpio106                       | /dev/chipsee-gpio7          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 4                           | gpio30                        | /dev/chipsee-gpio3          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 6                           | gpio95                        | /dev/chipsee-gpio6          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 7                           | gpio87                        | /dev/chipsee-gpio4          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 8                           | gpio29                        | /dev/chipsee-gpio1          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 9                           | gpio28                        | /dev/chipsee-gpio2          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 11                          | gpio94                        | /dev/chipsee-gpio5          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 12                          | gpio130                       | /dev/chipsee-gpio8          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+

.. table:: CS10600F070V1 P21
   :align: center
   :width: 100%
   :widths: auto

   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | PIN Number                  | GPIO Number                   | Devices File                | Direction                     |
   +=============================+===============================+=============================+===============================+
   | 21                          | gpio106                       | /dev/chipsee-gpio7          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 22                          | gpio29                        | /dev/chipsee-gpio1          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 23                          | gpio30                        | /dev/chipsee-gpio3          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 24                          | gpio28                        | /dev/chipsee-gpio2          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 27                          | gpio95                        | /dev/chipsee-gpio6          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 28                          | gpio94                        | /dev/chipsee-gpio5          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 29                          | gpio87                        | /dev/chipsee-gpio4          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 30                          | gpio130                       | /dev/chipsee-gpio8          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+

.. table:: CS10600F070V2 P21
   :align: center
   :width: 100%
   :widths: auto

   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | PIN Number                  | GPIO Number                   | Devices File                | Direction                     |
   +=============================+===============================+=============================+===============================+
   | 21                          | gpio29                        | /dev/chipsee-gpio1          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 22                          | gpio106                       | /dev/chipsee-gpio7          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 23                          | gpio28                        | /dev/chipsee-gpio2          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 24                          | gpio30                        | /dev/chipsee-gpio3          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 27                          | gpio130                       | /dev/chipsee-gpio8          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 28                          | gpio87                        | /dev/chipsee-gpio4          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 29                          | gpio94                        | /dev/chipsee-gpio5          | OUT                           |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+
   | 30                          | gpio95                        | /dev/chipsee-gpio6          | IN                            |
   +-----------------------------+-------------------------------+-----------------------------+-------------------------------+

.. figure:: /Media/ARM/A9/Software/Android_60/logo_1.png
   :align: center
   :figclass: align-center

   *Logo Modify with MFGTool*

**Use Logoflasher to Change Logo**

You can get the `Logoflasher <https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/IMX6Q/Tools/prebuilt-imx6qdl-bootfile-update-20220323.tar.gz>`_ file  and use these tools to make one bootable TF card. |br|
Follow the steps below to change logo

* Use the following commands to make bootable TF card.
     .. code-block:: bash

        $ sudo  tar  zxvf  prebuilt-imx6qdl-bootfile-update-xxx.tar.gz
        $ sudo  cd  prebuilt-imx6qdl-bootfile-update-xxx
        $ sudo  ./mksdcard.sh  --device  /dev/sdX --display 1024600     // resolution

* Put your custom logo file in the first partition ``boot-flash`` directory on the TF Card.
* Set boot mode to **TF card**. You can reference `Boot Switch Configuration`_.
* Power ON the IPC. If you see this message, **>>>>>>> eMMC Flashing Completed <<<<<<<**, you are done:

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
    .. figure:: /Media/ARM/A9/Software/Android_60/android_debug_2.png
       :align: center
       :figclass: align-center

       *Serial output information*

* You can communicate with the system when system boot is complete.

Adb connect via USB OTG
-----------------------

Please refer to the `ADB Test`_ chapter to learn how to set the ADB, how to install an app via ADB, and how to debug with ADB. |br|
You can use the following command to log in to the board and communicate with it.

.. code-block:: powershell

    > adb shell

.. figure:: /Media/ARM/A9/Software/Android_43/android_debug_3.png
   :align: center
   :figclass: align-center

   *ADB Shell*

Use ADB command to install user APP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the ``adb`` command to install an Android App: for example SogouInput.apk. If there is a **SUCCESS** message, as shown on the figure below, then the app installation was successful.

.. code:: powershell

    > adb install SogouInput.apk

.. figure:: /Media/ARM/A8/Software/Android/App_Installed.jpeg
   :align: center
   :figclass: align-center

   Install App

Use ADB command to uninstall user APP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``adb`` command to uninstall an Android app: for example AngryBirds.apk. Follow these commands to uninstall an app.

.. code:: powershell

    > adb shell pm list packages
    > adb uninstall com.rovio.angrybirds

* The `pm list` command gets the full name of the app, as shown on the figure below.

.. figure:: /Media/ARM/A9/Software/Android_43/android_debug_4.png
   :align: center
   :figclass: align-center

   *Uninstall user app*

* The ``uninstall`` command uninstalls the app from the Android system.
* Delete the apk file for the app by using these commands:

.. code:: powershell

    > adb shell
    # cd /system/app/
    # ls
    # rm Browser.apk

Use ADB command to uninstall default APP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``adb`` command to uninstall an Android app: for example *Email.apk*. Follow these commands to uninstall a default app.

.. code:: powershell

    > adb shell

.. code:: bash

    $ su
    su

.. code:: bash

    # cd /system/app
    cd /system/app

.. code:: bash

    # rm Email.apk

.. figure:: /Media/ARM/A9/Software/Android_43/android_debug_5.png
   :align: center
   :figclass: align-center

   *Uninstall default app*

Use ADB command to uninstall default APP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``adb`` command to transport files between the industrial PC and Windows 7 PC.

* Transfer file from the industrial PC to Windows 7 PC using `adb pull` command.
    .. code-block:: powershell

       > adb pull <pathTo_file_on_board> <pathTo_store_file_on_PC>

* Transfer file from the Windows 7 PC to the industrial PC using `adb push` command.
    .. code-block:: powershell

       > adb push <pathTo_file_on_PC> <pathTo_store_file_on_board>

For example, copy ``<ADT>\sdk\platform-tools\chipsee.txt`` from Windows PC to IPC:

.. code-block:: powershell

   > adb push chipsee.txt /chipsee.txt

Copy ``/testFile.txt`` from IPC to Windows PC:

.. code-block:: bash

   > adb pull /testFile.txt testFile.txt

Adb connect via internet
------------------------

#) The Ethernet port on the industrial PC and the host machine (Windows 7 PC) should connect to the network. Check Ethernet configuration for the industrial PC using the command below.
    .. code:: powershell

       # netcfg
       lo       UP            127.0.0.1/8   0x00000049 00:00:00:00:00:00
       can0     DOWN          0.0.0.0/0   0x00000080 00:00:00:00:00:00
       eth0     UP            192.168.6.176/24  0x00001043 1e:ed:19:27:1a:b3

#) If the industrial PC's Ethernet is not configured, configure the Ethernet using the ``ifconfig``/``netcfg`` command as shown below.
    .. code:: powershell

        # netcfg eth0 dhcp

#) Configure the ADB Daemon to use an Ethernet connection using the ``setprop`` command, as shown below.
    .. code:: powershell

        # setprop service.adb.tcp.port 5555

#) If the network is configured successfully using the steps above, then Restart service ``adbd`` on the Windows 7 PC.
    .. code:: powershell

        # stop adbd
        # start adbd

#) On the host machine (Windows 7 PC) use the following commands to establish the ``adb`` connection.
    .. code:: powershell

        $ adb kill-server
        $ adb start-server
        $ adb connect :5555

#) Verify the device connectivity, by executing the following commands. If connected, find the device name listed as``IPADDRESS:PORT``.
    .. code:: powershell

        $ adb devices
        List of devices attached
        192.168.6.176:5555      device

#) An example of using the ``adb`` command to install software for Android. Make sure the ``"**".apk`` file is at the current folder, and export the adb path.
    * Use the argument ``–s`` to assign the device to use over the internet.

    .. code::

       $ adb –s 192.168.1.117:5555 install "**".apk

Android App Development
=======================

In this section, we will introduce the development of an Android app with Android Studio on Windows. We assume that the USB is OTG model and the driver is already installed. (See `Adb connect via USB OTG`_)

Example — Develop a ``HelloWorld`` Program
------------------------------------------

#) Start a new Android Studio project
    .. figure:: /Media/ARM/A9/Software/Android_60/app_dev_1.png
       :align: center
       :figclass: align-center

       *New Project*

#) Configure your new project
    .. figure:: /Media/ARM/A9/Software/Android_60/app_dev_2.png
       :align: center
       :figclass: align-center

       *Project Configuration*

#) Select the form factors your application will run on
    .. figure:: /Media/ARM/A9/Software/Android_60/app_dev_3.png
       :align: center
       :figclass: align-center

       *App form factor*

#) Select one Empty Activity
    .. figure:: /Media/ARM/A9/Software/Android_60/app_dev_4.png
       :align: center
       :figclass: align-center

       *Add Activity*

#) Customize the Activity
    .. figure:: /Media/ARM/A9/Software/Android_60/app_dev_5.png
       :align: center
       :figclass: align-center

       *Customize Activity*

#) Develop the App
    .. figure:: /Media/ARM/A9/Software/Android_60/app_dev_6.png
       :align: center
       :figclass: align-center

       *App Development Interface*

#) Run app on target IPC
    .. figure:: /Media/ARM/A9/Software/Android_60/app_dev_7.png
       :align: center
       :figclass: align-center

       *HelloWorld Program*

.. note::

    If the USB is not configured as an OTG model, you can copy and install the file ``HelloWorld.apk`` from the project folder ``HelloWorld/bin/``, or install the ``HelloWorld.apk`` via the internet (See `Adb connect via internet`_).

For more resources about Android development, visit these links: |br|

    `<https://developer.android.com/guide/index.html>`_
    `<https://developer.android.com/develop/index.html>`_
    `<http://developer.android.com/support.html>`_
    `<http://blog.apptopia.com/android-development-forums/>`_
    `<http://androidforums.com/application-development/>`_

.. include:: Resources/support