# Actuators via ROS 2 Command Line

This page describes how to use the the Create® 3 robot's actuators using the ROS 2 command line tools.

## Audio

### Play a sequence of notes

Good times:
```sh
ros2 topic pub /cmd_audio irobot_create_msgs/msg/AudioNoteVector "{append: false, notes: [{frequency: 392, max_runtime: {sec: 0,nanosec: 177500000}}, {frequency: 523, max_runtime: {sec: 0,nanosec: 355000000}}, {frequency: 587, max_runtime: {sec: 0,nanosec: 177500000}}, {frequency: 784, max_runtime: {sec: 0,nanosec: 533000000}}]}" -1
```

Bad times:
```sh
ros2 topic pub /cmd_audio irobot_create_msgs/msg/AudioNoteVector "{append: false, notes: [{frequency: 369, max_runtime: {sec: 0,nanosec: 355000000}}, {frequency: 300, max_runtime: {sec: 0,nanosec: 533000000}}]}" -1
```

## Driving

### Command velocities

You can drive around the Create® 3 robot by publishing standard `Twist` messages on the `/cmd_vel` topic.

```sh
ros2 topic pub -r 20 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

### Drive a distance
The Drive Distance action takes a distance in meters and maximum speed in meters per second.
```sh
ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance "{distance: 0.5,max_translation_speed: 0.15}"
```

### Rotate an angle
The Rotate Angle action takes a turn angle in radians and maximum angular speed in radians per second.
```sh
ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: 1.57,max_rotation_speed: 0.5}"
```

### Docking

#### Undock the robot

If the Create® 3 robot is on its dock, you can undock it with:

```sh
ros2 action send_goal /undock irobot_create_msgs/action/Undock "{}"
```

#### Dock the robot

If the Create® 3 robot sees its dock (check the [docking documentation](../api/docking.md) for details) you can dock it with:

```sh
ros2 action send_goal /dock irobot_create_msgs/action/DockServo "{}"
```

### E-Stop

### Enable E-Stop
If under the robot's control, its light ring will turn yellow when the motors are disabled.
```sh
ros2 service call /e_stop irobot_create_msgs/srv/EStop "{e_stop_on: true}"
```

### Disable E-Stop
```sh
ros2 service call /e_stop irobot_create_msgs/srv/EStop "{e_stop_on: false}"
```

## Light Ring

### Multicolor
```sh
ros2 topic pub /cmd_lightring irobot_create_msgs/msg/LightringLeds "{override_system: true, leds: [{red: 255, green: 0, blue: 0}, {red: 0, green: 255, blue: 0}, {red: 0, green: 0, blue: 255}, {red: 255, green: 255, blue: 0}, {red: 255, green: 0, blue: 255}, {red: 0, green: 255, blue: 255}]}" -1
```

### Return static control to Create 3 Robot
```sh
ros2 topic pub /cmd_lightring irobot_create_msgs/msg/LightringLeds "{override_system: false, leds: [{red: 255, green: 0, blue: 0}, {red: 0, green: 255, blue: 0}, {red: 0, green: 0, blue: 255}, {red: 255, green: 255, blue: 0}, {red: 255, green: 0, blue: 255}, {red: 0, green: 255, blue: 255}]}" -1
```

### Animations
```sh
# Note: type 1 is blink and type 2 is spin
ros2 action send_goal /led_animation irobot_create_msgs/action/LedAnimation "{animation_type: 2,max_runtime:{sec: 10,nanosec: 0},lightring:{override_system: true, leds: [{red: 255, green: 0, blue: 0}, {red: 0, green: 255, blue: 0}, {red: 0, green: 0, blue: 255}, {red: 255, green: 255, blue: 0}, {red: 255, green: 0, blue: 255}, {red: 0, green: 255, blue: 255}]}}"
```

## Robot Power
Warning: this turns the robot and payload off immediately
```sh
ros2 service call /robot_power irobot_create_msgs/srv/RobotPower "{}"
```
