.. include:: /PCs/Shared/pdf_options_software

.. |systemType| replace:: Debian 11
.. |chip| replace:: RK3568
.. |ipc| replace:: Chipsee industrial PC

|systemType| OS
###############

.. rst-class:: fs-3 fw-bold text-center

  |systemType| OS on |chip| User Manual


.. image:: /Media/Chipsee_Logo_Full.png
   :align: center
   :width: 320
   :alt: chipsee-logo

This is the software manual for |chip| Chipsee industrial PC. If you've never developed on this hardware with a |systemType| OS, this manual can get you started quickly.

.. include:: Resources/Shared/overview

System Information
==================

.. rubric:: Out of Box System

.. table::
   :align: center
   :width: 100%
   :widths: auto

   +---------------------+----------------------------------------+
   |                     | Description                            |
   +=====================+========================================+
   | Kernel              | 5.10.110                               |
   +---------------------+----------------------------------------+
   | Bootloader          | U-Boot 2017.09                         |
   +---------------------+----------------------------------------+
   | OS                  | Debian GNU/Linux 11 (bullseye) aarch64 |
   +---------------------+----------------------------------------+
   | Python              | 3.9.2                                  |
   +---------------------+----------------------------------------+
   | Qt                  | 5.15.2, QMake 3.1                      |
   +---------------------+----------------------------------------+
   | GCC                 | 10.2.1                                 |
   +---------------------+----------------------------------------+
   | username/password   | [linaro/linaro]                        |
   +---------------------+----------------------------------------+
   | Window Manager      | Xfwm4                                  |
   +---------------------+----------------------------------------+
   | Desktop Environment | Xfce 4.16                              |
   +---------------------+----------------------------------------+

Prepare for Developing
======================

To get started, you first need to power on the |ipc|, then you may want to connect to this PC from your own laptop or computer to control it. Let's prepare some hardware and software to start developing.

Prepare the Hardware
--------------------

To power on and connect to |ipc|, we need:

#. A power adaptor. For products with a screen of 7 inch and below, a power adaptor with 6V ~ 36V DC output is required; for 10.1 inch and above products, you need one with 12V ~ 36V.
#. A USB to serial cable (if you need serial debug).
#. An Ethernet cable (if you want to SSH into the |ipc|). You may also use WiFi if your |ipc| supports WiFi, in this case you don't need the Ethernet cable.
#. A USB type-C cable (if you want to flash a new OS).

Prepare the Software
--------------------

Thanks to the |systemType| OS, developing on |ipc| isn't really different from developing on any other PCs, you can use any developer software you're comfortable with, with only one exception for flashing OS.

#. To flash a new operating system, you need RKDevtool, you can refer to the Flashing OS Image section.
   
   *The software listed below are not mandatory, they're recommendations because we find them easy to use:*

#. To SSH into a |ipc|, you may find **PuTTY** on Windows handy; for Linux and macOS users, a terminal app should come with your OS out of box, like **Terminal/iTerm2** on macOS and **xterm** on Linux.
#. To use a remote desktop, you can download **VNC Viewer** on your laptop or PC.


Connecting to the |ipc|
=======================

When a power supply is plugged, the |ipc| should boot itself automatically, next let's connect to it from our laptop or computer.

There are three different approaches: serial port debugging, SSH with Ethernet/WiFi and remote desktop with VNC.

Serial Port Debugging
---------------------

[*Cheatsheet for experienced developer*: username: **linaro**, password **linaro**.]

Physically, your laptop connects to your |ipc| with a USB to serial cable. To connect to the |ipc| in the terminal program, you first need to know what port your laptop or computer is using in the device tree.

The best way to find this is check what **tty** devices you have before connecting the |ipc| to your computer, then find out what is changed after you connect it to your laptop or PC.

Take macOS as an example:

.. code:: bash

   # on your laptop
   ls /dev/tty.*

You may see:

.. code:: bash

   # ➜  ~ ls /dev/tty.*
   # /dev/tty.Bluetooth-Incoming-Port /dev/tty.wlan-debug
   # ➜  ~ 

It means there is a Bluetooth and a wlan port **before** you plug the |ipc| to your Macbook.

Now you can plug the USB end to your laptop or computer, connect the serial port end to your |ipc|'s RS232 port. For different products the pins may vary, you can check the pin definition table to find out which pins are the RS232 TX, RX, GND for serial debugging.

And let's check again what has changed **after** we connect the two:

.. code:: bash

   # on your laptop, check again
   ls /dev/tty.*

You might see:

