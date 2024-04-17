# iRobot® Create® 3 Webserver Overview

!!! tip
    If this is your first time using the robot's web server, it's important to run through [initial setup](https://edu.irobot.com/create3-setup).

The Create® 3 robot runs a configuration webserver for modifying settings of the robot.
This is a separate process from its ROS 2[^1] application; it is running regardless of the status of that application.
The webserver can be accessed via the robot's `usb0` (Ethernet over USB host), `wlan0` (provisioned to an external access point), or `wlan1` (robot as its own access point) interfaces.
The robot has a fixed IP address of 192.168.186.2 over its `usb0` interface, and a fixed IP address of 192.168.10.1 over its `wlan1` interface.
The robot will get an IP address over DHCP as served by your network on its `wlan0` interface.
The webserver is available over http (port 80) in a browser by navigating to its IP address on whichever interface is active.

!!! attention
    It is not recommended to run the robot's access point while also controlling the robot via ROS 2 or the iRobot Education Bluetooth®[^2] protocol.

Please use the menu to navigate between sections of the webserver, or else navigate directly to the sections below:

- [Home](../webserver/home.md)
- [Connect](../webserver/connect.md)
- [Update](../webserver/update.md)
- [Logs](../webserver/logs.md)
- [Application](../webserver/application.md)
- Beta Features
    - [Serial Forwarder](../webserver/serial-config.md)
    - [Set Date and Time](../webserver/set-datetime.md)
    - [Edit ntp.conf](../webserver/edit-ntp-conf.md)
    - [Restart ntpd](../webserver/restart-ntpd.md)
    - [Set Wired Subnet](../webserver/set-wired-subnet.md)
    - [Override RMW Profile](../webserver/rmw-profile-override.md)
- [About](../webserver/about.md)

[^1]: ROS 2 is governed by Open Robotics
[^2]: The Bluetooth® word mark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by iRobot is under license.
[^3]: All other trademarks mentioned are the property of their respective owners.
