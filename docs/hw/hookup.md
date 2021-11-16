# iRobot® Create® 3 Hookup Guide

The iRobot® Create® 3 has a USB C connector implementing a USB 2.0 host capable of 5 V @ 3 A continuous, which can be used to power and communicate with various downstream devices. Here are some hookup examples.

## Raspberry Pi
The Raspberry Pi mounting scheme does not match Create 3's faceplate or cargo bay hole pattern; here are two 3D-printable adapters. The larger mount is more rigid but requires three times as much time to print.

* [Small Mount (128kB)](data/C3-RPi-Mount-Small-20211022.stl)
* [Large Mount (520kB)](data/C3-RPi-Mount-20211022.stl)

### Raspberry Pi 4
Since the Raspberry Pi 4 has a USB C port capable of an OTG connection, a cable with a USB C connector on both ends is all that is required. The Pi is pictured in the cargo bay with the large mount, and the adapter board is removed from the robot for clarity.
![Hookup diagram for Raspberry Pi 4](data/hookup_pi4.jpg "Raspberry Pi 4")

### Raspberry Pi 1-3 Model B
The original Raspberry Pi through the Raspberry Pi 3 do not have upstream (device) ports, so it's a little more difficult to connect and power them cleanly. We suggest powering the Pi using the USB C port with the help of a downstream connection adapter like [this one](adafruit.com/product/4090). The data connection could be made over Wi-Fi. If you'd rather connect to the robot over a wired connection, it's possible to use a hub with a USB to Ethernet adapter (either integrated or separate).
![Hookup diagram for Raspberry Pi 3B](data/hookup_pi3b.jpg "Raspberry Pi 3B")

### Raspberry Pi Zero
Coming soon.

## NVIDIA Jetson Nano 2GB
The Jetson Nano 2GB has a USB C port (J2) for power and a USB micro B port (J13) for downstream data. This can be connected to the Create 3 most simply using a USB C hub and two cables -- USB A to Micro B and USB A to USB C.
![Hookup diagram for Jetson Nano](data/hookup_nano2gb.jpg "Nano 2GB")

All trademarks mentioned are the property of their respective owners.