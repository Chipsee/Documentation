.. include:: /PCs/Shared/pdf_options_software

.. |systemType| replace:: Android 11
.. |chip| replace:: RK3568
.. |ipc| replace:: Chipsee industrial PC
.. |ipcs| replace:: Chipsee industrial PCs

|systemType| OS
###############

.. rst-class:: fs-3 fw-bold text-center

  |systemType| OS on |chip| User Manual


.. image:: /Media/Chipsee_Logo_Full.png
   :align: center
   :width: 320
   :alt: chipsee-logo

This is the software manual for RK3568 Chipsee industrial PC. If you’ve never developed on this hardware with an Android 11 OS, this manual can get you started quickly.

.. include:: Resources/Shared/overview

.. include:: Resources/Android/Connect

.. include:: Resources/Android/Install_APK


Hardware Resources in the OS
============================

Now that you have successfully booted the |ipc| and connected the |ipc| to your laptop/computer, this section will tell you how to control this |ipc| from its OS desktop itself, or from your PC.

Network
-------

You can use the native Android network API or the settings menu to change network configuration.

Serial Port RS232 and RS485
---------------------------

.. include:: Resources/Shared/serial_port_table

We know of 3 methods to interact with RS232 and RS485 in Android OS, sadly Android API does not support native ttyS* RS232 and RS485 devices, so people usually use JNI to add some C code to interact with serial ports, we'll show you what we know, because we are not experts in Android developments, we hope these methods can give software engineer experts like you some inspiration.

The **first method** is an Android app Google built in 2009, they open sourced their code at: https://code.google.com/archive/p/android-serialport-api/. This app is also installed on the |ipc| out of the factory, the app's name is "SerialPortTest". You can learn from the source code if you're building your own serial port app. There are also forks of this app on Github, some improves the app by adding more features like supporting a parity bit or flow control. You can search *android serial api* to find out more on the Internet.

.. image:: /Media/ARM/A55/Software/Android/Serial_App-3.jpg
   :align: center
   :width: 1024
   :alt: google-serial-test-app

When you first get your |ipc|, and looking to develop a program that involves serial ports, it's recommended to first test against the app Google built. For example, you have two |ipcs|, you should wire the RS232/RS485 port of two devices, and launch this app on both devices. You then set the baud rate, send messages from one device to another, and see if you can get the correct message on the other device. In this way, you can confirm you're wiring the hardware pins correctly. 

Then, if you have developed your app, you can install it on one of the devices, and still use this app on the other device to test your app. In this way, you make sure at least one device is working correctly, and if things go wrong, you can be confident it should be your code's problem, and then you gradually debug to fix the program.

If you have one device, you can use the approach above to test it with your workstation, there are serial debug tools available on Windows, Mac or Linux. Use a USB to serial RS232/RS485 cable to connect them, beware the serial cable is **NOT** a USB-to-TTL converter, the TTL voltage is not the same as RS232/RS485.

.. image:: /Media/ARM/A55/Software/Android/Serial_App-1.png
   :align: center
   :width: 1024
   :alt: google-serial-test-app-setup

.. image:: /Media/ARM/A55/Software/Android/Serial_App-2.jpg
   :align: center
   :width: 1024
   :alt: Serial Test App Communicate with Workstation

The image above shows we can use Google's app to test serial port. On the left is our workstation running a COMTool, on the right is the Android app, they are connected with a RS232 to USB cable.

The **second method** is using adb, **cat** and **echo** programs. You can wire the device's serial port to another device or your workstation, if you use two devices to communicate with each other, open two adb shells on your terminal app, each window should belong to one of the devices. In the example below, I will let the device talk to my Mac Mini, and use another tool on Mac called COMTool, it's a serial debugger you can download from Github.

.. image:: /Media/ARM/A55/Software/Android/Serial_Cat_Echo-1.png
   :align: center
   :width: 1024
   :alt: Two ADB Shell Windows

At the beginning you may wish to set the baud rate of the |ipc|'s serial devices, you can use **stty**, the command below will set ttyS0 (our RS232_0) to 115200 baud rate.

