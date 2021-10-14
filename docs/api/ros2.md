# ROS 2 APIs

The Create3 robot is based on ROS 2 and, as such, it exposes all its user-facing APIs through ROS 2 entities (topics, services, actions and parameters).

The purpose of this page is to give a quick overview of these ROS 2 APIs.
If you are interested in more details, have a look at the other pages in this section.

## ROS 2 Topics

You can see the ROS 2 topics exposed by the robot running the `ros2 topic list` command.

```bash
$ ros2 topic list
/battery_state
/cmd_lightring
/cmd_vel
/dock
/hazard_detection
/imu
/interface_buttons
/ir_intensity
/ir_opcode
/kidnap_status
/mouse
/odom
/parameter_events
/rosout
/slip_status
/stop_status
/tf
/tf_static
/wheel_ticks
/wheel_vels
```

## ROS 2 Services

You can see the ROS 2 services exposed by the robot running the `ros2 service list` command.

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

You can see the ROS 2 actions exposed by the robot running the `ros2 action list` command.

```bash
$ ros2 action list
/dock
/undock
/wall_follow
```

## ROS 2 Parameters

You can see the ROS 2 parameters exposed by the robot running the `ros2 param list` command.

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
```
