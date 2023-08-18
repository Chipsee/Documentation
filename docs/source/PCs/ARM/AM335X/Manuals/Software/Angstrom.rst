.. include:: /PCs/Shared/pdf_options_software

.. |systemType| replace:: Angstrom
.. |chip| replace:: AM335X


.. |filename| replace:: prebuilt-angstrom-XXXXXX.tar.gz
.. |folder_name| replace:: ~/prebuilt-angstrom-XXXXXX
.. |bash_script| replace:: ./mksdcard.sh
.. |user| replace:: root
.. |pswd| replace:: empty


|systemType| OS
###############

.. centered:: Chipsee |systemType| OS User Manual

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual provides users with a fast guide of Chipsee Industrial Computer (Abbreviated as IPC) about |systemType| OS development. Through this manual, users can quickly understand the hardware resources; users can debug |systemType| OS via serial and Internet.

.. table::
   :align: center
   :width: 100%

   +----------+-----------+--------+-----------------+
   | Revision |    Date   | Author |   Description   |
   +==========+===========+========+=================+
   |   V1.0   | 2021-12-09|  Randy | Initial Version |
   +----------+-----------+--------+-----------------+

**SUPPORTED BOARDS:**

   *CS80480T050*    *CS10600T070*   *CS10768T097*

.. _db_pkg_angstrom:

**PREBUILT FILES PACKAGE:**

Prebuilt files for the various industrial PCs can be found in the :ref:`OS Downloads <AM335X_OSDownloads>`. |br|
Below are the links to the prebuilt files for each industrial PC model.

+ :ref:`CS80480T050 <CS80480T050-angstrom>`
+ :ref:`CS10600T070 <CS10600T070-angstrom>`
+ :ref:`CS10768T097 <CS10768T097-angstrom>`



.. rubric:: System Features

.. table::
   :align: center
   :width: 100%

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | System        | Angstrom 2012                    |
   +---------------+----------------------------------+

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Files Package to re-flash the system.

* Power Supply Unit (PSU) with the appropriate voltages, as follows:

   + Products with 5" display panel require 6V to 36V PSU
   + Products with 7" to 10.1" display panel and larger require 6V to 42V PSU

* USB to serial cable for debugging Chipsee Industrial Embedded Computers (Chipsee IPC)
* TF Card to create a bootable storage for re-flashing the system. Use the prebuilt files :ref:`link above <db_pkg_angstrom>` to re-flash the system.

.. include:: Resources/Hardware_Req

Software Requirements
---------------------

* |systemType| OS Prebuilt Files Package (from the link above)

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

.. figure:: /Media/ARM/A8/Software/Angstrom/Startup_Screen.jpeg
   :align: center
   :figclass: align-center

   Angstrom OS start-up screen

Tests
-----

Touch screen and buzzer test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the screen, the mouse arrow stays in a position that triggers the buzzer sounds, indicating that touch and buzzer work properly. |br|
After working for some time, the resistive touch screen may not be accurate. The user must run a touch screen calibration test. |br|
Firstly delete the file ``/etc/pointercal.xinput`` using the command below.

.. code-block:: bash

    $ sudo rm /etc/pointercal.xinput

Click on the System-->Administration-->Calibrate Touchscreen app on desktop to recalibrate. |br|
Reboot the system. You will see the calibrate app upon boot up before you access the system.
Just calibrate, the result will be saved.


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

Audio IO test
^^^^^^^^^^^^^^^^^^^^

Start the terminal, then use the ``mplayer`` command to play an audio file.

.. code-block:: bash

    # mplayer FILENAME  //such as: mplayer ~/Music/test.mp3

Serial test
^^^^^^^^^^^

There are four serial ports on the Chipsee IPC: 2 X RS232 and 2 X RS485. The COM1(RS232) is used as the debug serial port. Users can communicate with the OS via COM1.
Refer to the table below for the available serial device nodes.

.. include:: Resources/serial_table

1) Run a serial test:
    + Install **SecureCRT** or **Putty** software on a Windows 7 PC and use it to perform the serial port testing.
    + Connect keyboard and mouse to the IPC. Then press **Ctrl+Alt+F1 (or F3~F6)** to get into **tty1(tty3~tty6)**. Enter username: :substitution-code:``|user|``, no password.

    .. note::

        Notes: The system is not QtE by default, follow the steps in the CD(Angstrom/Documents/Qt-Angstrom) to set the environment. The QtE in Angstrom OS is not working well, by now user only can use mouse for the Qt apps.

    + Launch the **ChipseeTest** app by using the commands below.

    .. code-block:: bash

        # cd chipsee
        # ./ChipseeTest -qws

    .. figure:: /Media/ARM/A8/Software/Linux/ChipseeTest_Screen.jpeg
           :align: center
           :figclass: align-center

           ChipseeTest

2) If you want to use COM1 as a normal serial port, you can re-configure the port by following these steps:
    * Open and edit the ``uEnv.txt`` file which can be found in the boot partition with any text editor.

    .. code-block:: bash

        bootargs=console=ttyO0,115200n8 root=/dev/mmcblk0p2

    * At the end of the file, edit this line ``bootargs=console=ttyO0,115200n8 root=/dev/mmcblk0p2`` to

    .. code-block:: bash

        bootargs=root=/dev/mmcblk0p2

    * This will change ttyO0 (COM1) to ttyO1, ttyO2 or ttyO4(RS232_2, RS485_1 and RS485_2) and makes it possible to use all the four serial ports as normal serial ports.
    * Stop the service in Angstrom.

    .. code-block:: bash

        # systemctl disable serial-getty@ttyO0.service
        # systemctl stop serial-getty@ttyO0.service

    Now you can use the COM1 as normal serial port.

1) If you want to use COM1 as debug serial port, you have to edit the ``uEnv.txt`` file which you can find in the boot partition. And start the service by running this command:
    .. code-block:: bash

        # systemctl start serial-getty@ttyO0.service

2) From the **ChipseeTest** app, search for the serial area then configure the following settings, as shown on the figure below.
    - set Com to COM2
    - set Baud to 115200
    - click on the **Open** button
    - It will send the string *Succeed in sending message!!!* every two seconds through the serial port to the Windows 7 PC.
    - Click on the **SendMSG** button to send the string *Succeed in sending message-manual!!!*.
    - Every two seconds, it will read the received buffer and show the result to the received area.

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

USB device test
^^^^^^^^^^^^^^^

* USB-WiFi
    1) The |systemType| OS supports USB-WiFi module. If you want to use the USB-Wifi module in the system, you need to edit the ``/var/lib/connman/wifi.config`` file.
    2) Modify the router, the login name, and password in the config file, as shown in the code-block below.

    .. code-block:: bash
            :linenos:
            :emphasize-lines: 2-4

            Type = wifi
            Name = chipsee  //router’s name
            Security = AES  //security mode
            Passphrase = 1234567890 //password

    3) Save and reboot. The system will automatically connect to the WiFi the next time you start.

* USB-Webcam
    1) The |systemType| OS supports USB-Camera. If you want to use the USB webcam, you need to connect the webcam to the IPC before power ON.
    2) Then choose Application-->Sound&Video-->Cheese Webcam Booth to take pictures.

.. include:: Resources/Logo_Modify


|systemType| OS debug
=====================

In this section, we will discover how to view the |systemType| system via the serial port on a Windows 7 PC. |br|
Also, we will discover how to debug using NFS on a Ubuntu Linux PC. |br|

.. include:: Resources/SerialPort_Debug

.. include:: Resources/NFS_Debug

.. include:: /PCs/Shared/support