# User Interface

The Create® 3 robot can interact with the user through its buttons and its lightring.

### Responding to buttons presses

Whenever a button on the Create® 3 robot is pressed, its information will be published on the `interface_buttons` topic.
By subscribing to this topic, you will be able to detect when to start your custom policies.

### Changing the lightring colors

!!! attention 
    **The Create® 3 robot uses its lightring to notify the user about critical events. If you override its color, you may not notice these events.**

You can change the color of the lightring on your Create® 3 robot by publishing a corresponding message on the `cmd_lightring` topic.

```bash
ros2 topic pub /cmd_lightring irobot_create_msgs/msg/LightringLeds "{override_system: true, leds: [{red: 255, green: 0, blue: 0}, {red: 0, green: 255, blue: 0}, {red: 0, green: 0, blue: 255}, {red: 255, green: 255, blue: 0}, {red: 255, green: 0, blue: 255}, {red: 0, green: 255, blue: 255}]}"
```

The easiest way to return lights to the default color (and relinquish their control to the robot) is to publish an empty message on the topic.

```bash
ros2 topic pub /cmd_lightring irobot_create_msgs/msg/LightringLeds "{}"
```

Additionally, an action server named `led_animation` can take Blink or Spin animation goals to execute a pattern for a fixed duration.
See [LedAnimation.action](https://github.com/iRobotEducation/irobot_create_msgs/blob/main/action/LedAnimation.action).


For example you can run the following.

```bash
ros2 action send_goal led_animation irobot_create_msgs/action/LedAnimation "{animation_type: 1, lightring: {leds: [{red: 255, green: 0, blue: 0}, {red: 0, green: 255, blue: 0}, {red: 0, green: 0, blue: 255}, {red: 255, green: 255, blue: 0}, {red: 255, green: 0, blue: 255}, {red: 0, green: 255, blue: 255}], override_system: true},max_runtime: {sec: 500, nanosec: 0}}"
```
