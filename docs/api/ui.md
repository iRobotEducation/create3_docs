# User Interface

The Create® 3 robot can interact with the user through its buttons and its light ring.

### Responding to buttons presses

Whenever a button on the Create® 3 robot is pressed, its information will be published on the `interface_buttons` topic.
By subscribing to this topic, you will be able to detect when to start your custom policies.

### Changing the light ring colors

!!! attention 
    **The Create® 3 robot uses its light ring to notify the user about critical events. If you override its color, you may not notice these events.**

You can change the color of the light ring on your Create® 3 robot by publishing a corresponding message on the `cmd_lightring` topic.

```bash
ros2 topic pub /cmd_lightring irobot_create_msgs/msg/LightringLeds "{override_system: true, leds: [{red: 255, green: 0, blue: 0}, {red: 0, green: 255, blue: 0}, {red: 0, green: 0, blue: 255}, {red: 255, green: 255, blue: 0}, {red: 255, green: 0, blue: 255}, {red: 0, green: 255, blue: 255}]}"
```

The easiest way to return lights to the default color (and relinquish their control to the robot) is to publish an empty message on the topic.

```bash
ros2 topic pub /cmd_lightring irobot_create_msgs/msg/LightringLeds "{}"
```

Additionally, an action server named `led_animation` can take Blink or Spin animation goals to execute a pattern for a fixed duration.
See [LedAnimation.action](https://github.com/iRobotEducation/irobot_create_msgs/blob/main/action/LedAnimation.action).


For example you can run the following:

```bash
ros2 action send_goal led_animation irobot_create_msgs/action/LedAnimation "{animation_type: 1, lightring: {leds: [{red: 255, green: 0, blue: 0}, {red: 0, green: 255, blue: 0}, {red: 0, green: 0, blue: 255}, {red: 255, green: 255, blue: 0}, {red: 255, green: 0, blue: 255}, {red: 0, green: 255, blue: 255}], override_system: true},max_runtime: {sec: 500, nanosec: 0}}"
```

### Playing sound through the speakers

You can play sound out of your Create® 3 robot speakers by publishing a corresponding message on the `cmd_audio` topic.

```bash
ros2 topic pub /cmd_audio irobot_create_msgs/msg/AudioNoteVector "{append: false, notes: [{frequency: 100, max_runtime: {sec: 1,nanosec: 0}}, {frequency: 50, max_runtime: {sec: 1,nanosec: 0}}]}"
```

This example command will play 2 notes at the given frequencies back to back with the given 1 second length for each note.
`append` is used to dictate the policy if an audio sequence is already playing when a new value comes in on the topic.
`append: true` tells the sound manager to play this audio sequence after the current sequence finishes playing.
`append: false` tell the sound manager to override any currently playing sequence with the new sequence.
Publishing an empty `notes` vector with `append: false` will stop any currently playing audio sequences.
