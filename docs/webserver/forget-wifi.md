# iRobot® Create® 3 Webserver - Forget Wi-Fi Network
The "Forget Wi-Fi Network" beta menu option of the Create® 3 webserver instructs the Create® 3 robot to forget about and disconnect from any Wi-Fi networks to which it had been connected.

!!!warning
    Please note that this is a beta feature, and as such is not supported by the customer service team.
    Please exercise caution, as improper use of beta features may result in an inoperable robot.

Selecting the "Forget Wi-Fi Network" option will spawn a pop-up requesting confirmation.
Once confirmed, the robot will forget about any SSIDs to which it has connected, and to immediately disconnect from the `wlan0` inteface if it is currently connected.
If this command is issued over `wlan0`, it will be necessary to communicate with the robot either in AP mode or using Ethernet-over-USB.

This feature can also be accessed by sending a POST to `/api/forget-wifi`.

[^1]: All trademarks mentioned are the property of their respective owners.