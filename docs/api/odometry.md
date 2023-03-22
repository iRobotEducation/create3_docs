# Odometry Estimation

The Create® 3 robot is equipped with a variety of sensors that are used to detect its motions.
In particular you will find:

 - IMU
 - Optical mouse
 - Wheel encoders

Many details about these messages can be found in the message definitions themselves, which are linked below.

## Raw sensor topics

If you want to implement your own algorithms using the raw sensor readings, you can read them from the following topics:

```bash
/imu
/mouse
/wheel_status
/wheel_ticks
/wheel_vels
```

### The `imu` topic

The `imu` topic produces messages of type [`sensor_msgs/msg/Imu`](https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/Imu.msg).
As of G.4 / H.1, this topic publishes at 100 Hz.
Prior to these releases, this topic published at 62.5 Hz.

### The `mouse` topic

The `mouse` topic produces messages of type [irobot_create_msgs/msg/Mouse](https://github.com/iRobotEducation/irobot_create_msgs/blob/rolling/msg/Mouse.msg).
This topic publishes at 62.5 Hz.

### The `wheel_status` topic

The `wheel_status` topic produces messages of type [irobot_create_msgs/msg/WheelStatus](https://github.com/iRobotEducation/irobot_create_msgs/blob/rolling/msg/WheelStatus.msg).
This topic publishes at 62.5 Hz.

### The `wheel_ticks` topic

The `wheel_ticks` topic produces messages of type [irobot_create_msgs/msg/WheelTicks](https://github.com/iRobotEducation/irobot_create_msgs/blob/rolling/msg/WheelStatus.msg).
This topic publishes at 62.5 Hz.
There are 508.8 ticks per wheel rotation.

### The `wheel_vels` topic

The `wheel_status` topic produces messages of type [irobot_create_msgs/msg/WheelStatus](https://github.com/iRobotEducation/irobot_create_msgs/blob/rolling/msg/WheelVels.msg).
This topic publishes at 62.5 Hz.

## The `odom` topic

The `odom` topic produces messages of type [nav_msgs/msg/Odometry](https://github.com/ros2/common_interfaces/blob/rolling/nav_msgs/msg/Odometry.msg).
The Create® 3 robot fuses the reading from its various sensors in order to produce a dead reckoning estimate of its pose on the `odom` topic.

## The `slip_status` topic

The `slip_status` topic produces messages of type [irobot_create_msgs/msg/SlipStatus](https://github.com/iRobotEducation/irobot_create_msgs/blob/rolling/msg/SlipStatus.msg).
We denote by "slippage" a loss of efficiency in the wheels.
This is usually caused by losing traction between the wheels and the ground with the results that the motion detected by the wheels encoders is greater than what the robot actually performed.

We fuse together various sensors in order to compute a boolean estimate of whether the robot is slipping or not and we periodically publish it on the `slip_status` topic.
If you are developing your own state estimation algorithm using the wheels encoders, then it is recommended to inflate the differential motion covariance matrix to take this problem into account.

Note that the optical mouse sensor is not affected by slippage.

## The `stop_status` topic

The `stop_status` topic produces messages of type [irobot_create_msgs/msg/StopStatus](https://github.com/iRobotEducation/irobot_create_msgs/blob/rolling/msg/StopStatus.msg).
The Create® 3 robot will periodically publish a boolean estimate of whether it is currently moving or not on the `stop_status` topic.

[^1]: All trademarks mentioned are the property of their respective owners.
