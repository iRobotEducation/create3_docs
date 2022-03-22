# iRobot® Create® 3 Hardware Overview
The Create® 3 is based on the Roomba®, a robot vacuum cleaner.
Its sensors, actuators, and compact design are capable of navigating and mapping a the whole floor of a home or office space.
The robot also ships with an iRobot® Home Base™ Charging Station.

![Create® 3 from its above-front-right, next to its dock.](data/front_iso.jpg "Robot Front")
The front of the robot features a multizone bumper with seven pairs of IR proximity sensors, which can be used to detect obstacles.
The top of the robot contains three buttons which can all be overloaded by a ROS 2 application (only the • and •• buttons can be overloaded in the iRobot Coding app.)
The power button features a ring of six RGB LEDs for indication.

![Create® 3 from its above-rear-left, with the top cover and cargo bay removed.](data/rear_iso.jpg "Robot Rear")
The faceplate and cargo bay of the robot can be removed for quick prototyping.
The faceplate is removed by rotating it on the center axis of the robot using the thumb rests, while the cargo bay is removed by simply pulling on the handle.
The locating pins on the top cover are used to install and retain the faceplate.
![How to Remove or Attach Create® 3 Faceplate](data/remove_faceplate.svg "How to Remove Create® 3 Faceplate")

There are two cable passthroughs.
The rear passthrough is good for quick prototyping while the one that penetrates the top cover and faceplate is useful to keep wires within the radius of the robot.

Also visible with the faceplate removed is the adapter board, which is used to interface to external computers either through Bluetooth®[^1] or via USB-C®[^2].
More information on this board is available on the [Electrical](../electrical/) page.

![Create® 3 from a bottom view, with the cargo bay removed.](data/bottom.jpg "Robot Bottom")
The bottom of the robot includes four cliff sensors to keep the robot on solid ground, a caster (by default, the robot's center of gravity is forward of the center axis), charging contacts, two wheels with current sensors and encoders, and an optical odometry sensor.
Not visible is the robot's IMU, which is used with the optical odometry sensor and wheel encoders to generate a fused odometry estimate.

[^1]: The Bluetooth® word mark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by iRobot is under license.
[^2]: USB-C® is a trademark of USB Implementers Forum.
[^3]: All other trademarks mentioned are the property of their respective owners.