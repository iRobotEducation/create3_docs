# iRobot® Create® 3 Webserver Overview
The Create® 3 robot runs a configuration webserver for modifying settings of the robot.
This is a separate process from its ROS 2[^1] application; it is running regardless of the status of that application.
The webserver can be accessed via the robot's `usb0` (Ethernet over USB host), `wlan0` (provisioned to an external access point), or `wlan1` (robot as its own access point) interfaces.
It is not recommended to run the robot's access point while also controlling the robot via ROS 2 or iRobot Coding.

Please use the menu to navigate between sections of the webserver.

[^1]: ROS 2 is governed by Open Robotics
[^2]: All other trademarks mentioned are the property of their respective owners.