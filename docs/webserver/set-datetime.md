# iRobot® Create® 3 Webserver - Set Date and Time
The Set Date and Time page of the Create® 3 webserver allows the user to directy change the robot's date and time.

!!!warning
    Please note that this is a beta feature, and as such is not supported by the customer service team.
    Please exercise caution, as improper use of beta features may result in an inoperable robot.

![Picture of set date and time page](data/set-datetime.png)

The page first shows the current date and time on the robot on load.
Simply change the date and time and click "save" to save.

This feature can also be accessed by sending a POST to `/api/set-datetime/newdatetime={YYYY-MM-DDThh:mm:ss}`.

[^1]: All trademarks mentioned are the property of their respective owners.