.. code:: bash

  stty -F /dev/ttyS0 115200

In the first window, you use **cat** program to listen for RS232/RS485 message:

.. code:: bash

    cat /dev/ttyS0

.. note:: 
  
  If you've been running some programs before, like a *pyserial* Python script (yes it's possible on Android!), the cat program might exit immediately. You can use a *stty* command to set most settings back to defaults (canonical), for more information, here is a doc for *stty*: https://man7.org/linux/man-pages/man1/stty.1.html.

  .. code:: bash

    stty -F /dev/ttyS0 icanon 

  And then use *cat /dev/ttyS0* again.

You should see this cat program seems blocking, and it's waiting for messages. Then we use our workstation to send a command through the serial port wire:

.. image:: /Media/ARM/A55/Software/Android/Serial_Cat_Echo-2.jpg
   :align: center
   :width: 1024
   :alt: Workstation Sends Message to Chipsee PC Through RS232

The image above shows the Mac's COMTool sent multiple "Hello from Chipsee!" to the |ipc| using RS232.

To send message from |ipc| and receive them in our workstation, we can use **echo**:

.. code:: bash
  
  echo -n -e "Greetings from Chipsee!\r" > /dev/ttyS0

.. image:: /Media/ARM/A55/Software/Android/Serial_Cat_Echo-3.jpg
   :align: center
   :width: 1024
   :alt: Chipsee PC Sends Message to Workstation Through RS232

This is one way to send and receive message from ADB, the ttyS* are our serial port RS232/RS485 devices represented by Linux files in Android OS. Hopefully, an Android developer could find this useful for building his Android native apps.

The **third** method is a workaround, even if it does not compile to an Android APK, it gives a similar user experience. It uses an Android app called **Termux**, which is an emulator that turns your Android to a Linux environment. With Termux, you can use the programming tools and languages you're familiar with, like Python, JavaScript. In this Termux Linux environment, you still have access to the Android's Chipsee hardware, like the RS232 and RS485 devices, through ttyS* files nodes. Then you can start a program to listen for incoming requests, such as a web server, then open a web page to send requests to this server. There are other solutions as well.

You can read the Termux's official doc to learn how to install your preferred Linux tools, for example, we installed Python 3.11 (in July, 2023):

.. image:: /Media/ARM/A55/Software/Android/Serial_Termux-1.png
   :align: center
   :width: 1024
   :alt: Use Termux to Install Python in Android OS on Chipsee PC

In the image above, it shows we can login to the Android |ipc| through ssh, and we have Python3 installed, we are also able to find our ttyS* devices (our RS232 RS485 devices).

We built a demo Python Flask web app targeting Debian OS, but it can also run on the Termux environment in Android OS, and the RS232, RS485 controlled by the *pyserial* library are fully functional as well. We can then open a browser or a webview Android app to visit the local IP address hosted by the Termux Linux environment on the Android to interact with RS232/RS485.

.. image:: /Media/ARM/A55/Software/Android/Serial_Termux-2.jpg
   :align: center
   :width: 1024
   :alt: Use Termux and Flask Web Server on Android to Control RS485

The image above shows we can communicate through RS485 between our workstation and |ipc|. On the left is my workstation Mac, on the right is a screen of our |ipc|. The Flask Python web server running in the Termux picks up the messages from ttyS3 (our RS485_3) using *pyserial* library, and then the Python server sends a command through websocket to the webview (think about a webview as a less powerful web browser Android app), then JavaScript in the webview picks up the message and displays them in the Android's screen as a HTML file.

To use the third method in your development, you can find out how Termux can auto boot your server program with *Termux:Boot*; and build a simple Android native APK that integrates a webview to visit your server's web port as soon as the APK is started;  then start your app automatically on system boot. In this way, when your |ipc| boots, your program is ready to use without having to type commands in Termux.

The source code of this demo app is in Chipsee's Github: https://github.com/Chipsee/chipsee-industrial-pc-web. If you're looking to use the approach above, or to develop your program on Debian Linux, you can refer to the repo, it's a Python program with HTML web pages. Except for serial ports, it has code to control buzzer, gpio, backlight, CAN and implemented a Modbus server/client as well.

