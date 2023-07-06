# Hazards Detection

The Create® 3 robot is equipped with a variety of sensors that are capable to detect hazards in the environment.

In particular you will find:

 - Bumper sensor to detect front contacts.
 - Cliff sensors to detect holes and steps.
 - Wheel drop sensors to detect if a wheel is not touching the ground.

### The `hazard_detection` topic

The Create® 3 robot will periodically publish on the `hazard_detection` ROS 2[^1] topic a vector of all the currently detected hazards.
If the vector is empty, this means that no hazards are currently being detected.

Each element of the vector will denote a different hazard detection.
Look at the [HazardDetection.msg](https://github.com/iRobotEducation/irobot_create_msgs/blob/main/msg/HazardDetection.msg) definition in order to see how to differentiate different types of hazards.
The `header` field of each indivdual detection will provide all the information required to localize it.
In particular the timestamp will denote when the robot detected the hazard and the frame id will denote the location of the sensor that performed the detection.

!!! important
    The `hazard_detection` topic will also contain a `BACKUP_LIMIT` hazard if the robot safety features are preventing it from safely moving further backwards. Look at the [safety documentation](safety.md) for details and how to disable it.

### The `kidnap_status` topic

By "kidnap" we denote the action of manually lifting the robot and, eventually, placing it back in a location which may be different from the original one.

The Create® 3 robot combines together different sensors data in order to determine when it's being kidnapped.
A boolean status will be periodically published on the `kidnap_status` topic.

### Reflective Infrared Sensors

The Create 3 robot is equipped with 11 reflective IR sensors to detect hazards.

#### The `ir_intensity` topic

[7 sets of IR emitters and receivers](/hw/mechanical/#ir-proximity-sensors) are available in the front bumper to detect objects at close range.

The Create® 3 robot will periodically publish on the `ir_intensity` topic the raw intensity readings obtained from these sensors.
The message will be a vector where each element corresponds to a different sensor.
The higher the intensity value is, the closer an obstacle is to the robot.
The `header` field of each indivdual detection will provide all the information required to localize it.
In particular the timestamp will denote when the robot detected the hazard and the frame id will denote the location of the sensor that performed the detection.

#### The `cliff_intensity` topic

[4 sets of IR emitters and receivers](/hw/mechanical/#bottom-view) are available in on the bottom of the robot just behind its front bumper to detect presence or absence of the floor.

The Create® 3 robot will periodically publish on the `cliff_intensity` topic the raw intensity readings obtained from these sensors.
The message will be a vector where each element corresponds to a different sensor.
The higher the intensity value is, the more intensely the floor is perceived.
The `header` field of each indivdual detection will provide all the information required to localize it.
In particular the timestamp will denote the time of the reading and the frame id will denote the location of the sensor that performed the detection.

[^1]: ROS 2 is governed by Open Robotics
[^2]: All trademarks mentioned are the property of their respective owners.
