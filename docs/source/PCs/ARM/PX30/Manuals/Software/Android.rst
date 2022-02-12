.. |systemType| replace:: Android
.. |filename| replace:: prebuilt-jb-hmi-XXXX.tar.gz
.. |folder_name| replace:: ~/Prebuilt-cs-androidXXXXX/prebuilt-sd/
.. |bash_script| replace:: ./mkmmc-android.sh



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
   |   V1.0   | 2021-12-09|  Randy | Initial Version |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

   *CS80480T050*   *CS80600T080*   *CS10600T070*   *CS80480T070*   *CS10768T097*

.. _db_pkg_android:

**PREBUILT FILES PACKAGE:**

Prebuilt files for the various industrial PCs can be found in the :ref:`OS Downloads <AM335X_OSDownloads>`. |br|
Below are the links to the prebuilt files for each industrial PC model.

+ :ref:`CS80480T050 <CS80480T050-android>`
+ :ref:`CS80600T080 <CS80600T080-android>`
+ :ref:`CS10600T070 <CS10600T070-android>`
+ :ref:`CS80480T070 <CS80480T070-android>`
+ :ref:`CS10768T097 <CS10768T097-android>`


.. rubric:: System Features

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | System        | Android 4.1                      |
   +---------------+----------------------------------+

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Files Package to re-flash the system.

Power Supply Unit (PSU) with the appropriate voltages, as follows:

+ Products with 5" display panel require 6V to 36V PSU
+ Products with 7" to 10.1" display panel and larger require 6V to 42V PSU

* USB to serial cable for debugging Chipsee Industrial Embedded Computers (Chipsee IPC)
* TF Card to create a bootable storage for re-flashing the system. Use the prebuilt files :ref:`link above <db_pkg_android>` to re-flash the system.

.. include:: Resources/Hardware_Req

Software Requirements
---------------------

* |systemType| OS Prebuilt Files Package (from the link above)
* ADT for Windows
* Android USB driver (for Windows)

.. include:: Resources/Starting

.. include:: Resources/SD_Bootable

How flash Android to NAND
-------------------------

The Prebuilt Files Package has a shell tool that can help create a bootable NAND card using a Linux platform (such as desktop PC or Virtual
Machine running Ubuntu 14.04 distribution). |br|
Follow the steps below to create a bootable NAND card:

#) Copy the Prebuilt Files Package to a Linux environment (such as Ubuntu 14.04).
#) Insert the SD card into your computer. If you are using virtual machines, please ensure the SD card is mounted to the Linux operating system.
#) Confirm the SD card mount point, ``/dev/sdX``，(e.g., ``/dev/sdc`` or ``/dev/sdb``, be sure to use the right one). In a Linux system, you can use the command below to find out what *X* is.
    .. code:: bash

        $ sudo fdisk –l

#) Copy the prebuilt file ``prebuilt-jb-hmi-XXXX.tar.gz`` to somewhere(such as $HOME).
#) Extract the prebuilt file ``prebuilt-jb-hmi-XXXX.tar.gz``
    .. code:: bash

        $ tar -xzvf prebuilt-jb-hmi-XXXX.tar.gz

#) Go to the folder ``prebuilt-jb-hmi-XXXX/prebuilt-nand/``
    .. code:: bash

        $ cd ~/prebuilt-jb-hmi-XXXX/prebuilt-nand/

#) Use the following command to flash the |systemType| OS to the NAND card
    .. code:: bash

        $ sudo ./mkmmc-android-nand.sh --device  /dev/sd<?>

    .. note::

        * sd<?> means the SD card mount point, (e.g., ``/dev/sdc`` or ``/dev/sdb``) in Ubuntu system.
        * The recommended SD card should be Sandisk Class4 level SD card or above.

#) The bootable NAND Card is now ready. Power OFF the industrial PC and insert the NAND Card.
#) Set the DIP switch to NAND BOOT mode. (refer to `DIP Switch Configuration`_ above)
#) Connect the industrial PC to PC via COM1. Power ON the IPC.
#) After 20 minutes, if the LED on industrial PC stays lit, flashing is completed. Using COM1, you can also find this message **>>>>>>> eMMC Flashing Completed <<<<<<<** which indicates that the system image was downloaded correctly to the eMMC.
#) Power OFF the IPC and set the DIP switch to eMMC BOOT mode. (refer to `DIP Switch Configuration`_ above)

