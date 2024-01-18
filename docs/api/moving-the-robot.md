# Moving the Robot

This page describes the various APIs available to move the Create® 3 robot via ROS 2[^1].

!!! important
    Supervise your robot while executing movements, to avoid risk of damaging it or its surroundings.

!!! important
    It's recommended to not try to command robot motions if the robot is on its docking station.
    Either lift it and place it somewhere else or use the built-in [undocking behavior](../docking/#undocking).


## Velocity Control

The velocity control API is the simplest way to move the Create® 3 robot.
It's recommended for beginners and to simply try out the robot.
Being the lowest-level motion API exposed by the robot, this is also recommended to the more advanced users who want to implement their own autonomous navigation applications.

The robot is controlled by publishing [geometry_msgs/msg/Twist](https://github.com/ros2/common_interfaces/blob/rolling/geometry_msgs/msg/Twist.msg) messages to the `/cmd_vel` topic.
For example, to move the robot straight forward using the ROS 2 command line:

```bash
ros2 topic pub -r 20 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

The robot will execute the last received message on the topic until a fixed timeout period has passed or a new message is received, at which point the timer is restarted and this process begins again.
The purpose of the timeout is to provide an easy way to stop the robot, i.e. just stop sending messages rather than having to send an explicit "0", and to prevent the robot to keep moving if it has lost connectivity with the process controlling it (e.g. a script on the user's laptop).

<!---
THIS PARAMETER IS NOT YET AVAILABLE: uncomment after release
The timeout is controlled by a ROS 2 parameter provided by the `/motion_control` node and named `/wheels_stop_threshold_sec`.
This parameter can't be modified at runtime.
You can change the value of this parameter using the application ROS 2 parameters file exposed by the webserver (see details [here](../webserver/application/#application-ros-2-parameters-file)), for example adding this snippet to the file

```yaml
motion_control:
  ros__parameters:
    wheels_stop_threshold_sec: 0.1
```

You can read the currently set value using ROS 2 command line tools:

```bash
ros2 param get /motion_control wheels_stop_threshold_sec
```
--->

Note that these raw velocity commands have lower "priority" than the other request-based approaches to move the robot (described in the next sections).
The request of a position control or autonomous behavior goal will block the execution of the `cmd_vel` messages, which will be ignored until the goal terminates.
The corollary is that it's of no use to publish `cmd_vel` messages while those are running; you should rather first wait for the behavior to finish or actively cancel it.

## Position Control

The position control APIs are suitable for users who want to implement simple high-level strategies, such as driving a specific pattern.
Basic position control, based on the internal dead-reckoning estimate of the robot, is exposed to the user via ROS 2 action goals.
See the [drive goals documentation](drive-goals.md) for details.

## Autonomous Behaviors

The Create® 3 robot exposes some autonomous behaviors suitable for more specific situations.
These behaviors are controlled using ROS 2 action goals.

 - [Docking and Undocking](docking.md)
 - [Obstacle Following](wall-follow.md)


[^1]: ROS 2 is governed by Open Robotics
