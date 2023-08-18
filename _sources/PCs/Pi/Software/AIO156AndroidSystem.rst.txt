.. include:: /PCs/Shared/pdf_options_software

.. |systemType| replace:: Android
.. |chip| replace:: AIO CM4

AIO-CM4-156 Android Start Guide
###############################

.. centered:: Setting up your AIO-CM4-156

.. image:: /Media/Chipsee_Logo_Full.png
   :align: center

This manual provides users with a fast guide of Chipsee Raspberry Pi Computer (Abbreviated as RPC) after reflashed a third party provided Android OS. Through this manual, users can quickly set up their AIO-CM4-156 to run a third party released Android OS.

.. table::
   :align: center
   :width: 100%

   +----------+-----------+--------+-----------------+
   | Revision |    Date   | Author |   Description   |
   +==========+===========+========+=================+
   |   V1.0   | 2023-04-18| Chipsee| Revision        |
   +----------+-----------+--------+-----------------+

What you will need
------------------

* SD Card

  - We recommend a minimum of 16GB micro SD card, and using `Raspberry Pi Imager`_ to install `operating system`_ onto it.


* Power supply

  - We recommend 12V 2A.

.. Warning::
   This device only supports 12V Power Supply.

Installing the Operating System
-------------------------------

You can reference `Installing operating system images on SD`_ to know how to install the Operating System on your SD card.

You can reference `Installing operating system images on eMMC`_ to know how to install the Operationg System on the eMMC.

The diffren between AIO-CM4-156 with CM4 IO board is that AIO-CM4-156 use Volume+ to enter usb boot mode.

Push Volume+ before power on and release it after 3 seconds, the system will boot from the USB port, then we can run rpiboot to enable eMMC work as one Storage on PC.


Start up your AIO-CM4-156
-------------------------

1. Insert the SD card to SD Slot of AIO-CM4-156, If you use eMMC, ignore the SD card operation.

2. Press power button to power On.

3. In Android system, setting Audio device to HDMI0 like follow,
	
	Setting->System->Raspberry Pi settings->Audio device->HDMI0

Known Issues/Limitations
------------------------

1. Storage only has 8GB in the Android system. The other space of eMMC or SD is not useabled.
2. We can't control the backlight in the Android system, but we can control it by using the hardware button.
3. Hardware power button doesn't support suspending the Android system and waking up the Android system, but supports long-press to shutdown the system, and short-press to power on the device.
4. Hardware Volume control button doesn't work.


.. links
.. _Raspberry Pi Imager: https://www.raspberrypi.org/software/
.. _operating system: https://chipsee-tmp.s3.amazonaws.com/mksdcardfiles/RaspberryPi/15.6/Android13/AOSP13-20230412-KonstaKANG-rpi4.zip
.. _Installing operating system images on SD: https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system
.. _Installing operating system images on eMMC: https://www.raspberrypi.com/documentation/computers/compute-module.html#flashing-the-compute-module-emmc


.. include:: /PCs/Shared/support