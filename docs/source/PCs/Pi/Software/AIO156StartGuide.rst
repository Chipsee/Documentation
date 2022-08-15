AIO-CM4-156 Start Guide
#######################

.. centered:: Setting up your AIO-CM4-156

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual provides users with a fast guide of Chipsee Raspberry Pi Computer (Abbreviated as RPC) after reflashed Raspberry Official latest rleased OS. Through this manual, users can quickly setting up their AIO-CM4-156 to run Raspberry Official latest released OS.

.. table::
   :align: center
   :width: 100%

   +----------+-----------+--------+-----------------+
   | Revision |    Date   | Author |   Description   |
   +==========+===========+========+=================+
   |   V1.0   | 2022-01-20| Chipsee| Revision        |
   +----------+-----------+--------+-----------------+

What you will need
------------------

* SD Card

  - We recommend a minimum of 16GB micro SD card, and using `Raspberry Pi Imager`_ to install an `operating system`_ onto it.


* Power supply

  - We recommend 12V 2A.

.. Warning::
   This device only support 12V Power Supply.

Installing the Operating System
-------------------------------
You can reference `Installing operating system images`_ to know how to install the Operating System on your SD card.

Start up your AIO-CM4-156
-------------------------

1. Insert the SD card to SD Slot of AIO-CM4-156.

2. Power On.

Install CMhelper
----------------

1. Add follow lines in your **/boot/config.txt** file::

    disable_overscan=1
    dtparam=i2c_vc=0n
    dtoverlay=i2c-rtc,ds1307,i2c_csi_dsi,addr=0x32

2. Add cmhelper PPA to your system manually by copying the lines below,
   and adding them to your system's software sources **/etc/apt/sources.list.d/cmhelper.list**::

    deb http://ppa.launchpad.net/chipsee/cmhelper/ubuntu bionic main 
    deb-src http://ppa.launchpad.net/chipsee/cmhelper/ubuntu bionic main 

3. Update list of available packages::

    $ sudo apt update

   You will get error "the public key is not available: NO_PUBKEY 06D92B49B9078A87", you should
   use follow commands to receive key from ubuntu key server::

   $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 06D92B49B9078A87

   If the above commands is not useable and get warning "apt-key is deprecated. Manage keyring files in trusted.gpg.d instead"
   run follow commands instead::

   $ sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/cmhelper.gpg --keyserver keyserver.ubuntu.com --recv 06D92B49B9078A87
   $ sudo chmod 644 /etc/apt/trusted.gpg.d/cmhelper.gpg
   
   or use follow commands if above commands don't work::

   $ sudo gpg --keyserver keyserver.ubuntu.com --recv 06D92B49B9078A87
   $ sudo gpg --export --armor 06D92B49B9078A87 | sudo apt-key add -


.. Warning::
   The key 06D92B49B9078A87 may be diffrent with your error message, you should check your error,
   and use the right key.
 

4. Install cmhelper::

   $ sudo apt update
   $ sudo apt install cmhelper
   $ sudo reboot

.. Warning::
   Don't forget to reboot to make cmhelper be installed completely.

How to use CMHelper
-------------------

.. figure:: /Media/Pi/Software/AIO156helper.jpg
   :align: center
   :figclass: align-center

The CMHelper can help customer to use keys and onboard buzzer, led, you can use it
to control volume, brightness, power, act led, buzzer.

1. Buzzer can be enabled and disabled, if you enable buzzer function, you can open and close
   buzzer, otherwise, you can't control the buzzer.

2. The act led is disabled default, if you enable it, you can use it like ACT LED on Raspberry Pi.

3. The product have two boot mode, default is manual boot, you should press power key to boot system.
   If you want boot system directly after power, you can select auto boot.

4. You can use CMHelper QT application to control backlight, you also can use key to control that.

5. This QT Application is open source, you can recompile it by use follow commands::

    $ sudo apt update
    $ sudo apt install qt5-default
    $ git clone https://gitee.com/chipsee/cmhelper_tester.git
    $ cd cmhelper_tester
    $ qmake cmhelper_tester.pro
    $ make

6. There is also one C file for you to use::

    $ cd cmhelper_tester/c
    $ gcc -o cmhelper_test -lcmhelper cmhelper_test.c
    


.. links
.. _Raspberry Pi Imager: https://www.raspberrypi.org/software/
.. _operating system: https://www.raspberrypi.org/software/operating-systems/
.. _Installing operating system images: https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system
