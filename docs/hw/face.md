# iRobot® Create® 3 Buttons and Light Ring
![Button diagram](data/buttons.png)

## Buttons
The iRobot® Create® 3 has three buttons on its top face.
These buttons expose core functionality of the robot, but can also be overridden by the user.

### Button 1
Button 1 (to the left of center) is marked with a single dot (•).
If held for ten seconds, the robot will go into "standby" mode, keeping its charging circuitry active, and continuing to power the payload.
The robot can be placed on the dock to charge or to keep the payload alive in this mode.
To wake the robot from standby, hold the center button for one second.
Button presses can be accessed by the user in both ROS 2 and iRobot Education Bluetooth[^1] modes.

### Button 2
Button 2 (to the right of center) is marked with two dots (••).
This button is a user button only.
Button presses can be accessed by the user in both ROS 2 and iRobot Education Bluetooth[^1] modes.

### Center Button
The center button is marked with a power (⏻) icon.
If held for seven seconds, the robot will go into "storage mode," disconnecting its internal battery from the robot and its payload.
When the robot is in storage mode, the only way to power it on is to place it on the dock.
The button also contains a light ring on its circumference.

## Light Ring
The center button contains a ring of six RGB LEDs which communicate state about the robot.
The LEDs expose internal state information about the robot, but can also be overridden by the user.

### While Charging
|  Spinning White  |  Partial White  |  Solid White  |  Pulsing Red  |
| ----- | ----- | ----- | ------ |
|  ![Full spinning white](data/lightring/boot.gif){: style="height:100%;width:100%"}  |  ![Partial spinning white](data/lightring/charged_spinning.gif){: style="height:100%;width:100%"}  |  ![Solid white](data/lightring/white_solid.jpg){: style="height:100%;width:100%"}  |  ![Pulsing Red](data/lightring/red_pulsing.gif){: style="height:100%;width:100%"}  |
|  Robot is booting up.<br>Wait for "happy sound" to play.  |  Robot is charging<br>(Example shows 40%)  |  Robot is 100% charged  |  Battery < 10%  |

### While Idle
|  Spinning White  |  Solid White  |  Pulsing Red  |  Solid Red  |
| ----- | ----- | ----- | ------ |
|  ![Full spinning white](data/lightring/boot.gif){: style="height:100%;width:100%"}  |  ![Solid white](data/lightring/white_solid.jpg){: style="height:100%;width:100%"}  |  ![Pulsing Red](data/lightring/red_pulsing.gif){: style="height:100%;width:100%"}  |  ![Solid Red](data/lightring/red_solid.jpg){: style="height:100%;width:100%"}  |
|  Robot is booting up.<br>Wait for "happy sound" to play.  |  Robot is powered on  |  Battery <10%. Place on charger.  |  Robot error. Cycle power.  |

### While Connecting to Robot Access Point
|  Spinning Cyan  |  Solid Cyan  | | |
| ----- | ----- | ----- | ----- |
|  ![Spinning cyan](data/lightring/cyan_spinning.gif){: style="height:100%;width:100%"}  |  ![Solid cyan](data/lightring/cyan_solid.jpg){: style="height:100%;width:100%"}  | | |
|  Access Point is active. <br> Select robot from device’s <br> Wi-Fi menu.  |  Device is connected to <br> robot’s Access Point page.  | | |

### While Connecting to Wi-Fi
|  Solid Cyan  |  Spinning Cyan  |  Quick Green Flash  |  Solid White  |
| ----- | ----- | ----- | ----- |
|  ![Solid cyan](data/lightring/cyan_solid.jpg){: style="height:100%;width:100%"}  |  ![Spinning cyan](data/lightring/cyan_spinning.gif){: style="height:100%;width:100%"}  |  ![Green Flash](data/lightring/green_solid.jpg){: style="height:100%;width:100%"}  |  ![Solid White](data/lightring/white_solid.jpg){: style="height:100%;width:100%"}  |
|  Device is connected to <br> robot’s Access Point page.  |  Robot attempting to <br> connect to Wi-Fi  |  Success connecting to Wi-Fi  |  Robot successfully <br> disconnected from <br> Access Point page  |

|  Yellow with Red  |  Yellow with Green  |  Yellow with Blue  |  Yellow with White  |  Solid Yellow  |
| ----- | ----- | ----- | ----- | ----- |
|  ![Yellow with red](data/lightring/yellow-red_solid.jpg){: style="height:100%;width:100%"}  |  ![Yellow with green](data/lightring/yellow-green_solid.jpg){: style="height:100%;width:100%"}  |  ![Yellow with blue](data/lightring/yellow-blue_solid.jpg){: style="height:100%;width:100%"}  |  ![Yellow with white](data/lightring/yellow-white_solid.jpg){: style="height:100%;width:100%"}  |  ![Solid yellow](data/lightring/yellow_solid.jpg){: style="height:100%;width:100%"}  |
|  Failed Wi-Fi password  |  Robot cannot connect to <br> network access point | DHCP failed to obtain a valid <br> IP address before time-out. <br> Try again. |  Access point located but <br> failed association. Try again.  |  Failed to connect to Wi-Fi <br> for unknown reason  |

### While Updating Firmware
|  Solid Cyan  |  Spinning Blue  |  Spinning White  |  Solid White  |
| ----- | ----- | ----- | ----- |
|  ![Solid cyan](data/lightring/cyan_solid.jpg){: style="height:100%;width:100%"}  |  ![Spinning blue](data/lightring/blue_spinning.gif){: style="height:100%;width:100%"}  |  ![Full spinning white](data/lightring/boot.gif){: style="height:100%;width:100%"}  |  ![Solid White](data/lightring/white_solid.jpg){: style="height:100%;width:100%"}  |
|  Device is connected to <br> robot’s Access Point page.  |  Robot downloading <br> update file  |  Robot updating firmware <br> Do not remove from dock  |  Update successful  |

### While Operating
|  Spinning White  |  Solid White  |  Pulsing Red  |  Spinning Red  |  Half Solid Orange  | Half Solid Yellow  |
| ----- | ----- | ----- | ----- | ----- | ----- |
|  ![Full spinning white](data/lightring/boot.gif){: style="height:100%;width:100%"}  |  ![Solid white](data/lightring/white_solid.jpg){: style="height:100%;width:100%"}  |  ![Pulsing Red](data/lightring/red_pulsing.gif){: style="height:100%;width:100%"}  |  ![Spinning Red](data/lightring/red_spinning.gif){: style="height:100%;width:100%"}  |  ![Rear Half Orange](data/lightring/orange_half_solid.jpg){: style="height:100%;width:100%"}  |  ![Rear Half Yellow](data/lightring/yellow_half_solid.jpg){: style="height:100%;width:100%"}  |
|  Robot is booting up.<br>Wait for "happy sound" to play.  |  Default light color  |  Battery < 10%  |  Battery < 3%  |  Back-up safety activated  |  Wheels disabled  |

[^1]: The Bluetooth® word mark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by iRobot is under license.
[^2]: All other trademarks mentioned are the property of their respective owners.