.. include:: /PCs/Shared/pdf_options

.. |product| replace:: BBB-EXP7H

.. |PN| replace:: PN: BBB-EXP7H

.. _product_link: https://chipsee.com/product/epca870hbc/

.. _BBB-EXP7H:

.. |product_link| replace:: BBB-EXP7H

.. |Cover PNG| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-Front.png

.. |Front View| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-Front.jpg
                  :class: product-img

.. |Rear View| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-Rear.jpg
                  :class: product-img

.. |Side View 1| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-Side1.jpg
                  :class: product-img

.. |Side View 2| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-Side2.jpg
                  :class: product-img 

.. |sw_manual_download| replace:: :download:`Download Archived Software Manual: Chipsee_Beagle_Bone_Black_User_Manual_V1.0.2.pdf <PDF/Chipsee_Beagle_Bone_Black_User_Manual_V1.0.2.pdf>`

.. |display| replace:: 7 Inch LCD, 1024*600 Pixel, 250nit Brightness by default (400 nit optional)

.. |touch| replace:: Five Point Capacitive touch, Covered with Amorplate Glass (Or Reisistive Touch);

.. |audio| replace:: On board Speaker(1W), 1 Audio out, 1 Mic In Connector (Can change to Line in by changing resistor)

.. |rtc| replace:: Use Battery CR1220, Not Mounted by default.

.. |rs232| replace:: 2 Channels, COM0 and COM1 

.. |rs485| replace:: 2 Channels, COM2 and COM4

.. |can| replace:: 1 Channel, CAN0 

.. |buzzer| replace:: 1

.. |key| replace:: 5 User defined keys, 1 Reset Key, 1 Power Key

.. |led| replace:: 2 User defined LEDs

.. |sensors| replace:: Three-Axis Digital Accelerometer

.. |power| replace:: 5V, 3W power Consumption

.. |img1| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-1.jpg
                  :align: middle
                  :width: 640

.. |img2| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-2.jpg
                  :align: middle
                  :width: 640

.. |img3| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-3.jpg
                  :align: middle
                  :width: 640

.. |img4| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-4.jpg
                  :align: middle
                  :width: 640

.. |img5| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-5.jpg
                  :align: middle
                  :width: 640

.. |img6| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-6.jpg
                  :align: middle
                  :width: 640

.. |img7| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-7.jpg
                  :align: middle
                  :width: 640

.. |img8| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-8.jpg
                  :align: middle
                  :width: 640

.. |img9| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-9.jpg
                  :align: middle
                  :width: 640

.. |img10| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-10.jpg
                  :align: middle
                  :width: 640

.. |img11| image:: /Media/ARM/A8/BBB-EXP7H/BBB-EXP7H-11.jpg
                  :align: middle
                  :width: 640


|product|
#########

.. rubric:: *Version 2.0*
    :class: html-only

.. include:: /PCs/Shared/four_main_images

BeagleBone Black 7 Inch LCD Expansion board (Abbreviate as BBB-EXP7H) designed by Chipsee. It has two versions: Capacitive Touch Version and Resistive Touch Version. 

- |sw_manual_download|

:pagebreak:`True`

Hardware Features
=================


.. table:: Key Features
   :align: center
   :width: 100%
   :widths: auto

   +------------------------------------------------------------------------------+
   | .. centered:: |product|                                                      |
   +==============================================+===============================+
   | **Display**                                  | |display|                     |
   +----------------------------------------------+-------------------------------+
   | **Touch**                                    | |touch|                       |
   +----------------------------------------------+-------------------------------+
   | **Audio**                                    | |audio|                       |
   +----------------------------------------------+-------------------------------+
   | **RTC**                                      | |rtc|                         |
   +----------------------------------------------+-------------------------------+
   | **RS232**                                    | |rs232|                       |
   +----------------------------------------------+-------------------------------+
   | **RS485**                                    | |rs485|                       |
   +----------------------------------------------+-------------------------------+
   | **CAN**                                      | |can|                         |
   +----------------------------------------------+-------------------------------+
   | **Buzzer**                                   | |buzzer|                      |
   +----------------------------------------------+-------------------------------+
   | **KEY**                                      | |key|                         |
   +----------------------------------------------+-------------------------------+
   | **LED**                                      | |led|                         |
   +----------------------------------------------+-------------------------------+
   | **Sensor**                                   | |sensors|                     |
   +----------------------------------------------+-------------------------------+
   | **Power**                                    | |power|                       |
   +----------------------------------------------+-------------------------------+


