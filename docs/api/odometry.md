# Odometry Estimation

The Create® 3 robot is equipped with a variety of sensors that are used to detect its motions.
In particular you will find:

 - IMU
 - Optical mouse
 - Wheel encoders

### Raw sensor topics

If you want to implement your own algorithms using the raw sensor readings, you can read them from the following topics:

```bash
/imu
/mouse
/wheel_status
/wheel_ticks
/wheel_vels
```

### The `odom` topic

The Create® 3 robot fuses the reading from its various sensors in order to produce a dead reckoning estimate of its pose on the `odom` topic.

### The `slip_status` topic

We denote by "slippage" a loss of efficiency in the wheels.
This is usually caused by losing traction between the wheels and the ground with the results that the motion detected by the wheels encoders is greater than what the robot actually performed.

We fuse together various sensors in order to compute a boolean estimate of whether the robot is slipping or not and we periodically publish it on the `slip_status` topic.
If you are developing your own state estimation algorithm using the wheels encoders, then it is recommended to inflate the differential motion covariance matrix to take this problem into account.

Note that the optical mouse sensor is not affected by slippage.

### The `stop_status` topic

The Create® 3 robot will periodically publish a boolean estimate of whether it is currently moving or not on the `stop_status` topic.

[^1]: All trademarks mentioned are the property of their respective owners.
