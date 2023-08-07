# iRobot® Create® 3 Electrical System

## Robot Battery
The iRobot® Create® 3 robot uses a standard [Lithium Ion Battery for Roomba® e & i series](https://store.irobot.com/default/parts-and-accessories/roomba-batteries/) robots.
The battery shipping with the robot is a 26 Wh, 4S Lithium Ion smart battery pack, with a nominal voltage of 14.4 V (12 V min, 16.8 V max).
It will report a 0% state of charge when the total voltage of the pack reaches 12.0 V.
It will self-protect and disconnect from any load at 10.8 V or lower.

!!! attention "Notice"
    If the robot is approaching a 0% state of charge and the application does not believe it will make it to the dock, the robot should be powered down using the `/robot_power` service.

If the battery self-protects, its internal management system may refuse to charge until it is reset.
Resetting the battery is accomplished by removing the battery from the robot for at least fifteen minutes, at which point it should be reinstalled in the robot and the robot placed on the charger.


!!! attention "Notice"
    When not overridden, the robot's light ring will flash red to indicate low battery state, at about 10% state of charge. It is recommended not to run the robot for extended periods of time in this state.

Charge the battery by placing Create® 3 on the included iRobot® Home Base™ Charging Station.
The light ring will show the state of charge and animate while the battery is charging.
The battery will self-protect and disable the ability to charge if it charges continuously for four hours without reaching 100% state of charge.

!!! attention "Notice"
    Always remove the Create® 3 robot’s battery prior to dismantling, adjusting, altering, or affecting the robot’s chassis at the risk of damaging the battery, robot, or both.
    Do not attempt to use the robot without its battery installed.

!!! tip
    Keep the robot on the Home Base™ charging station (or power down the robot by holding down the power button for 10 seconds) when not in use to prevent the battery from discharging.

## Buttons and Light Ring Overview
The iRobot® Create® 3 has three buttons on its top face.
The center button is marked with a power icon, while the flanking buttons are marked with one or two dots.
The center button also contains a ring of six RGB LEDs.
[Detailed information about the use of these buttons and LEDs can be found here.](../hw/face.md)

## Adapter Board Overview
The iRobot® Create® 3 robot exposes connections and some status indicators via the Adapter Board.
The Adapter Board also adds a Bluetooth® Low Energy[^1] interface to the core robot.
[Detailed information on the Adapter Board can be found here.](../hw/adapter.md)

[^1]: The Bluetooth® word mark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by iRobot is under license.
[^2]: All other trademarks mentioned are the property of their respective owners.
