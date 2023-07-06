# iRobot® Create® 3 Webserver - Restart ntpd
The "Restart ntpd" beta menu option of the Create® 3 webserver instructs the Create® 3 robot to resynchronize its clock.

!!!warning
    Please note that this is a beta feature, and as such is not supported by the customer service team.
    Please exercise caution, as improper use of beta features may result in an inoperable robot.

Selecting the "Restart ntpd" option will spawn a pop-up requesting confirmation.
Restarting the ntp daemon will trigger a time resynchronization with the first time server found.

This feature can also be accessed by sending a POST to `/api/restart-ntpd`.

[^1]: All trademarks mentioned are the property of their respective owners.