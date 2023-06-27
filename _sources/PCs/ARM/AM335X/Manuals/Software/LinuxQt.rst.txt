:pdf-build: False


.. |systemType| replace:: Linux QT
.. |filename| replace:: prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-sd-yyyymmdd.tar.gz
.. |folder_name| replace:: ~/prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-sd-yyyymmdd
.. |bash_script| replace:: ./mksdcard.sh
.. |user| replace:: root
.. |pswd| replace:: empty


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
   |   V1.0   | 2021-12-09|  Randy | Initial Version |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

   *CS80480T050*   *CS80600T080*    *CS10600T101*   *CS10600T070*   *CS80480T070*   *CS10768T097*

.. _db_pkg_linux:

**PREBUILT FILES PACKAGE:**

Prebuilt files for the various industrial PCs can be found in the :ref:`OS Downloads <AM335X_OSDownloads>`. |br|
Below are the links to the prebuilt files for each industrial PC model.

+ :ref:`CS80480T050 <CS80480T050-linuxQt>`
+ :ref:`CS80600T080 <CS80600T080-linuxQt>`
+ :ref:`CS80600T101 <CS10600T101-linuxQt>`
+ :ref:`CS10600T070 <CS10600T070-linuxQt>`
+ :ref:`CS80480T070 <CS80480T070-linuxQt>`
+ :ref:`CS10768T097 <CS10768T097-linuxQt>`


.. rubric:: System Features

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | System        | LinuxQt 4.8 & LinuxQt 5.5        |
   +---------------+----------------------------------+

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Files Package to re-flash the system.

* Power Supply Unit (PSU) with the appropriate voltages, as follows:
   + Products with 5" display panel require 6V to 36V PSU
   + Products with 7" to 10.1" display panel and larger require 6V to 42V PSU

* USB to serial cable for debugging Chipsee Industrial Embedded Computers (Chipsee IPC)
* TF Card to create a bootable storage for re-flashing the system. Use the prebuilt files :ref:`link above <db_pkg_linux>` to re-flash the system.

.. include:: Resources/Hardware_Req

Software Requirements
---------------------

* |systemType| OS Prebuilt Files Package (from the link above)
* Useful tools for Qt development

.. note::

    In this documentation, all the commands are executed with ``root`` user privileges.

.. include:: Resources/Starting

.. include:: Resources/SD_Bootable

How to flash Linux to eMMC
--------------------------

The Prebuilt Files Package has a shell tool that can help create a bootable SD card using a Linux platform (such as desktop PC or Virtual
Machine running Ubuntu 14.04 distribution). |br|
Follow the steps below to create a bootable SD card:

#) Copy the Prebuilt Files Package to a Linux environment (such as Ubuntu 14.04).
#) Insert the SD card into your computer. If you are using virtual machines, please ensure the SD card is mounted to the Linux operating system.
#) Confirm the SD card mount point, ``/dev/sdX``，(e.g., ``/dev/sdc`` or ``/dev/sdb``, be sure to use the right one). In a Linux system, you can use the command below to find out what *X* is.
    .. code:: bash

        $ sudo fdisk –l

#) Copy the prebuilt file ``prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-emmc-yyyymmdd.tar.gz`` to somewhere(such as $HOME).
#) Extract the prebuilt file ``prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-emmc-yyyymmdd.tar.gz``
    .. code:: bash

        $ tar -xzvf prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-emmc-yyyymmdd.tar.gz

#) Go to the folder ``prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-emmc-yyyymmdd``
    .. code:: bash

        $ cd ~/prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-emmc-yyyymmdd

#) Use the following command to flash the |systemType| OS to the SD card
    .. code:: bash

        $ sudo ./mksdcard.sh --device  /dev/sd<?>

    .. note::

        * sd<?> means the SD card mount point, (e.g., ``/dev/sdc`` or ``/dev/sdb``) in Ubuntu system.
        * The recommended SD card should be Sandisk Class4 level SD card or above.

#) The bootable SD Card is now ready. Power OFF the industrial PC and insert the SD Card.
#) Set the DIP switch to SD BOOT mode. (refer to `DIP Switch Configuration`_ above)
#) Connect the industrial PC to PC via COM1. Power ON the IPC.
#) After 20 minutes, if the LED on industrial PC stays lit, flashing is completed. Using COM1, you can also find this message **>>>>>>> eMMC Flashing Completed <<<<<<<** which indicates that the system image was downloaded correctly to the eMMC.
#) Remove the SD card and Power OFF the IPC.
#) Set the DIP switch to eMMC BOOT mode (refer to `DIP Switch Configuration`_ above) and Power ON the IPC.

