# Connect Create® 3 to Wi-Fi
## The Basics
Follow the main guide for getting started [here](https://edu.irobot.com/create3-setup).

## Select RMW Implementation
If you are planning to use ROS 2, make sure you have selected the matching RMW implementation as the rest of the nodes in your system.
This can be found in the Application &rarr; Configuration menu in the Create® 3 robot's web server, shown in the below image.

![Application Configuration Detail](data/appconfig.png)

The default RMW for ROS 2 Galactic is Cyclone DDS.
Be sure to click "save" after making any changes, and then restart the application.
!!! attention
    **As of Create 3 software version G.2.2, there is a memory leak in Cyclone DDS that can cause the robot to reboot after a few hours of use. Please monitor for [this issue](https://github.com/ros2/rmw_cyclonedds/issues/388) further information. Fast-DDS does not have this problem.**

See [ROS 2 Network Config](xml-config.md) for more information about RMW specific choices and configuration requirements.

## Using Multiple Robots

!!! important
    If you plan to use multiple Create® 3 robots connected to the same Wi-Fi network, then **you must follow the [Multi-Robot Setup documentation](multi-robot.md)**
