# Create® 3 Wall Follow

The Create® 3 robot exposes a ROS 2 action server to invoke a wall-following behavior.

You can command the robot to follow along an obstacle using the following ROS 2 action.

```sh
ros2 action send_goal /wall_follow irobot_create_msgs/action/WallFollow "{follow_side: 1, max_runtime: {sec: 1, nanosec: 0}}"
```

When this behavior is requested, the robot will try to engage with nearby obstacles and, after a successfull engagement, it will start following the obstacle along the specified side until the maximum runtime is reached.

The `follow_side` can be specified as left (1) or right (-1) see the [action interface](https://github.com/iRobotEducation/irobot_create_msgs/blob/main/action/WallFollow.action) for the implementation.

The robot will use a spiraling motion to try to engage with the obstacles.
The spiral will be clockwise if `follow_side` is left (1) or counter-clockwise if `follow_side` is right (-1).