Start |systemType| OS
---------------------
The first time you start |systemType| OS on the industrial PC will take a little time. But after the first time, |systemType| OS will start quickly.
When the |systemType| OS starts up, you will see the Chipsee Logo on the LCD screen.
It is a successful start if you see the |systemType| OS desktop such as the one shown in the figure below:

.. figure:: /Media/ARM/A8/Software/Linux/Startup_Screen.jpeg
   :align: center
   :figclass: align-center

   Chipsee Linux QT OS start-up screen

Tests
-----

Touch screen and buzzer test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the screen, the mouse arrow stays in a position that triggers the buzzer sounds, indicating that touch and buzzer work properly. |br|
After working for some time, the resistive touch screen may not be accurate. The user must run a touch screen calibration test. |br|
Click on the **Chipsee** icon on the desktop. Select **Calibrate Screen** to calibrate it, just as described in the figure below.

.. figure:: /Media/ARM/A8/Software/Linux/Touch_Screen_Test.jpeg
   :align: center
   :figclass: align-center

   Resistive touch screen calibration app

The buzzer will sound when the screen is touched, if you want to disable it, you can do this:

* On capacitive touchscreen:
    .. code-block:: bash

        # echo 0 > /sys/devices/ocp.3/44e0b000.i2c/i2c-0/0-0038/buzopen

* On resistive touchscreen:
    .. code-block:: bash

        # echo 1 > /sys/devices/ocp.3/44e0d000.tscadc/tsc/buzopen

    where:
        + 0 = disable
        + 1 = enable

Audio and video test
^^^^^^^^^^^^^^^^^^^^

Insert the microphone and earphones into the Audio IO interface (Audio IN coloured pink, Audio OUT coloured light blue). |br|
as shown on the figure below, click the **Multimedia** icon on desktop then choose the **MPEG-4+AAC Dec** codec to test.

.. figure:: /Media/ARM/A8/Software/Linux/Audio_Video_Test.jpeg
   :align: center
   :figclass: align-center

   Audio and Video

3D Test
^^^^^^^

Click the **3D** icon on desktop, then choose **Film TV** to test perform 3D testing as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Linux/3D_Test.jpeg
   :align: center
   :figclass: align-center

   3D test Film TV

Serial test
^^^^^^^^^^^

There are four serial ports on the Chipsee IPC: 2 X RS232 and 2 X RS485. The COM1(RS232) is used as the debug serial port. Users can communicate with the OS via COM1.
Refer to the table below for the available serial device nodes.

.. include:: Resources/serial_table

If you want to use COM1 as a normal serial port, you can re-configure the port by following these steps:

* Open and edit the file ``/etc/inttab`` with any text editor.
* At the end of the file, edit this line ``S:2345:repawn:/sbin/getty 115200 ttyO0`` to

.. code-block:: bash

    # S:2345:repawn:/sbin/getty 115200 ttyO0

* The code-block above, comments off the last line making it possible to use all the four serial ports as normal serial ports.
* You can verify the changes by running a serial test.
* Run a serial test:
    + Install **SecureCRT** or **Putty** software on a Windows 7 PC and use it to perform the serial port testing.
    + Click on the **Chipsee** icon on desktop, select **ChipseeTest** to run the **SerialTest** app to communicate with Windows 7 PC.
    + From the **ChipseeTest** app, search for the serial area then configure the following settings, as shown on the figure below.
        - set Com to COM2
        - set Baud to 115200
        - click on the **Open** button

        .. figure:: /Media/ARM/A8/Software/Linux/ChipseeTest_Screen.jpeg
           :align: center
           :figclass: align-center

           ChipseeTest

    + It will send the string *Succeed in sending message!!!* every two seconds through the serial port to the Windows 7 PC.
    + Click on the **SendMSG** button to send the string *Succeed in sending message-manual!!!*.
    + Every two seconds, it will read the received buffer and show the result to the received area.

CAN test
^^^^^^^^

To perform the test, the user will need the following: **2 x Embedded Industrial Computers, 2 x CAN bus connectors, 1 x 120Ω resistor, and oscillometer.**

* The user will connect the two CAN bus connectors directly to each other for testing.

    Between CANH and CANL you should use a 120Ω resistor

* At the CAN area, click on the **Open** button, then click on the **SendMSG** button to send message: *11 22 33 44 55 66 77 88*
* On both embedded industrial PCs, you should see the message shown at the received area.
* If you have one embedded industrial PC, you can use an **oscillometer** to see the result.