.. rst-class:: text-center

    |img1|

    *Figure 1 BBB-EXP7H (Capacitive,Android 4.2)*

.. rst-class:: text-center

    |img2|

    *Figure 2 BBB-EXP7H Back-Side View (Capacitive)*

:pagebreak:`True`

How to connect BBB-EXP7H with BeagleBone Black
==============================================

When connect BBB-EXP7H with BeagleBone Black, Figure 3 shows the right connects direction. If connect on the wrong direction, the Beaglebone Black can’t be push down to connect tightly: The LAN connector on Beaglebone Black will conflict with the Audio connector on the BBB-EXP7H.

.. rst-class:: text-center

    |img3|

    *Figure 3*

:pagebreak:`True`

How to connect Power to the System
==================================

BeagleBone Black use 5V DC power Input, BBB-EXP7H use 5V DC power also.

When BBB-EXP7H connect with BeagleBone Black, the Power connector on BeagleBone black will be hide by the RS485 connector. User can provide 5V power to the power connector on the BBB-EXP7H connector **P4 ONLY** as Figure 4 shows. This 5V power will be connect to Beaglebone Black. **5V/2A** power adapter will be necessary.

.. rst-class:: text-center

    |img4|

    *Figure 4*

:pagebreak:`True`

How to change Boot Method
=========================

Beaglebone Black can be changed boot method by push the Button **S2**: Push button **S2** when system power on, BeagleBone Black will boot from uSD card, or it will boot from eMMC by default.

When connect with BBB-EXP7H, the Button **S2** on the Beaglebone black will be hide and not easy to touch. BBB-EXP7H connect this boot signal to switch **SW8** as Figure 5 shows. When user switch it to upside, the system will boot from uSD card, when user switch it to downside, the system will boot from eMMC.

.. rst-class:: text-center

    |img5|

    *Figure 5*

:pagebreak:`True`

Power and Reset Button
======================

BeagleBone Black use Button **S3** as Power button, BBB-EXP7H connect this signal to Button **SW6** as Figure 6 shows. So BBB-EXP7H button SW6 will have the same effect with S3 on the BeagleBone Black.

BeagleBone Black use Button **S1** as Reset button, BBB-EXP7H connect this signal to Button **SW7** as Figure 6 shows. So BBB-EXP7H button SW7 will have the same effect with S1 on the BeagleBone Black.

.. rst-class:: text-center

    |img6|

    *Figure 6*

:pagebreak:`True`

User Keys and user LED
======================

BBB-EXP7H have add 5 user keys as SW1 to SW5 as Figure 7 shows, User can define the key function in software, ChipSee have define it in Android as:

* HOME
* BACK
* MENU
* VOLUME UP
* VOLUME DOWN

BBB-EXP7H add two user LEDs as Figure 7 shows. User can define its function in software.

.. rst-class:: text-center

    |img7|

    *Figure 7*

:pagebreak:`True`

Audio Input and Output
======================

BBB-EXP7H has audio input and output as Figure 8 shows. The expansion board use standard 3.5mm connector. Blue Connector **P8** is output, Pink Connect **P9** is input.

User can connect the output to any other speaker. As for the Input, it’s “MIC in”, NOT “Line In”, that means user can connect Microphone to the connector directly.

.. rst-class:: text-center

    |img8|

    *Figure 8*

:pagebreak:`True`

About RTC
=========

BBB-EXP7H adds RTC support, and adds Lithium Battery CR1220 to keep the time as Figure 9 shows. That means the system time will not lost when power off. Be attention the Battery CR1220 is **NOT Mount** on by default because of International shipment Limitation. User should purchase this Lithium battery and mount on by themselves.

.. rst-class:: text-center

    |img9|

    *Figure 9*

:pagebreak:`True`

About the RS232 , RS485 and CAN on Expansion board
==================================================

BBB-EXP7H have add RS232 ,RS485, CAN function to the connector **P10**, **P12** and **P13** as Figure 2 shows.