Start |systemType| OS
---------------------
The first time you start |systemType| OS on the industrial PC will take a little time. But after the first time, |systemType| OS will start quickly.
When the |systemType| OS starts up, you will see the Chipsee Logo on the LCD screen.
It is a successful start if you see the |systemType| OS desktop such as the one shown in the figure below:

.. figure:: /Media/ARM/A8/Software/Android/Startup_Screen.jpeg
   :align: center
   :figclass: align-center

   Android OS start-up screen

Tests
-----

Touch screen test
^^^^^^^^^^^^^^^^^

Run **MultiTouch** Tester App. |br|
The screen will show the number and position of the touch point when touching the screen.

.. note::

    Resistive screen expansion board only supports single-touch, and capacitive screen expansion board supports five-point touch as described in the figure below.

.. figure:: /Media/ARM/A8/Software/Android/Touch_Test.jpeg
   :align: center
   :figclass: align-center

   Touch screen test (Capacitive touch)

After working for some time, the resistive touch screen may not be accurate. The user must run a touch screen calibration test. |br|
Run **Chipsee TouchCal** App as described in the figure below.

.. figure:: /Media/ARM/A8/Software/Android/Touch_Test_2.jpeg
   :align: center
   :figclass: align-center

   Touch screen calibration test (Resistive touch)

Buzzer test
^^^^^^^^^^^

Run **Chipsee Buzzer** App. |br|
Push the *"OpenBuzzer"* button to start the buzzer sound. |br|
Push the *"CloseBuzzer"* button to stop the sound.

Gravity sensor test
^^^^^^^^^^^^^^^^^^^

You can test the gravity sensor by whirling the screen.

* Run **SensorList** App.
* In the *"Analog Device 3 axis accelerometer"* option, you can see real-time changes of the three-axis acceleration value curve, as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Android/Gravity_Sensor_Test.jpeg
   :align: center
   :figclass: align-center

   Real-time acceleration curve

* You can also test gravity using a gravity sensing game, such as "NFS shift" or "Tilt 3D laby". If you use "NFS shift", please run the **ChipseeSensorTool** app to adjust the direction of the axis by selecting "Invert X-axis" and "Swap X/Y axes". If you use other games, please adjust the settings as default.

Audio IO test
^^^^^^^^^^^^^

Insert the microphone and earphones into the Audio IO interface (Audio IN coloured pink, Audio OUT coloured light blue). |br|
Start **Talking Tom** App (Tom Cat). |br|
Speak into the microphone, Tom the cat will repeat spoken content.

Serial test
^^^^^^^^^^^

There are four serial ports on the Chipsee IPC: 2 X RS232 and 2 X RS485. Refer to the table below for the available serial device nodes.

.. include:: Resources/serial_table

You can install the **SecureCRT** or **Putty** software on a Windows 7 PC to test the serial ports by following these steps:

* Connect COM1 on industrial PC board to Windows 7 PC.
* Run **Serial Port API** App to communicate with Windows 7 PC, as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Android/Serial_Port_Settings.jpeg
   :align: center
   :figclass: align-center

   Serial settings

* Push the button with the label "Send 01010101", you will see something on the Windows 7 PC that looks similar to the figure below.

.. figure:: /Media/ARM/A8/Software/Android/Serial_Port_Settings_2.jpeg
   :align: center
   :figclass: align-center

   Serial send test

* Push the button with the label "Console", to send whatever you like as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Android/Serial_Port_Settings_3.jpeg
   :align: center
   :figclass: align-center

   Serial receive test


USB device test
^^^^^^^^^^^^^^^

**USB-WiFi**

The |systemType| OS supports USB-WiFi (RTL8188). You can find the device in settings, as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Android/USB_WiFi_Settings.jpeg
   :align: center
   :figclass: align-center

   USB-WiFi

**USB-Camera**

The |systemType| OS supports USB-Camera. You can find the device in settings, as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Android/USB_Camera_Settings.jpeg
   :align: center
   :figclass: align-center

   USB-Camera

.. include:: Resources/Logo_Modify

IP settings
-----------
To make changes to the IP address, follow these steps:

* Search the **boot partition** for the ``uEnv.txt`` file.
* Open and edit the file ``uEnv.txt`` with any text editor.
    .. code::

       bootargs=console=ttyO0,115200n8 androidboot.console=ttyO0 mem=512M root=/dev/mmcblk0p2 rw rootfstype=ext4 rootwait init=/init ip=off