.. code:: bash

   # ➜  ~ ls /dev/tty.*
   # /dev/tty.Bluetooth-Incoming-Port /dev/tty.wlan-debug /dev/tty.usbmodem2812
   # ➜  ~ 

You can tell the last */dev/tty.usbmodem2812* appeared right after we plug in the cable, and this is the serial port that connects to your |ipc| with your USB to serial cable.

For Windows and Linux users the approach is almost the same, on Windows you may check the Microsoft Windows Device Manager. And check which COM port appears/disappears when you plug/unplug the USB to serial cable.

Now that we know the port on our OS, let's use the terminal program to connect to it.

Take macOS as an example:

.. code:: bash

   # on your laptop
   screen /dev/tty.usbmodem2812 115200

Use the **screen** command followed by the port name (in our case usbmodem2812), and a baud rate to connect to this serial port.

After a few seconds, in your terminal you should see some text, asking for a username and password. In our |chip| based system, we should input *linaro* for the username, and also *linaro* for the password.

For Windows users who use PuTTY, you should select Session, choose Serial in the radio buttons, and choose the COM port you found in the previous procedure, say COM3, and choose 115200 as baud rate, then click Open. When it asks for a username and password, give **linaro** for username and also **linaro** for password.

.. rst-class:: text-center

   .. image:: /Media/Shared/Software/Debug-Connection/serial-1.png
      :align: center
      :width: 640

   *Input your-com in the Serial Line field, in our case COM3*

That's it for connecting the |ipc| to your machine with a serial debug port.

SSH Connect
-----------

[*Cheatsheet for experienced developer*: username: **linaro**, password: **linaro**, IP check: **sudo ifconfig**.]

If you have a network connecting the |ipc| and your laptop or computer, you may find SSH comes handy.

To connect to your |ipc| with SSH, you need to plug an Ethernet cable to the RJ45 port, or connect through WiFi if your product supports WiFi.

You will need to know the IP address of your |ipc| to use SSH, to find out which, you can use a mouse and keyboard temporarily and type:

.. code:: bash

   # type this in your Chipsee PC's xterm program to find out the IP address of this device:
   $ sudo ifconfig

You should see a bunch of outputs, look for the keyword **eth** and **inet**, they will turn out to be your IP address, for example:

.. code:: bash

   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.6.134  netmask 255.255.255.0  broadcast 192.168.6.255
        inet6 fe80::c3be:d086:e810:ee8e  prefixlen 64  scopeid 0x20<link>
        ......
   
   lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        ......

   p2p0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ......

In our example, the IP address is **192.168.6.134**.

Now that we have the IP of our |ipc|, we can detach the mouse and keyboard, and go back to our laptop or computer to proceed.

We can now open a terminal app, like PuTTY on Windows, or Terminal/xterm on macOS/Linux.

For Windows users using PuTTY, you can choose Session, input **username@your-ip** (in our case *linaro@192.168.6.134*, yours should be different) in the Host Name field. Port Number should remain 22, choose SSH as the connection type in the radio buttons, click "Open". When the prompt asks for the password, type **linaro** and hit enter.

.. rst-class:: text-center

   .. image:: /Media/Shared/Software/Debug-Connection/ssh-2.png
      :align: center
      :width: 640

   *Input username@your-ip in the Host Name field, in our case linaro@192.168.6.134*

For macOS/Linux, in your terminal program, type:

.. code:: bash
   
   # change 192.168.6.134 to your Chipsee PC's IP we got earlier
   ssh linaro@your-ip
   # in our case, we are
   ssh linaro@192.168.6.134

.. rst-class:: text-center

   .. image:: /Media/Shared/Software/Debug-Connection/ssh-1.png
      :align: center
      :width: 640

   *Change the command to ssh username@your-ip, in our case ssh linaro@192.168.6.134*


When the prompt asks for your password, input **linaro**, the password will not show up on the screen when you type it, it's OK, just hit enter when you finish typing.

For both Windows and Linux/macOS users, we should have successfully ssh'd into our |ipc| now.

Connect with VNC Remote Desktop
-------------------------------

[*Cheatsheet for experienced developer*: username: **linaro**, password: **linaro**, IP check: **sudo ifconfig**, VNC port: **5900** (default port).] 

We can have a graphical user interface if we use VNC to connect to our |ipc|. This is handy if you're developing an HMI and want to test from your own laptop or computer. Here is how:

First please refer to the previous section to learn how to find out your |ipc|'s IP address. In our case we get **192.168.6.134**.

Then, for either Windows, macOS or Linux users, please open the VNC Viewer software on your laptop or PC. In the input area, which has a placeholder "Enter a VNC server address or search", you should input the IP address we obtained earlier: **your-ip**, in our case: **192.168.6.134** (yours should be different), and hit enter.

