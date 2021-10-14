# Reflexes

With the word "reflex" we denote a set of autonomous reactive behaviors that the Create3 robot will trigger when it detects obstacles or hazards.

Reflexes are high-priority behaviors and will temporarily override any user-provided command for their short duration.

Reflexes can be enabled or disabled on the Create3 using the corresponding ROS 2 parameters exposed by the `motion_control` ROS 2 node.

## Reflex parameters

The `reflexes_enabled` parameter controls whether reflexes should be executed or not. It accepts boolean values.
When this parameter is set to `false`, no reflexes will be enabled, regardless of their specific parameters values.

Reflexes are enabled by default.

### Bumps reflex

The `reflex.REFLEX_BUMP` ROS 2 parameter enables (`true`) or disables (`false`) the bump reflex.
It will trigger as soon as the robot bumps into an obstacle and it will move the robot away from it.
The reflex will continue until the robot has cleared the bump.

This reflex is enabled by default.

### Cliffs reflex

The `reflex.REFLEX_CLIFF` ROS 2 parameter enables (`true`) or disables (`false`) the cliff reflex.
It will trigger as soon as the robot detects a cliff and it will move the robot away from it.
The reflex will continue until the robot has cleared the cliff.

This reflex is enabled by default.

### Dock avoidance reflex

The `reflex.REFLEX_DOCK_AVOID` ROS 2 parameter enables (`true`) or disables (`false`) the dock avoidance reflex.
It will trigger as soon as the robot gets close to the dock and tries to move towards it.
The reflex will stop forward movements.

This reflex is disabled by default.

### Gyro calibration reflex

The `reflex.REFLEX_GYRO_CAL` ROS 2 parameter enables (`true`) or disables (`false`) the gyro calibration reflex.
It will trigger while the robot is stationary and will try to recalibrate the internal gyroscope.

This reflex is enabled by default.

### Panic reflex

The `reflex.REFLEX_PANIC` ROS 2 parameter enables (`true`) or disables (`false`) the dock avoidance reflex.
It will trigger when the robot is trapped and unable to clear obstacles or hazards.
The reflex will try more aggressive maneuvers to allow the robot to recover from this situation

This reflex is enabled by default.

### Proximity slowdown reflex

The `reflex.REFLEX_PROXIMITY_SLOWDOWN` ROS 2 parameter enables (`true`) or disables (`false`) the dock avoidance reflex.
It will trigger when the robot's IR sensors detect an obstacle in close proximity.
The reflex will reduce the robot movement speed in order to better prepare for an eventual impact.

This reflex is enabled by default.

### Stuck reflex

The `reflex.REFLEX_STUCK` ROS 2 parameter enables (`true`) or disables (`false`) the dock avoidance reflex.
It will trigger when the robot is stuck, i.e. it's pushing against an obstacle and its wheels are losing traction.
The reflex will try aggressive maneuvers to allow the robot to recover from this situation

This reflex is enabled by default.

### Virtual Wall reflex

The `reflex.REFLEX_VIRTUAL_WALL` ROS 2 parameter enables (`true`) or disables (`false`) the cliff reflex.
It will trigger as soon as the robot detects an iRobot virtual wall it will move the robot away from it.
The reflex will continue until the robot has cleared the virtual wall.

This reflex is enabled by default.

### Wheel drop reflex

The `reflex.REFLEX_WHEEL_DROP` ROS 2 parameter enables (`true`) or disables (`false`) the cliff reflex.
It will trigger as soon as the robot detects that one of its wheels is fully extended (dropped).
The robot will drive the other wheel in order to return to a flat surface.

This reflex is enabled by default.