* Edit the part with **ip=value**, where value = off OR <iPv4 address>:::<Subnet mask>
    For example:
    .. code::

       bootargs=console=ttyO0,115200n8 androidboot.console=ttyO0 mem=512M root=/dev/mmcblk0p2 rw rootfstype=ext4 rootwait init=/init ip=192.168.1.111:::255.255.0.0

.. note::

    Inputting wrong details could harm the industrial PC and because of that you should backup the file before making any changes. This can help you reverse changes easily if an error occurs.

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
* Open the **SecureCRT** or **Putty** software on the Windows 7 PC.
* Power ON the industrial PC. You will see the serial output information as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Android/Serial_Debug.jpeg
   :align: center
   :figclass: align-center

   Serial output information


Adb connect via USB OTG
-----------------------

#) Download `Oracle JDK 6 <https://www.oracle.com/technetwork/java/javase/downloads/index.html>`_ and `Android Studio SDK <https://developer.android.com/sdk/index.html>`_ for Windows. We suggest you download JDK-6u45.

#) Install Oracle JDK 6 and Android Studio SDK for Windows.

#) Extract the file somewhere (the name for the extracted folder is ADT).

#) The ADB command is in the ``<ADT>\sdk\platform-tools`` folder.

#) Optionally, you can add the location of the SDK’s primary tools directory to your system PATH by following these steps:
    * Right-click on My Computer, and select Properties.
    * Under the Advanced tab, hit the Environment Variables button.
    * In the dialogue that comes up, double-click on Path (under System Variables).
    * Add the full path to the tools\ directory to the path.

#) Install Android USB driver on Windows:
    * Copy the ``usb_driver`` folder on the CD to a folder on the Windows 7 PC.
    * Boot the board as normal and wait until shell prompt is available (disconnect the micro-B USB cable).
    * Connect a micro-B USB cable between the board and Windows 7 PC.
    * If it is proceeding as planned, Windows will recognise the new hardware and ask you to install drivers for it.
    * Right click on the hardware. Click on install driver.
    * Choose the answer **No, not this time** to the question about running Windows Update to search for software.
    * Choose **Install the hardware that I manually select from a list (Advanced)** this is the 2nd option, then click **Next**.
    * Browse to your driver folder (``\usb_driver``). and look for a ``.inf`` file.
    * Select ``android_winusb.inf`` and click **Open** then **OK**. It’s the only file in the folder, so you shouldn’t go wrong.
    * Select **Android ADB Interface** then click the **Next** button.
    * A warning will appear, answer **Yes** but read the warning, anyway.
    * When the wizard finishes, click the **Close** button .
    * Now you can see it installed the driver successfully, as shown on the figure below.

    .. figure:: /Media/ARM/A8/Software/Android/ADB_Driver.jpeg
       :align: center
       :figclass: align-center

       ADB Driver

#) Test ADB by following these steps:
    * Press the **Win+r** key combination to open the *Run Command* dialogue box.
    * Type **cmd** and press enter.
    * Execute the commands below in the command prompt.

    .. code:: powershell

        > cd <ADT>\sdk\platform-tools\
        > adb kill-server
        > adb start-server
        > adb devices
        > adb shell

    * If the ``#`` prompt appears at the beginning of the command line, it means we connected the industrial PC with the Windows 7 PC successfully as shown on the figure below.

    .. figure:: /Media/ARM/A8/Software/Android/ADB_Shell.jpeg
       :align: center
       :figclass: align-center

       ADB Command

    * Now you can use Linux commands like ``ls``, ``cd`` and so on. Press **Ctrl + C** to exit the shell and return to the Windows system.

#) Use the ``adb`` command to install an Android App: for example SogouInput.apk. If there is a **SUCCESS** message, as shown on the figure below, then the app installation was successful.
    .. code:: powershell

        > adb install SogouInput.apk

    .. figure:: /Media/ARM/A8/Software/Android/App_Installed.jpeg
       :align: center
       :figclass: align-center

       Install App

