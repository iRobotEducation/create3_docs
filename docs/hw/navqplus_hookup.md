# iRobot® Create® 3 Hookup Guide for NavQ+ by NXP

The iRobot® Create® 3 robot has a USB-C®[^1] connector implementing a USB 2.0 host capable of 5 V @ 3 A continuous, which can be used to power and communicate with various downstream devices.

NavQ+ is an open source reference design provided by NXP and manufacturable by anyone.
Since NavQ+ has USB-C® ports capable of being configured as a USB Ethernet Gadget, a cable with a USB-C® connector on both ends is all that is required.

!!! note
    - Unless set otherwise, the default USB-C® port for use as an Ethernet Gadget device is configured to only the centermost USB-C® port (labeled USB 2) as shown in the example pictures.

The NavQ+ is pictured in the cargo bay using the 3D-printed [adapter](#adapter) plate and on top of the faceplate using the 3D-printed [case](#case-top).
![Hookup diagram for NavQ+ with adapter mount in cargo bay](data/hookup_navqplus_adapter_mount_bay.jpg "NavQ+ in Cargo Bay")
![Hookup diagram for NavQ+ with case on faceplate](data/hookup_navqplus_case_faceplate.jpg "NavQ+ on Faceplate")


## Printable Case
The NavQ+ has a printable case specifically designed for use with the Create® 3, allowing for it to be mounted to the faceplate or cargo bay.
The base of the case attaches to the NavQ+ using the existing four (4) M2.5-0.45 x 12mm System On Module (SOM) mounting screws.

!!! note
    - This case is designed to be fastened together with four (4) M3-0.5 x 10mm screws if not mounted to a Create® 3 plate or M3-0.5 x 12mm if mounted; cap head is suggested.
    - For best results, it is suggested to tap/thread the M3-0.5 (Create® 3 mounting/case fastening) and M2.5-0.45 (SOM) holes.

### Case Top
<details>
  <summary>3D-Rendering</summary>

  <script src="https://embed.github.com/view/3d/iRobotEducation/create3_docs/main/docs/hw/data/cases/C3-NavQPlus-Top.stl"></script>

</details>


* [Case Top STL (170.5 kB)](data/cases/C3-NavQPlus-Top.stl)
* [Case Top STEP (413.5 kB)](data/cases/C3-NavQPlus-Top.stp)

### Case Bottom
<details>
  <summary>3D-Rendering</summary>

  <script src="https://embed.github.com/view/3d/iRobotEducation/create3_docs/main/docs/hw/data/cases/C3-NavQPlus-Base.stl"></script>

</details>


* [Case Base STL (150.7 kB)](data/cases/C3-NavQPlus-Base.stl)
* [Case Base STEP (130.2 kB)](data/cases/C3-NavQPlus-Base.stp)

Setup showing faceplate mounted case and printable [sensor brackets](https://github.com/iRobotEducation/create3_docs/tree/main/docs/hw/data/brackets).
![Sensor faceplate hookup example.](data/navqplus_case_sensors.jpg "NavQ+ with sensors on Faceplate")


## Printable Adapter
If a more minimal mount is desired instead of a case, an adapter plate using the existing SOM mounting screws for fastening is also provided.

!!! note
    - This adapter is designed to be fastened to the Create® 3 plate with four (4) M3-0.5 x 6mm screws; cap head is suggested.
    - For best results, it is suggested to tap/thread the M3-0.5 (Create® 3 mounting) and M2.5-0.45 (SOM) holes.

### Adapter

<details>
  <summary>3D-Rendering</summary>

  <script src="https://embed.github.com/view/3d/iRobotEducation/create3_docs/main/docs/hw/data/brackets/C3-RudisLabs-NavQPlus-Adapter.stl"></script>

</details>


* [Adapter STL (1.2 MB)](data/brackets/C3-RudisLabs-NavQPlus-Adapter.stl)
* [Adapter STEP (3.4 MB)](data/brackets/C3-RudisLabs-NavQPlus-Adapter.stp)

[^1]: USB-C® is a trademark of USB Implementers Forum.
[^2]: All other trademarks mentioned are the property of their respective owners.