GPIO test
^^^^^^^^^

There are (4) four input and (4) four output pins. LOW is 0V, HIGH is 5V. |br|
The GPIO input terminals connect to the GPIO output terminals, respectively. IN1-4 corresponds to OUT1-4. |br|
As a result, if you set the GPIO_OUT area, you will see the GPIO_IN region change as well. |br|
You can control the LED light on the industrial PC by setting the LED **ON** or **OFF**.

.. include:: Resources/gpio_table

You can read and write the GPIO by following the steps below. For this example, we are going to use **gpio49** (OUT1).

* Use this command to export gpio.
    .. code-block:: bash

        # echo 49 > /sys/class/gpio/export

* Use this command to check if the directory ``/sys/class/gpio/gpio49/`` exist before writing to it
    .. code-block:: bash

        # find /sys/class/gpio/gpio49/

* Use this command to write gpio
    .. code-block:: bash

        # echo 1 > /sys/class/gpio/gpio49/value

* Use this command to read gpio
    .. code-block:: bash

        # cat /sys/class/gpio/gpio49/value

Network
^^^^^^^

To view the network information on the industrial PC, follow these steps:

* Click on the **Network** tab, then click the **Ifconfig** button to view the network information on the industrial PC.
* Click on the **Refresh** button to restart the network service which will take five or six seconds to finish.

The figure below is an illustration of the network information on the industrial PC.

.. figure:: /Media/ARM/A8/Software/Linux/Network_Test.jpeg
    :align: center
    :figclass: align-center

    View Network Information


Date and Time
^^^^^^^^^^^^^

Click the **Edit** icon at the time display area to set the time and date, as shown on the figure below.

.. figure:: /Media/ARM/A8/Software/Linux/Date_Time_Test.jpeg
    :align: center
    :figclass: align-center

    Set Date and Time

* Check the system time
    .. code-block:: bash

        # date

* Set the system time
    .. code-block:: bash

        # date –s "2014-03-15 10:30:30"

* Check RTC
    .. code-block:: bash

        # hwclock

* Write RTC
    .. code-block:: bash

        # hwclock -w

* Modify the time zone to a different timezone, such as China
    .. code-block:: bash

        # ln -sf /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime

Backlight
^^^^^^^^^

Modify this file ``/sys/class/backlight/backlight`` to adjust the screen brightness. Brightness ranges from 0 to 100 where 0 means no backlight, and 100 is the MAX brightness value. |br|
For example, you can adjust the screen brightness using this command:

.. code-block:: bash

    # echo 50 > /sys/class/backlight/backlight.10/Brightness

WiFi
^^^^

The |systemType| OS has a WiFi module. If you want to get Wifi module to work, you need to edit the configuration file: ``/etc/wpa_supplicant.conf``.

#) Set SSID and password in the config file, as shown in the code-block below:
    .. code-block:: bash
        :linenos:
        :emphasize-lines: 2-5

        # vi /etc/wpa_supplicant.conf
        network={
                ssid="Chipsee"    //set your wifi ssid
                psk="1chipsee234567890"   //set your wifi password
        }


#) Launch the Wifi
    .. figure:: /Media/ARM/A8/Software/Linux/WiFi_Test_1.jpeg
        :align: center
        :figclass: align-center

    .. figure:: /Media/ARM/A8/Software/Linux/WiFi_Test_2.jpeg
        :align: center
        :figclass: align-center

    .. figure:: /Media/ARM/A8/Software/Linux/WiFi_Test_3.jpeg
        :align: center
        :figclass: align-center

        Launching WiFi

#) After a few minutes, you can use the WiFi


.. include:: Resources/Logo_Modify

.. note::

    If you want to run the system from NAND Flash and change the Logo, you should change the logo first then flash the NAND. |br|
    If the system is running in the NAND Flash, you can rewrite the ``u-boot.img`` file. |br|
    Boot from uSD card, hit the **space** key after power on, to switch boot into **u-boot** mode ``U-Boot #``. |br|
    Rewrite the ``u-boot.img`` file.

    .. code:: bash

       U-Boot # nand erase.chip

    Reboot


|systemType| OS debug
=====================

In this section, we will discover how to view the |systemType| system via the serial port on a Windows 7 PC. |br|
Also, we will discover how to debug using NFS on a Ubuntu Linux PC. |br|

.. include:: Resources/SerialPort_Debug

