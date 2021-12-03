# Create® 3 Drive Goals

The Create® 3 robot exposes some actions for simple driving goals that close the loop on odometry position.

Through the ROS 2 APIs users can command:

 * Driving along a specified arc

 * Driving in a straight line for a fixed distance

 * Navigating to a specified odometry position and orientation

 * Rotating a fixed angle

A cliff event or a wheel stall will trigger a goal to cancel,
otherwise it will run until the robot achieves the odometry goal or it's canceled by the user.
If there is something blocking the robot's path,
the user must intervene to stop the robot,
otherwise it will continue to bump until odometry slip achieves the goal position.

## Built-in Drive Goals behaviors

#### Drive Arc

You can command the robot to drive a fixed angle along an arc defined by radius:

```bash
ros2 action send_goal /drive_arc irobot_create_msgs/action/DriveArc "{angle: 1.57,radius: 0.3,translate_direction: 1,max_translation_speed: 0.3}"
```

The robot will drive forward or backward given the translate direction along an arc defined by radius until it achieves the specified relative heading.

#### Drive Distance

You can command the robot to drive a fixed distance in a straight line:

```bash
ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance "{distance: 0.5,max_translation_speed: 0.15}"
```

The robot will drive straight until it has traveled the specified distance in odometry frame.
It will drive backwards if distance is negative (be aware of the [backup limit](../safety/#backup-limit)).

#### Navigate To Position

You can command the robot to drive to the specified odometry position:

```bash
ros2 action send_goal /navigate_to_position irobot_create_msgs/action/NavigateToPosition "{achieve_goal_heading: true,goal_pose:{pose:{position:{x: 1,y: 0.2,z: 0.0}, orientation:{x: 0.0,y: 0.0, z: 0.0, w: 1.0}}}}"
```

The robot will take a rotate -> translate -> rotate approach to achieve the goal position.
First rotating from its current heading to face the goal position, then driving straight to the goal position,
then optionally rotating to achieve the goal heading. 

#### Rotate Angle

You can command the robot to rotate a relative angle from current robot heading:

```bash
ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: 1.57,max_rotation_speed: 0.5}"
```

The robot will rotate either clockwise (negative angle) or counter clockwise (positive angle) until it has achieved the angle offset.

