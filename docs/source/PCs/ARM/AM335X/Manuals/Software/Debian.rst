.. include:: /PCs/Shared/pdf_options_software

.. |systemType| replace:: Debian
.. |chip| replace:: AM335X

.. |filename| replace:: prebuilt-som-v3-csrrrrrtss-v3-debian-sd-yyyymmdd.tar.gz
.. |folder_name| replace:: ~/prebuilt-som-v3-csxxxxxtxx-v3-ezsdk-sd-yyyymmdd
.. |bash_script| replace:: ./mksdcard.sh
.. |user| replace:: debian or root
.. |pswd| replace:: chipsee or root


|systemType| OS
###############

.. centered:: |systemType| OS User Manual

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual provides users with a fast guide of Chipsee Industrial Computer (Abbreviated as IPC) about |systemType| OS development. Through this manual, users can quickly understand the hardware resources; users can debug |systemType| OS via serial and Internet.

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

.. _db_pkg_debian:

**PREBUILT FILES PACKAGE:**

Prebuilt files for the various industrial PCs can be found in the :ref:`OS Downloads <AM335X_OSDownloads>`. |br|
Below are the links to the prebuilt files for each industrial PC model.

+ :ref:`CS80480T050 <CS80480T050-debian>`
+ :ref:`CS80600T080 <CS80600T080-debian>`
+ :ref:`CS10600T070 <CS10600T070-debian>`
+ :ref:`CS80480T070 <CS80480T070-debian>`
+ :ref:`CS10768T097 <CS10768T097-debian>`



.. rubric:: System Features

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +---------------+----------------------------------+
   | Feature       | Comment                          |
   +===============+==================================+
   | System        | Debian 7.4 & Debian 8.4          |
   +---------------+----------------------------------+

Preparation
===========

You will need to prepare the following items before you can start using the Prebuilt Files Package to re-flash the system.

* Power Supply Unit (PSU) with the appropriate voltages, as follows:

   + Products with 5" display panel require 6V to 36V PSU
   + Products with 7" to 10.1" display panel and larger require 6V to 42V PSU

* USB to serial cable for debugging Chipsee Industrial Embedded Computers (Chipsee IPC)
* TF Card to create a bootable storage for re-flashing the system. Use the prebuilt files :ref:`link above <db_pkg_debian>` to re-flash the system.

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

#) Copy the prebuilt file ``prebuilt-som-v3-csrrrrrtss-v3-debian-emmc-yyyymmdd.tar.gz`` to somewhere(such as $HOME).
#) Extract the prebuilt file ``prebuilt-som-v3-csrrrrrtss-v3-debian-emmc-yyyymmdd.tar.gz``
    .. code:: bash

        $ tar -xzvf prebuilt-som-v3-csrrrrrtss-v3-debian-emmc-yyyymmdd.tar.gz

#) Go to the folder ``prebuilt-som-v3-csrrrrrtss-v3-debian-emmc-yyyymmdd/``
    .. code:: bash

        $ cd ~/prebuilt-som-v3-csrrrrrtss-v3-debian-emmc-yyyymmdd

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

.. figure:: /Media/ARM/A8/Software/Debian/Startup_Screen.jpeg
   :align: center
   :figclass: align-center

   Debian OS start-up screen

Tests
-----

Touch screen and buzzer test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the screen, the mouse arrow stays in a position that triggers the buzzer sounds, indicating that touch and buzzer work properly. |br|
After working for some time, the resistive touch screen may not be accurate. The user must run a touch screen calibration test. |br|
Firstly delete the file ``/etc/pointercal.xinput`` using the command below.

.. code-block:: bash

    $ sudo rm /etc/pointercal.xinput

Click on the Preferences-->Calibrate Touchscreen app to recalibrate. |br|
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

Audio test
^^^^^^^^^^^

Start the terminal, then use the ``mplayer`` command to play an audio file.

.. code-block:: bash

    # mplayer FILENAME  //such as: mplayer ~/Music/test.mp3

Serial test
^^^^^^^^^^^

There are four serial ports on the Chipsee IPC: 2 X RS232 and 2 X RS485. The COM1(RS232) is used as the debug serial port. Users can communicate with the OS via COM1.
Refer to the table below for the available serial device nodes.

.. include:: Resources/serial_table

If you want to use COM1 as a normal serial port, you can re-configure the port by following these steps:

* Open and edit the file ``/etc/inttab`` with any text editor.
* At the end of the file, edit this line ``T0:23:respawn:/sbin/getty –L ttyO0 115200 vt102`` to

.. code-block:: bash

    # T0:23:respawn:/sbin/getty –L ttyO0 115200 vt102

* The code-block above, comments off the last line making it possible to use all the four serial ports as normal serial ports.
* You can verify the changes by running a serial test.
* Run a serial test:
    + Install **SecureCRT** or **Putty** software on a Windows 7 PC and use it to perform the serial port testing.
    + Connect COM2 on the industrial PC to Windows 7 PC. Set BAUD as 9600.
    + Send an echo through the terminal as shown in the code block below.

    .. code:: bash

        echo "This is a test" > /dev/ttyO1

    + You will see the string on the **SecureCRT** or **Putty** software running on the Windows 7 PC.
    + Change ttyO1 to ttyO2/ttyO4 to test RS485.