Those are the three methods we know of that can control the RS232/RS485 devices on Android.

GPIO
----

.. include:: Resources/Shared/gpio_table

GPIO devices are already exported as 8 Linux files in the Android OS, they are */dev/chipsee-gpio1 ~ /dev/chipsee-gpio8*.

To use GPIO in your program, there are also two methods:

The **first** method is to read the file or write 0/1 to the file to control GPIO in **adb**. Similarly, you can also build Android APK and use Kotlin or Java to read/write those files to control GPIO.

The **second** method is the workaround we addressed in the serial port RS232/RS485 section. We can use Termux to take advantage of a Linux environment and are still able to use the /dev/chipsee-gpio1~8 device nodes.

Here is an demo we made in Python and webview running in Android:

.. image:: /Media/ARM/A55/Software/Android/GPIO_Termux-1.jpg
   :align: center
   :width: 1024
   :alt: Python Webserver Polling GPIO

The image above shows 8 GPIO ports in a webview (similar to a web browser, but in a limited Android app), the 4 round icons above are 4 GPIO output pins, among them the OUT_2 is set to high voltage by tapping the screen. We can confirm this in the left top window, when we *cat* the /dev/chipsee-gpio2, it returns a "1", indicating a high voltage. 

The 4 round icons in the bottom are 4 GPIO input pins, because we are not applying voltages to them, they all appear as red cross, meaning they are "0". If we apply a logic high to any pin, it would turn green.

This GPIO demo is a Python program, like it is discussed in the serial port section, it's running in the Linux environment on Android OS using Termux. The program starts a Flask web server, listens for requests from the webview. In the webview part, JavaScript polls the Python web server to know if the content in the HTML should be changed, then Python reads/writes contents of 8 /dev/chipsee-gpio* files to know the status of the input pins or make a change to the output pins.

To **test** the GPIO, there is a GPIODemo app made by Chipsee pre installed in your Android OS:

.. image:: /Media/ARM/A55/Software/Android/GPIO_Test-1.jpg
   :align: center
   :width: 1024
   :alt: GPIO Test App

Inside the app, you can test GPIO outputs and inputs, as well as Buzzer.

.. image:: /Media/ARM/A55/Software/Android/GPIO_Test-2.jpg
   :align: center
   :width: 1024
   :alt: GPIO Test App

BUZZER
------

Inside ADB, you can **echo** 0 or 1 to control the buzzer.

.. include:: Resources/Shared/buzzer

As shown in the GPIO section, you can **test** buzzer in the GPIODemo app.

.. image:: /Media/ARM/A55/Software/Android/Buzzer_Test-1.jpg
   :align: center
   :width: 1024
   :alt: Buzzer Control in Python and Webview

The red square has a buzzer switch, when you toggle the switch, the internal buzzer will be enabled.

You can also use Termux and Linux plus your favourite programming language to control buzzer:

.. image:: /Media/ARM/A55/Software/Android/Buzzer_Termux-1.jpg
   :align: center
   :width: 1024
   :alt: Buzzer Control in Python and Webview
   
The image above is a Python plus webview demo for controlling buzzer. Same Termux Linux environment as GPIO and Serial Port sections.

Backlight
---------

Android OS has native backlight API.

Multitouch Test
---------------

You can test the touch screen with the preinstalled TouchTester app:

.. image:: /Media/ARM/A55/Software/Android/Multitouch-1.jpg
   :align: center
   :width: 1024
   :alt: Multitouch Tester App

For different |ipc| models, some supports 5-point multitouch, some supports 10-point multitouch.

.. image:: /Media/ARM/A55/Software/Android/Multitouch-2.jpg
   :align: center
   :width: 1024
   :alt: 10 Points Multi Touch

The image above shows a 10.1 inch |ipc| supporting 10 point multitouch.


Flashing OS Image
=================

.. include:: Resources/Download_Required_Tools_And_Image

.. include:: Resources/Flash_OS

.. include:: Resources/Flash_OS_Video

.. include:: /PCs/Shared/support