.. table:: DB9 Connector P10 connects to the CPU UART0, It use RS232 Level
   :align: center
   :width: 100%
   :widths: auto

   +-------------------------------------------------------------------------------+
   | .. centered:: DB9 Connector P10 connects to the CPU UART0, It use RS232 Level |
   +================+==============================+===============================+
   |   Pin Number   | Definition                   | CPU Function                  |
   +----------------+------------------------------+-------------------------------+
   |   2            | TXD                          | UART0, CPU PIN D15 and D16    |
   +----------------+------------------------------+-------------------------------+
   |   3            | RXD                          |                               |
   +----------------+------------------------------+-------------------------------+
   |   5            | GND                          |                               |
   +----------------+------------------------------+-------------------------------+
   | 1,4,6,7,8,9    | Not Connected                |                               |
   +----------------+------------------------------+-------------------------------+

.. table:: Connector **P13** connects to the CPU UART0 also, But It use 3.3V TTL Level.
   :align: center
   :width: 100%
   :widths: auto

   +-------------------------------------------------------------------------------+
   | .. centered:: **P13** connects to the CPU UART0, But It use 3.3V TTL Level.   |
   +================+==============================+===============================+
   |   Pin Number   | Definition                   | CPU Function                  |
   +----------------+------------------------------+-------------------------------+
   |   1            | GND                          |                               |
   +----------------+------------------------------+-------------------------------+
   |   4            | RXD                          |                               |
   +----------------+------------------------------+-------------------------------+
   |   5            | TXD                          | UART0, CPU PIN D15 and D16    |
   +----------------+------------------------------+-------------------------------+
   |   2,3,6        | Not Connected                |                               |
   +----------------+------------------------------+-------------------------------+

:pagebreak:`True`

.. table:: Connector **P12** definition
   :align: center
   :width: 100%
   :widths: auto

   +-------------------------------------------------------------------------------+
   | .. centered:: **P12** Definition                                              |
   +================+==============================+===============================+
   |   Pin Number   | Definition                   | CPU Function                  |
   +----------------+------------------------------+-------------------------------+
   |   1            | GND                          |                               |
   +----------------+------------------------------+-------------------------------+
   |   2            | CAN0_L                       | DCAN0, CPU PIN D17 and D18    |
   +----------------+------------------------------+-------------------------------+
   |   3            | CAN0_H                       |                               |
   +----------------+------------------------------+-------------------------------+
   |   4            | RS485_2+                     | UART4, CPU PIN T17 and U17    |
   +----------------+------------------------------+-------------------------------+
   |   5            | RS485_2-                     |                               |
   +----------------+------------------------------+-------------------------------+
   |   6            | RS485_1+                     | UART2, CPU PIN A15 and B17    |
   +----------------+------------------------------+-------------------------------+
   |   7            | RS485_1-                     |                               |
   +----------------+------------------------------+-------------------------------+
   |   8            | RS232_0_TXD                  | UART0, CPU PIN D15 and D16    |
   +----------------+------------------------------+-------------------------------+
   |   9            | RS232_0_RXD                  |                               |
   +----------------+------------------------------+-------------------------------+
   |   10           | RS232_1_TXD                  | UART1, CPU PIN D15 and D16    |
   +----------------+------------------------------+-------------------------------+
   |   11           | RS232_1_RXD                  |                               |
   +----------------+------------------------------+-------------------------------+
   |   12           | +5V                          |                               |
   +----------------+------------------------------+-------------------------------+

Be Attention:

a) COM0 signal have been connect out from Beaglebone Black for customer to debug. This product connect COM0 to P13 directly, it use 3.3V TTL logic. And it product also change the COM0 signal to RS232 level at the same time, then connect the RS232 signal to P10 and P11. **Be Attention**, The COM0 RXD signal connect to RS232 Level circuit by default, and not connect to P13. That means if you monitor COM0 debug signal from P13, you can receive message from the system, but you can’t input any message to the system. If you want to use P13 to input signal to system, please remove **R60**, and solder the **R81** with 0 Ohm 0603 package resistor,As Figure 10 shows:


.. rst-class:: text-center

    |img10|

    *Figure 10*

b) The RS232_0 signals have been connect to the DB9 connector P10 and connector P12 Pin8 and Pin9 at the same time. They are totally the same. As for this function, you can use one connector one time.

:pagebreak:`True`

Mechanical Dimension
====================

.. rst-class:: text-center

    |img11|

    *Figure 11*    

:pagebreak:`True`

Product Video
=============

Android 4.1 http://youtu.be/FebYqMws0g4

WindowsCE 6.0 http://youtu.be/S2Ttujf6cWU

:pagebreak:`True`

.. include:: /PCs/Shared/support
