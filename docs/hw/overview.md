### iRobot® Create® 3 Hardware Overview

Create® 3 is based on the Roomba i3, a robot vacuum cleaner. Its sensors, actuators, and compact design are capable of navigating and mapping a the whole floor of a home or office space. The robot also ships with an iRobot® Home Base® Charging Station.

![Create® 3 from its above-front-right, next to its dock.](data/front_iso.jpg "Robot Front")
The front of the robot features a multizone bumper with six pairs of IR obstacle sensors. The top of the robot contains three buttons which can all be overloaded by a ROS 2 application (only the 1 and 2 buttons can be overloaded in the iRobot Coding app.) The power button features a ring of six RGB LEDs for indication.

![Create® 3 from its above-rear-left, with the top cover and cargo bay removed.](data/rear_iso.jpg "Robot Rear")
The faceplate and cargo bay of the robot can be removed for quick prototyping. The faceplate is removed by rotating it on the center axis of the robot using the thumb rests, while the cargo bay is removed by simply pulling on the handle. The locating pins on the top cover are used to install and retain the faceplate.

There are two cable passthroughs. The rear passthrough is good for quick prototyping while the one that penetrates the top cover and faceplate is useful to keep wires within the radius of the robot.

Also visible with the faceplate removed is the communications board, which is used to interface to external computers either through Bluetooth or via USB C. More information on this board is available on the [Electrical](../electrical/) page.

![Create® 3 from a bottom view, with the cargo bay removed.](data/bottom.jpg "Robot Bottom")
The bottom of the robot includes four cliff sensors to keep the robot on solid ground, a caster (by default, the robot's center of gravity is forward of the center axis), charging contacts, two wheels with current sensors and encoders, and an optical odometry sensor. Not visible is the robot's IMU, which is used with the optical odometry sensor and wheel encoders to create a fused odometry estimate.
