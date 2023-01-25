# Sensors via ROS 2 Command Line

This page describes how to read the the Create® 3 robot's sensors using the ROS 2 command line tools.

## Overview
Reading the robot's sensors is as simple as
```sh
ros2 topic echo {topic}
```
where {topic} is the topic of interest. If you're not sure what topics are available, you can type
```sh
ros2 topic list --no-daemon --spin-time 10
```
The --no-daemon and --spin-time arguments are not strictly necessary, but they may help with initial discovery.

A detailed API description for each sensor can be found [here](../../api/ros2/).

## A non-exhaustive set of examples
These are relatively straighforward, but for fun:

### Battery State
```sh
ros2 topic echo /battery_state
```

### Buttons
```sh
ros2 topic echo /interface_buttons
```

### Docking State

##### Galactic
```sh
ros2 topic echo /dock
```
##### Humble
```sh
ros2 topic echo /dock_status
```


### IR Docking Sensor
```sh
ros2 topic echo /ir_opcode
```

### IR Proximity Sensors
```sh
ros2 topic echo /ir_intensity
```

### Wheel Odometry
```sh
ros2 topic echo /odom
```

### Wheel Status (includes PWM and current)
```sh
ros2 topic echo /wheel_status
```