.. include:: Resources/NFS_Debug

Linux App Development
=====================

In this section, we will introduce how to develop applications for the industrial computer in Linux.

Preparation
-----------

**Software**:

#) Ubuntu system, we suggest Ubuntu 14.04.5 LTS x64
#) Install Qtcreator package: `qt-linux-opensource-5.1.0-x86-offline.run <https://download.qt.io/archive/qt/5.1/5.1.0/>`_.
#) Install package `ti-sdk-am335x-evm-07.00.00.00-Linux-x86-Install.bin <https://software-dl.ti.com/sitara_linux/esd/AM335xSDK/07_00_00_00/index_FDS.html>`_ provided by TI.


Steps
-----

#) We assume you have created a GUI program using Qtcreator, such as ``HelloWorld``.
#) Configure the environment variables for the TI package by using the command below to source a script file included in the TI package.
    .. code-block:: bash

        $ source /opt/ti-sdk-am335x-evm/linux-devkit/environment-setup

#) Change directory into the folder of your GUI program (``HelloWorld``) and run these commands:
    .. code-block:: bash

        $ qmake –project
        $ qmake
        $ make

    Now there will be a file which you can run in the industrial PC. You can use the command ``file HelloWorld``, to check if the file can be executed in the ARM platform.

#) Put the file ``HelloWorld`` on the industrial PC. Then run the command below in the Ubuntu Linux system (communicate via COM1).
    .. code-block:: bash

        # ./Hello

    The program will start running

#) Add application to the desktop of Matrix
    * Put your program file ``HelloWorld`` into a folder which can be found by the system such as, ``/usr/bin``.
    * Put the program’s icon into the folder: ``/usr/share/matrix-gui-2.0/apps/images/``. For example, ``/usr/share/matrix-gui-2.0/apps/images/YOURAPPIMG.png``
    * Go to the folder ``/usr/share/matrix-gui-2.0/apps/``, then create a new folder named ``HelloWorld`` using this command ``$ mkdir HelloWorld``.
    * Change directory to ``HelloWorld`` folder, then create a new file named ``HelloWorld.desktop`` using the command ``$ touch HelloWorld.desktop``.
    * Edit the ``HelloWorld.desktop`` file using the command:

        .. code-block:: bash
           :linenos:

           #!/usr/bin/env xdg-open[Desktop Entry] Name= YOURAPPNAME // Can be changed
           GenericName=Demo App
           Icon=/usr/share/matrix-gui-2.0/apps/images/YOURAPPIMG.png
           Exec=YOURAPPNAME
           Type=Application
           ProgramType=gui

    * Refresh the system by clicking on Settings-->Refresh Matrix, then click on run.
    * You will see your application’s icon on the desktop after refreshing. If the icon does not change in time, you need to reboot your system.

New development kit
-------------------

#) Open a Terminal in Ubuntu using the **CTRL + ALT + T** key combination. Enter the command below.
    .. code-block:: bash

        # source /usr/local/ti-sdk-am335x-evm/linux-devkit/environment-setup

#) Then open QtCreator
    .. code-block:: bash

        # /opt/Qt5.1.0/Tools/QtCreator/bin/qtcreator &

    Choose Tool-->Options:

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_1.jpeg
        :align: center
        :figclass: align-center

        New Device

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_2.jpeg
        :align: center
        :figclass: align-center

        Properties of the Device

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_3.jpeg
        :align: center
        :figclass: align-center

        Succeed

    Click the **Finish** button to test the connection between the Ubuntu Linux system and the industrial PC via internet. |br|
    Then click the **Build & Run** tab to select and apply a compiler, as shown on the figure below.

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_4.jpeg
        :align: center
        :figclass: align-center

        Compilers

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_5.jpeg
        :align: center
        :figclass: align-center

        Qt Version

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_6.jpeg
        :align: center
        :figclass: align-center

        Change the name

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_7.jpeg
        :align: center
        :figclass: align-center

        New kit settings

    Follow the `Steps`_ above to build a new project named ``Test`` and choose the new development kit.

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_8.jpeg
        :align: center
        :figclass: align-center

        Choose new kit

    Add the code below to the ``Test.pro`` file before you build & run.

    .. code-block:: text

        target.files = Test
        target.path = /home/root
        INSTALLS += target

    .. figure:: /Media/ARM/A8/Software/Linux/Dev_Kit_9.jpeg
        :align: center
        :figclass: align-center

        Test.pro file

    Now you should see a window on the industrial PC.

.. include:: /PCs/Shared/support