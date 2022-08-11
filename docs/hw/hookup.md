# iRobot® Create® 3 Hookup Guide

The iRobot® Create® 3 has a USB-C®[^1] connector implementing a USB 2.0 host capable of 5 V @ 3 A continuous, which can be used to power and communicate with various downstream devices.
Here are some hookup examples.

## NXP NavQ+
Since NavQ+ has USB-C® ports capable of being configured as a USB Ethernet Gadget, a cable with a USB-C® connector on both ends is all that is required.

!!! note
    - Unless set otherwise, the default USB-C® port for use as an ethernet gadget device is configured to only the centermost (USB 2) USB-C® as shown in the example pictures.

The NavQ+ is pictured in the cargo bay using the 3D printed adapter plate and ontop of the faceplate using the 3D printed case.
![Hookup diagram for NavQ+ with adapter mount in cargo bay](data/hookup_navqplus_adapter_mount_bay.jpg "NavQ+ in Cargo Bay")
![Hookup diagram for NavQ+ with case on faceplate](data/hookup_navqplus_case_faceplate.jpg "NavQ+ on Faceplate")

The NavQ+ has a printable case specifically designed for use with the Create® 3, allowing for it to be mounted to the faceplate or cargo bay.
The base of the case attaches to the NavQ+ using the existing four (4) M2.5-0.45 x 12mm System On Module (SOM) mounting screws.

!!! note
    - This case is designed to be fastened together with four (4) M3-0.5 x 10mm screws if not mounted to a Create® 3 plate or M3-0.5 x 12mm if mounted; cap head is suggested.
    - For best results, it is suggested to tap/thread the M3-0.5 (Create® 3 mounting/case fastening) and M2.5-0.45 (SOM) holes.

* [Case Top (413.5 kB)](data/cases/C3-NavQPlus-Top.stp)
* [Case Base (130.2 kB)](data/cases/C3-NavQPlus-Base.stp)

Setup showing faceplate mounted case and printable [sensor brackets](https://github.com/iRobotEducation/create3_docs/tree/main/docs/hw/data/brackets).
![Sensor faceplate hookup example.](data/navqplus_case_sensors.jpg "NavQ+ with sensors on Faceplate")


If a more minimal mount is desired instead of a case, an adapter plate using the existing SOM mounting screws for fastening is also provided.

!!! note
    - This adapter is designed to be fastened to the Create® 3 plate with four (4) M3-0.5 x 6mm screws; cap head is suggested.
    - For best results, it is suggested to tap/thread the M3-0.5 (Create® 3 mounting) and M2.5-0.45 (SOM) holes.

* [Adapter Plate (3.4 MB)](data/brackets/C3-RudisLabs-NavQPlus-Adapter.stp)


## Raspberry Pi®
The Raspberry Pi®[^2] mounting scheme does not match Create® 3's faceplate or cargo bay hole pattern; here are two 3D-printable mounts.
The larger mount is more rigid but requires three times as much time to print.

* [Small Mount (128kB)](data/brackets/C3-RPi-Mount-Small-20211022.stl)
* [Large Mount (520kB)](data/brackets/C3-RPi-Mount-20211022.stl)

### Raspberry Pi® 4
Since the Raspberry Pi®[^2] 4 has a USB-C® port capable of an OTG connection, a cable with a USB-C® connector on both ends is all that is required.
The Raspberry Pi® is pictured in the cargo bay with the large mount, and the Adapter Board is removed from the robot for clarity.
![Hookup diagram for Raspberry Pi® 4](data/hookup_pi4.jpg "Raspberry Pi® 4")

### Raspberry Pi® 1-3 Model B
The original Raspberry Pi® through the Raspberry Pi® 3 do not have upstream (device) ports, so it's a little more difficult to connect and power them cleanly.
We suggest using a USB-C® hub which includes an integrated USB to Ethernet adapter as the cleanest way to go.
![Hookup diagram for Raspberry Pi® 3B](data/hookup_pi3b.jpg "Raspberry Pi® 3B")
It's also possible to power the Raspberry Pi® using the USB-C® port on the Adapter Board with the help of a downstream connection adapter like [this one](https://www.adafruit.com/product/4090) and make the data connection over Wi-Fi.

### Raspberry Pi® Zero
This should be the same as the Raspberry Pi® 4.
The Micro-USB connector labeled "USB" is an OTG port capable of being an Ethernet Gadget; use a USB Micro B to USB-C® cable to connect it directly to the robot's Adapter Board.
![Hookup diagram for Raspberry Pi® Zero](data/hookup_piZ.jpg "Raspberry Pi® Zero")

## NVIDIA® Jetson Nano™ 2GB
The Jetson Nano™[^3] 2GB has a USB-C® port (J2) for power and a USB Micro-B port (J13) for downstream data.
This can be connected to the Create 3 most simply using a USB-C® hub and two cables -- USB A to Micro-B and USB A to USB-C®.
![Hookup diagram for Jetson Nano™](data/hookup_nano2gb.jpg "Jetson Nano™ 2GB")

## NVIDIA® Jetson Xavier NX™ Developer Kit
The [Jetson Xavier NX™ Developer Kit](https://developer.nvidia.com/embedded/jetson-xavier-nx-devkit) has a 5.5mm x 2.5mm barrel connector jack (J16) for power (9 V to 20 V) and a USB Micro-B port (J5) for downstream data.<br>
This can be powered from the unregulated battery port of the Create® 3  adapter board by using a JST-XH female connector to DC barrel plug cable.
The data connection is established by using a USB Micro B to USB-C® cable.
![Hookup diagram for Jetson Xavier NX™ Developer Kit](data/hookup_jetson_xavier_nx.jpg "Jetson Xavier NX™ Developer Kit")

### Mounting NVIDIA® Jetson Xavier NX™ Developer Kit
You can 3d print the [mount adapter](data/brackets/C3-JetsonXavierNX-Mount.3mf) to place the Jetson Xavier NX Developer Kit in the cargo bay or on the faceplate.

!!! note
    - If you are 3d printing the above mount adapter, use **support** to support overhang areas. ([slicing example](data/brackets/C3-JetsonXavierNX-Mount_slice-example.png))
    - You need four (4) M3 x 6mm screws; cap head is suggested.

[^1]: USB-C® is a trademark of USB Implementers Forum.
[^2]: Raspberry Pi® is a trademark of Raspberry Pi Trading.
[^3]: NVIDIA and Jetson Nano are trademarks or registered trademarks of NVIDIA Corporation.
[^4]: All other trademarks mentioned are the property of their respective owners.