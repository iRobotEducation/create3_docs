# iRobot® Create® 3 Hookup Guide

The iRobot® Create® 3 has a USB-C®[^1] connector implementing a USB 2.0 host capable of 5 V @ 3 A continuous, which can be used to power and communicate with various downstream devices.
Here are some hookup examples.

## NVIDIA® Jetson Nano™ 2GB
The Jetson Nano™[^2] 2GB has a USB-C® port (J2) for power and a USB Micro-B port (J13) for downstream data.
This can be connected to the Create 3 most simply using a USB-C® hub and two cables -- USB A to Micro-B and USB A to USB-C®.
![Hookup diagram for Jetson Nano™](data/hookup_nano2gb.jpg "Jetson Nano™ 2GB")

## NVIDIA® Jetson Xavier NX™ Developer Kit
The [Jetson Xavier NX™ Developer Kit](https://developer.nvidia.com/embedded/jetson-xavier-nx-devkit) has a 5.5mm x 2.5mm barrel connector jack (J16) for power (9 V to 20 V) and a USB Micro-B port (J5) for downstream data.<br>
This can be powered from the unregulated battery port of the Create® 3  adapter board by using a JST-XH female connector to DC barrel plug cable.
The data connection is established by using a USB Micro B to USB-C® cable.
![Hookup diagram for Jetson Xavier NX™ Developer Kit](data/hookup_jetson_xavier_nx.jpg "Jetson Xavier NX™ Developer Kit")

### Mounting NVIDIA® Jetson Xavier NX™ Developer Kit
You can 3d print the [mount adapter](data/brackets/C3-JetsonXavierNX-Mount.stl) to place the Jetson Xavier NX Developer Kit in the cargo bay or on the faceplate.

<details>
  <summary>3D-Rendering</summary>

  <script src="https://embed.github.com/view/3d/iRobotEducation/create3_docs/main/docs/hw/data/brackets/data/brackets/C3-JetsonXavierNX-Mount.stl"></script>

</details>



!!! note
    - If you are 3d printing the above mount adapter, use **support** to support overhang areas. ([slicing example](data/brackets/C3-JetsonXavierNX-Mount_slice-example.png))
    - You need four (4) M3 x 6mm screws; cap head is suggested.

[^1]: USB-C® is a trademark of USB Implementers Forum.
[^2]: NVIDIA and Jetson Nano are trademarks or registered trademarks of NVIDIA Corporation.
[^3]: All other trademarks mentioned are the property of their respective owners.