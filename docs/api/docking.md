# Create® 3 Docking

The Create® 3 robot is equipped with a docking station to recharge it between experiments.

Through the ROS 2[^1] APIs users can command docking and undocking autonomous behaviors.

!!! warning
    Note that the docking action and sensor topic changed between Galactic and Humble.

In order for the robot to detect the dock, determine its location, and understand when it is succesfully docked, it is necessary that the docking station is connected to a power source.

## Autonomous behaviors

#### Undocking

You can command the robot to undock using the following ROS 2 action.

```bash
ros2 action send_goal /undock irobot_create_msgs/action/Undock "{}"
```

The robot will move backward out of the dock and then it will rotate 180 degrees.

This action will fail if the robot is already undocked.

#### Docking

You can command the robot to dock using a ROS 2 action.

##### Galactic
```bash
ros2 action send_goal /dock irobot_create_msgs/action/DockServo "{}"
```

##### Humble
```bash
ros2 action send_goal /dock irobot_create_msgs/action/Dock "{}"
```

The robot will first search for the dock in its immediate surroundings.
Note that the action will fail if the robot is too far from the dock.
You can check if the dock is visible by subscribing to the (in Galactic) `/dock` (or in Humble) `/dock_status` ROS 2 topic.

Then the robot will align with the dock and carefully drive onto it.

This action will fail if the robot is already docked.

## Docking sensor data

The Create® 3 robot exposes several docking-related information through its ROS 2 publications.
These should allow users to write their own algorithms taking into account the presence of the dock in the environment and even to write their own docking and undocking procedures.

#### IR opcodes

The Create® 3 docking station transmit several IR signals.
The Create® 3 robot is equipped with two different sensors that are capable of detecting them.

![Docking signals](data/create3_dock_codes.png)

The robot will publish these signals in the `/ir_opcode` ROS 2 topic.
Each message will contain a time-stamped detection of one of those signals, including the identifier of the sensor that detected it.

#### Dock information

In Galactic, more high-level information is produced by the robot in the `/dock` ROS 2 topic.
In Humble and beyond, the topic has been renamed to `/dock_status`.
Here it's possible to quickly know if the robot is able to see the dock from its current location and whether it is currently docked or not.

[^1]: ROS 2 is governed by Open Robotics
[^2]: All trademarks mentioned are the property of their respective owners.