GPIO test
^^^^^^^^^

There are (4) four input and (4) four output pins. LOW is 0V, HIGH is 5V. |br|
The GPIO input terminals connect to the GPIO output terminals, respectively. IN1-4 corresponds to OUT1-4. |br|
As a result, if you set the GPIO_OUT area, you will see the GPIO_IN region change as well. |br|
You can control the LED light on the industrial PC by setting the LED **ON** or **OFF**.

.. include:: Resources/gpio_table

You can read and write the GPIO by following the steps below. For this example, we are going to use **gpio49(OUT1)**.

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

Use this command to view the network information on the industrial PC.
    .. code-block:: bash

        # ifconfig –a

Date and Time
^^^^^^^^^^^^^

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

USB device
^^^^^^^^^^

The |systemType| OS supports USB-WiFi (RTL8723). If you want to get USB-Wifi module to work, you need to edit file: ``/etc/network/interfaces`` as shown in the code-block below.

.. code-block:: bash

    # Wifi Example
    allow-hotplug wlanX
    auto wlanX
    iface wlanX inet dhcp
    wpa-ssid "Chipsee"   # Router’ name
    wpa-psk "1234567890" # Passwd

    **wlanX** usual should be ``wlan0``, you can use the command ``ifconfig –a`` to make sure of that.

.. include:: Resources/Logo_Modify

|systemType| OS debug
=====================

In this section, we will discover how to view the |systemType| system via the serial port on a Windows 7 PC. |br|
Also, we will discover how to debug using NFS on a Ubuntu Linux PC. |br|

.. include:: Resources/SerialPort_Debug

.. include:: Resources/NFS_Debug

Debian App Development
=======================

In this section, we will set up the Java environment and show you how to a make simple Java application.

Preparation
-----------

Download and install a Java jdk.
    .. code-block:: bash

        # sudo apt-get install openjdk-6-jdk

Example — Develop a ``HelloWorld.java`` Program
-----------------------------------------------

#) Open and edit, with any text editor, a simple java ``HelloWorld.java`` program.
    .. code-block:: java
       :linenos:

       import java.awt.Color;
       import java.awt.Font;
       import java.awt.Toolkit;
       import javax.swing.JFrame;
       import javax.swing.JTextField;

       public class HelloWorld extends JFrame{
           public HelloWorld(){
                JTextField text = new JTextField("Hello, world!");
                text.setFont(new Font("Times New Roman",Font.BOLD,60));
                text.setForeground(Color.BLACK);
                this.getContentPane().add(text);
            }
           public static void main(String argv[]){
                HelloWorld win = new HelloWorld();
                Toolkit tk  = Toolkit.getDefaultToolkit();
                int winWidth = 512;
                int winHeight = 300;
                int Width  = tk.getScreenSize().width;
                int Height = tk.getScreenSize().height;
                win.setSize(winWidth, winHeight);
                win.setLocation((Width-winWidth)/2, (Height-winHeight)/2);
                win.setVisible(true);
                win.setDefaultCloseOperation(EXIT_ON_CLOSE);
            }
       }


#) Compile the source.
    .. code-block:: bash

        # javac HelloWorld.java

    **This will be very slow in Debian OS, we suggest do it in your PC, you need install jdk-1.6 first.**

#) Run the program.
    .. code-block:: bash

        # java HelloWorld

    You will see something similar as the figure below.

    .. figure:: /Media/ARM/A8/Software/Debian/Hello_World.jpeg
       :align: center
       :figclass: align-center

       Hello World Program

#) Adding the Java program to Quick Start.
       * Make a directory
           .. code-block:: bash

              # mkdir /usr/lib/java/

       * Copy ``HelloWorld.class`` to ``/usr/lib/java/`` directory
           .. code-block:: bash

              # cp HelloWorld.class /usr/lib/java/

       * Open and edit script ``/usr/bin/HelloWorld.sh`` with any text editor.
           .. code-block:: bash
              :linenos:

              #!/bin/bash
              cd /usr/lib/java/
              java HelloWorld

       * Change the permissions of the script.
           .. code-block:: bash

              # sudo chmod a+x HelloWorld.sh

       * Edit file ``/usr/share/applications/javatest.desktop``.
           .. code-block:: text

              [Desktop Entry]
              Name=HelloWorld
              Comment=Simple test for Java
              Exec=/usr/bin/HelloWorld.sh
              Icon=/usr/share/pixmaps/chipsee.png
              Terminal=false
              Type=Application
              Categories=GTK;Utility;GNOME;

       * This is the result:
            .. figure:: /Media/ARM/A8/Software/Debian/Hello_World_2.jpeg
               :align: center
               :figclass: align-center

               Hello World Program

#) Auto-Launch Java app
    Add script ``89javatest`` in directory ``/etc/X11/Xsession.d/``.

    .. code-block:: bash

      #!/bin/bash
      cd /usr/lib/java/
      java HelloWorld

    Now when you Reboot the system, the ``HelloWorld`` app will automatically launch.


.. include:: /PCs/Shared/support