#) Use ``adb`` command to uninstall an Android app: for example SogouInput.apk. Follow these commands to uninstall an app.
    .. code:: powershell

        > adb shell pm list packages
        > adb uninstall com.sohu.inputmethod.sogou

    * The ``pm list`` command gets the full name of the app, as shown on the figure below.

    .. figure:: /Media/ARM/A8/Software/Android/App_Installed.jpeg
       :align: center
       :figclass: align-center

       Command ``pm list`` to get app’s name

    * The ``uninstall`` command uninstalls the app from the Android system.
    * Delete the apk file for the app by using these commands:

    .. code:: powershell

        > adb shell
        # cd /system/app/
        # ls
        # rm Browser.apk

#) Use ``adb`` command to transport files between the industrial PC and Windows 7 PC.
    * Transfer file from the industrial PC to Windows 7 PC using ``adb pull`` command.

    .. code:: powershell

        > adb pull <pathTo_file_on_board> <pathTo_store_file_on_PC>

    * Transfer file from the Windows 7 PC to the industrial PC using ``adb push`` command.

    .. code:: powershell

        > adb push <pathTo_file_on_PC> <pathTo_store_file_on_board>


Adb connect via internet
------------------------

#) The Ethernet port on the industrial PC and the host machine (Windows 7 PC) should connect to the network. Check Ethernet configuration for the industrial PC using the command below.
    .. code:: powershell

        # netcfg
        lo       UP    127.0.0.1       255.0.0.0       0x00000049
        eth0     UP    192.168.1.117/24   255.255.252.0   0x00001043

#) If the industrial PC's Ethernet is not configured, configure the Ethernet using the ``ifconfig``/``netcfg`` command as shown below.
    .. code:: powershell

        # netcfg eth0 dhcp

#) Configure the ADB Daemon to use an Ethernet connection using the ``setprop`` command, as shown below.
    .. code:: powershell

        # setprop service.adb.tcp.port 5555

#) If the network is configured successfully using the steps above, then Restart ``service adbd`` on the Windows 7 PC.
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
        emulator-5554    device
        192.168.1.117:5555  device

#) An example of using the ``adb`` command to install software for Android. Make sure the ``"**".apk`` file is at the current folder, and export the adb path.
    * Use the argument ``–s`` to assign the device to use over the internet.

    .. code::

       $ adb –s 192.168.1.117:5555 install "**".apk



Android App Development
=======================

In this section, we will introduce the development of an Android app with Eclipse on Windows. We assume that the USB is OTG model and the driver is already installed. (See `Adb connect via USB OTG`_)

Preparation
-----------

#) Download and install `Eclipse IDE <https://www.eclipse.org/downloads/packages/release/2021-12/r/eclipse-ide-java-developers>`_.
#) Go to the ``/eclipse`` folder, start eclipse.exe.
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_1.jpeg
       :align: center
       :figclass: align-center

       Start eclipse

#) Click Windows-->Android SDK Manager to open SDK Manager.
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_2.jpeg
       :align: center
       :figclass: align-center

       Android SDK Manager

#) Click Tools-->Options, check the ``Force`` box and click close.
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_3.jpeg
       :align: center
       :figclass: align-center

       Android SDK Manager Settings

#) Choose the API, such as Android4.2.2(API 17), then click the **Install packages** button to start the download and installation of API packages.
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_4.jpeg
       :align: center
       :figclass: align-center

       Install API packages

#) Downloading and installing the packages will take some time. When the process completes, close the Android SDK Manager.

Example — Develop a ``HelloWorld`` Program
------------------------------------------

#) Click File-->New-->Android Application Project
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_5.jpeg
       :align: center
       :figclass: align-center

       New Application

#) Click on the **Next** button until the app project is created. Connect the industrial PC to Windows 7 PC via the USB cable (A-A). If the connection is successful, you will see the device in the DDMS window (Windows-->Open Perspective-->Other-->DDMS)
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_6.jpeg
       :align: center
       :figclass: align-center

       DDMS

#) You can capture the desktop of Android
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_7.jpeg
       :align: center
       :figclass: align-center

       Capture Android Desktop

#) Click run, and choose the device
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_8.jpeg
       :align: center
       :figclass: align-center

       Run HelloWorld Program

#) Result
    .. figure:: /Media/ARM/A8/Software/Android/App_Dev_9.jpeg
       :align: center
       :figclass: align-center

       HelloWorld Program

.. note::

    If the USB is not configured as an OTG model, you can copy and install the file ``HelloWorld.apk`` from the project folder ``HelloWorld/bin/``, or install the ``HelloWorld.apk`` via the internet (See `Adb connect via internet`_).

.. include:: Resources/support