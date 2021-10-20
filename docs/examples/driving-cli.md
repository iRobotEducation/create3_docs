# Driving via ROS 2 Command Line

This page describes how to drive the Create® 3 robot using the ROS 2 command line tools.

#### Undock the robot

If the Create® 3 robot is on its dock, you can undock it with: 

```sh
ros2 action send_goal /undock irobot_create_msgs/action/Undock "{}"
```

#### Command velocities

You can drive around the Create® 3 robot by publishing standard `Twist` messages on the `/cmd_vel` topic.

```sh
ros2 topic pub -r 20 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

#### Dock the robot

If the Create® 3 robot seeing its dock (check the [docking documentation](../api/docking.md) for details) you can dock it with:

```sh
ros2 action send_goal /dock irobot_create_msgs/action/DockServo "{}"
```
