# ROS 2 APIs

The Create® 3 robot is based on ROS 2[^1] and, as such, it exposes all its user-facing APIs through ROS 2 entities (topics, services, actions and parameters).

The purpose of this page is to give a quick overview of these ROS 2 APIs.
The robot uses standard ROS 2 messages when available and implements custom messages in [irobot_create_msgs](https://github.com/iRobotEducation/irobot_create_msgs) for data not represented by standard messages.
If you are interested in more details, have a look at the other pages in this section.

## ROS 2 Topics

You can see the ROS 2 topics exposed by the Create® 3 robot running the `ros2 topic list` command.

```bash
$ ros2 topic list -t
/battery_state [sensor_msgs/msg/BatteryState]
/cliff_intensity [irobot_create_msgs/msg/IrIntensityVector]
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
/tf [tf2_msgs/msg/TFMessage]
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

If you have trouble seeing the topics using `ros2 topic list`, ensure that the robot's `RMW_IMPLEMENTATION` matches the one on your machine; see [Network Configuration](../setup/xml-config.md) for more information about <ins>R</ins>OS <ins>m</ins>iddle<ins>w</ins>are (RMW).
Additionally, the command line `ros2 topic` utility could use stale cached discovery information; try running it with additional arguments `ros2 topic list --no-daemon --spin-time 10` to not use the cached information.

## ROS 2 Services

You can see the ROS 2 servers exposed by the Create® 3 robot running the `ros2 service list` command.

```bash
$ ros2 service list -t
/e_stop [irobot_create_msgs/srv/EStop]
/motion_control/describe_parameters [rcl_interfaces/srv/DescribeParameters]
/motion_control/get_parameter_types [rcl_interfaces/srv/GetParameterTypes]
/motion_control/get_parameters [rcl_interfaces/srv/GetParameters]
/motion_control/list_parameters [rcl_interfaces/srv/ListParameters]
/motion_control/set_parameters [rcl_interfaces/srv/SetParameters]
/motion_control/set_parameters_atomically [rcl_interfaces/srv/SetParametersAtomically]
/robot_power [irobot_create_msgs/srv/RobotPower]
/robot_state/change_state [lifecycle_msgs/srv/ChangeState]
/robot_state/get_available_states [lifecycle_msgs/srv/GetAvailableStates]
/robot_state/get_available_transitions [lifecycle_msgs/srv/GetAvailableTransitions]
/robot_state/get_state [lifecycle_msgs/srv/GetState]
/robot_state/get_transition_graph [lifecycle_msgs/srv/GetAvailableTransitions]
/static_transform/change_state [lifecycle_msgs/srv/ChangeState]
/static_transform/describe_parameters [rcl_interfaces/srv/DescribeParameters]
/static_transform/get_available_states [lifecycle_msgs/srv/GetAvailableStates]
/static_transform/get_available_transitions [lifecycle_msgs/srv/GetAvailableTransitions]
/static_transform/get_parameter_types [rcl_interfaces/srv/GetParameterTypes]
/static_transform/get_parameters [rcl_interfaces/srv/GetParameters]
/static_transform/get_state [lifecycle_msgs/srv/GetState]
/static_transform/get_transition_graph [lifecycle_msgs/srv/GetAvailableTransitions]
/static_transform/list_parameters [rcl_interfaces/srv/ListParameters]
/static_transform/set_parameters [rcl_interfaces/srv/SetParameters]
/static_transform/set_parameters_atomically [rcl_interfaces/srv/SetParametersAtomically]
```

## ROS 2 Actions

You can see the ROS 2 action servers exposed by the Create® 3 robot running the `ros2 action list` command.

```bash
$ ros2 action list -t
/audio_note_sequence [irobot_create_msgs/action/AudioNoteSequence]
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
  min_speed
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
/robot_state:
  publish_odom_tfs
  qos_overrides./tf.publisher.depth
  qos_overrides./tf.publisher.durability
  qos_overrides./tf.publisher.history
  qos_overrides./tf.publisher.reliability
  use_sim_time
/static_transform:
  qos_overrides./tf_static.publisher.depth
  qos_overrides./tf_static.publisher.history
  qos_overrides./tf_static.publisher.reliability
  use_sim_time
  wheel_base
  wheels_encoder_resolution
  wheels_radius
/system_health:
  log_period
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  use_sim_time
/ui_mgr:
  lightring_led_brightness
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  use_sim_time
```

 - Morphology parameters such as `wheel_base` and `wheels_encoder_resolution` are read-only parameters that can be used in order to implement your estimation or motion control algorithms.
 - The `safety_override` parameter allows user to enable/disable safety features (default: none).
For more details, please have a look at the [safety documentation](safety.md).
 - The `publish_odom_tfs` parameter allows the user to enable transformations from `odom` (boolean, default: true).
   This parameter cannot be set at runtime; it must be configured from the [ROS 2 parameters file on the application configuration page](../../webserver/application/#application-ros-2-parameters-file) of the webserver, as it is loaded only at application start.
 - The `wheel_accel_limit` parameter sets acceleration limits in units of mm·s<sup>-2</sup> (int between 1 and 900 inclusive, default: 900).
 - The `lightring_led_brightness` parameter allows user to increase/decrease the brightness of the light ring (int between 10 - 100 inclusive, default: 15).

For more details on how to use and configure reflexes, please have a look at the [reflexes documentation](reflexes.md).

## ROS 2 Coordinate System

The Create® 3 robot produces a fused odometry that combines its wheel encoders, IMU, and ground optical flow sensor.
The robot's coordinate system is right-handed, with x forward, y left, and z up.
It exposes this coordinate system both through the tf tree and the `/odom` publication.
The `/tf` tree from the robot exposes ROS 2 standard transforms `odom->base_footprint` and `odom->base_link` with corresponding definitions [odom](https://www.ros.org/reps/rep-0105.html#odom), [base_footprint](https://www.ros.org/reps/rep-0120.html#base-footprint), and [base_link](https://www.ros.org/reps/rep-0120.html#base-link).
`base_link` is defined to be at the center of rotation of the robot with z height intersecting the floor.
`base_footprint` is the 2D planar representation `base_link` with the pitch and roll factors removed from the transform, this can be useful for applications like 2D planar mapping.
The `/odom` publication contains the same position and orientation as `base_link` in the form of a `nav_msgs/msg/Odometry` message with velocity additionally populated.
Note: the `/odom` -> `/base_footprint` and `/odom` -> `base_link` transformations can be disabled by setting the `publish_odom_tfs` parameter to `false`.
The `publish_odom_tfs` parameter cannot be set at runtime; it must be configured from the [ROS 2 parameters file on the application configuration page](../../webserver/application/#application-ros-2-parameters-file) of the webserver, as it is loaded only at application start.

```bash
$ ros2 topic echo /tf
transforms:
- header:
    stamp:
      sec: 1646697192
      nanosec: 702756640
    frame_id: odom
  child_frame_id: base_footprint
  transform:
    translation:
      x: -0.00043813258525915444
      y: -3.853919679386308e-06
      z: 0.0
    rotation:
      x: 0.0
      y: 0.0
      z: 2.5629995434428565e-05
      w: 1.0
- header:
    stamp:
      sec: 1646697192
      nanosec: 702756640
    frame_id: odom
  child_frame_id: base_link
  transform:
    translation:
      x: -0.00043813258525915444
      y: -3.853919679386308e-06
      z: 0.0
    rotation:
      x: -0.0016827837098389864
      y: -0.009617267176508904
      z: 9.441922884434462e-06
      w: 0.9999523162841797
```

[^1]: ROS 2 is governed by Open Robotics
[^2]: All trademarks mentioned are the property of their respective owners.
