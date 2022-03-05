# ROS 2 APIs

The Create® 3 robot is based on ROS 2 and, as such, it exposes all its user-facing APIs through ROS 2 entities (topics, services, actions and parameters).

The purpose of this page is to give a quick overview of these ROS 2 APIs.
The robot uses standard ROS 2 messages when available and implements custom messages in [irobot_create_msgs](https://github.com/iRobotEducation/irobot_create_msgs) for data not represented by standard messages.
If you are interested in more details, have a look at the other pages in this section.

## ROS 2 Topics

You can see the ROS 2 topics exposed by the Create® 3 robot running the `ros2 topic list` command.

```bash
$ ros2 topic list -t
/battery_state [sensor_msgs/msg/BatteryState]
/cmd_audio [irobot_create_msgs/msg/AudioNoteVector]
/cmd_lightring [irobot_create_msgs/msg/LightringLeds]
/cmd_vel [geometry_msgs/msg/Twist]
/dock [irobot_create_msgs/msg/Dock]
/hazard_detection [irobot_create_msgs/msg/HazardDetectionVector]
/imu [sensor_msgs/msg/Imu]
/interface_buttons [irobot_create_msgs/msg/InterfaceButtons]
/ir_intensity [irobot_create_msgs/msg/IrIntensityVector]
/ir_opcode [irobot_create_msgs/msg/IrOpcode]
/kidnap_status [irobot_create_msgs/msg/KidnapStatus]
/mouse [irobot_create_msgs/msg/Mouse]
/odom [nav_msgs/msg/Odometry]
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
/slip_status [irobot_create_msgs/msg/SlipStatus]
/stop_status [irobot_create_msgs/msg/StopStatus]
/tf_static [tf2_msgs/msg/TFMessage]
/wheel_status [irobot_create_msgs/msg/WheelStatus]
/wheel_ticks [irobot_create_msgs/msg/WheelTicks]
/wheel_vels [irobot_create_msgs/msg/WheelVels]
```

Note that the Create® 3 robot will produce data on most of these topics.
On the other hand, some of them can be used by the user to send commands to the Create® 3 robot.
In particular, the Create® 3 robot will subscribe to the following topics:

 - `/cmd_audio`: use this topic to play specified notes from the robot speaker.
 - `/cmd_lightring`: use this topic to change the color of the light ring.
 - `/cmd_vel`: use this topic to command velocities in the robot reference frame.

For more details on the content of these topics, please have a look at their corresponding sections.

 - [Hazards](hazards.md)
 - [Odometry](odometry.md)
 - [User Interface](ui.md)

## ROS 2 Services

You can see the ROS 2 servers exposed by the Create® 3 robot running the `ros2 service list` command.

```bash
$ ros2 service list
/e_stop
/motion_control/describe_parameters
/motion_control/get_parameter_types
/motion_control/get_parameters
/motion_control/list_parameters
/motion_control/set_parameters
/motion_control/set_parameters_atomically
/robot_power
/static_transform/describe_parameters
/static_transform/get_parameter_types
/static_transform/get_parameters
/static_transform/list_parameters
/static_transform/set_parameters
/static_transform/set_parameters_atomically
```

## ROS 2 Actions

You can see the ROS 2 action servers exposed by the Create® 3 robot running the `ros2 action list` command.

```bash
$ ros2 action list -t
/dock [irobot_create_msgs/action/DockServo]
/drive_arc [irobot_create_msgs/action/DriveArc]
/drive_distance [irobot_create_msgs/action/DriveDistance]
/led_animation [irobot_create_msgs/action/LedAnimation]
/navigate_to_position [irobot_create_msgs/action/NavigateToPosition]
/rotate_angle [irobot_create_msgs/action/RotateAngle]
/undock [irobot_create_msgs/action/Undock]
/wall_follow [irobot_create_msgs/action/WallFollow]
```

For more details on how to use these actions, please have a look at their corresponding sections.

 - [Docking](docking.md)
 - [Drive Goals](drive-goals.md)

## ROS 2 Parameters

You can see the ROS 2 parameters exposed by the Create® 3 robot running the `ros2 param list` command.

```bash
$ ros2 param list
/motion_control:
  max_speed
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  reflexes.REFLEX_BUMP
  reflexes.REFLEX_CLIFF
  reflexes.REFLEX_DOCK_AVOID
  reflexes.REFLEX_GYRO_CAL
  reflexes.REFLEX_PANIC
  reflexes.REFLEX_PROXIMITY_SLOWDOWN
  reflexes.REFLEX_STUCK
  reflexes.REFLEX_VIRTUAL_WALL
  reflexes.REFLEX_WHEEL_DROP
  reflexes_enabled
  safety_override
  use_sim_time
  wheel_accel_limit
/static_transform:
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  qos_overrides./tf_static.publisher.depth
  qos_overrides./tf_static.publisher.history
  qos_overrides./tf_static.publisher.reliability
  use_sim_time
  wheel_base
  wheels_encoder_resolution
  wheels_radius
/ui_mgr:
  lightring_led_brightness
```

Morphology parameters such as `wheel_base` and `wheels_encoder_resolution` are read-only parameters that can be used in order to implement your estimation or motion control algorithms.

The `safety_override` parameter allows user to enable/disable safety features.
For more details, please have a look at the [safety documentation](safety.md).

The `lightring_led_brightness` parameter allows user to increase/decrease the brightness of the light ring.

For more details on how to use and configure reflexes, please have a look at the [reflexes documentation](reflexes.md).