.. rst-class:: text-center

   .. image:: /Media/Shared/Software/Debug-Connection/vnc-1.png
      :align: center
      :width: 640

   *Change the input to your-ip, in our case 192.168.6.134*


VNC Viewer might ask for your credentials, you should input our username and password, in our case: username: **linaro**, password: **linaro**. And then continue, VNC Viewer might tell you the connection is not encrypted, it's OK if you're in your local network.

Now we should see our |ipc|'s desktop GUI in the VNC Viewer software.


Hardware Resources in the OS
============================

Now that you have successfully booted the |ipc| and connected the |ipc| to your laptop/computer, this section will tell you how to control this |ipc| from its OS desktop itself, or from your PC.

Network
-------

From the |ipc|'s desktop GUI, you can click the Network icon in the menu bar to set your network.

.. rst-class:: text-center

   .. image:: /Media/ARM/A55/Software/Network-1.png
      :align: center
      :width: 640

   *Network Settings*

From the terminal, you can use **nmcli** to configure the network. You can refer to the documents of the **nmcli** program for more information. **nmcli** is not a Chipsee specific tool, it's widely used in Linux distributions.

.. code:: bash

   $ nmcli -o

   eth0: connected to Wired connection 1
        "eth0"
        ethernet (rk_gmac-dwmac), 42:0B:6F:67:B0:E3, hw, mtu 1500
        ip4 default
        inet4 192.168.6.134/24

   p2p0: disconnected
           "p2p0"
           wifi (rtl8821cs), B6:6D:C2:13:A3:AE, hw, mtu 1500

   wlan0: disconnected
           "wlan0"
           wifi (rtl8821cs), B4:6D:C2:13:A3:AE, hw, mtu 1500

Serial Port RS232 and RS485
---------------------------

.. include:: Resources/Shared/serial_port_table

You can install **cutecom** to test the serial port:

.. code:: bash

   $ sudo apt-get install cutecom

Only root user and use the serial port:

.. code:: bash

   $ sudo cutecom

You can then use two |ipc|\s to test each other.

If you've got only one |ipc|, you can test that with your computer: you can use a USB to serial cable, connect the USB end to your computer, and connect the serial end to any of the |ipc|'s serial port. You may also wish to install a UART/COM Assistant software which has a GUI for testing. 

If you're an experienced engineer, you can also use a programming language to test the serial ports, like C, C++, Python, Javascript. They have their libraries for controlling serial port devices.

GPIO
----

.. include:: Resources/Shared/gpio_table

BUZZER
------

.. include:: Resources/Shared/buzzer


Backlight
---------

We use one PWM to control the backlight of |chip| boards, You can use the following commands:

* Get the supported max brightness:
    .. code:: bash

        $ cat /sys/class/backlight/backlight/max_brightness

* Get the current brightness:
    .. code:: bash

        $ cat /sys/class/backlight/backlight/actual_brightness

* Set brightness:
    .. code:: bash

        # might require write permission to the brightness file if you're not root
        $ sudo chmod a+w /sys/class/backlight/backlight/brightness
        # then set the new brightness
        $ echo 50 > /sys/class/backlight/backlight/brightness

CAN Bus
-------

There are two CAN bus channels on the |chip| based |ipc|. You can install `can-utils` and use them to test CAN. But you must add one 120Ω resistor between CAN_H and CAN_L on one of the two Boards, as shown on the figure below.

.. note::

   The Chipsee IPC does not mount the 120Ω matched resistor on all CAN signals by default.

.. figure:: /Media/Pi/Software/CAN.jpeg
   :align: center
   :figclass: align-center

   Connecting CAN

Here are a few examples to test CAN by using CAN units.

* Install `can-utils` if you haven't.
    .. code:: bash

        $ sudo apt install can-utils

* Set the bit-rate to **50Kbits/sec** with triple sampling using the following command (use ROOT user):
    .. code:: bash

         $ sudo ip link set can0 down
         $ sudo ip link set can0 type can bitrate 50000 triple-sampling on

* Bring up the device using the command:
    .. code:: bash

        $ sudo ip link set can0 up

* Transfer packets
    .. code:: bash

        $ sudo cansend can0 5A1#11.2233.44556677.88

* Receive data from CAN bus
    .. code:: bash

        $ sudo candump can0

* Bring down the device
    .. code:: bash

        $ sudo ip link set can0 down


Flashing OS Image
=================

.. include:: Resources/Download_Required_Tools_And_Image

.. include:: Resources/Flash_OS

.. include:: Resources/Flash_OS_Video

.. include:: /PCs/Shared/support