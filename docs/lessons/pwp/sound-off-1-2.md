# Sound Off, 1-2
## Details
Code your Create® 3 Robot to play musical tones and respond to button presses and other sensor input.
### Downloads and Resources
* [PDF: Sound Off, 1-2 Activity Sheet](./Create3-Sound_Off.pdf)

## The Main Idea
Robots can play musical notes by emitting sounds of different frequencies and durations. These notes can be strung together in a sequence to play simple melodies, which are used to help the robot communicate its status. A “Happy Sound” can communicate “I am ready to run,” while an “Angry Sound” can mean “I am experiencing a problem.” Explore programming different notes and melodies to give your robot its own voice!

## Project Steps
1. Locate Button 1 and Button 2 in the Create® 3 button suite. In the code, trigger an event for Button 1 and 2 press with these commands:
```
@event(robot.when_touched, [True, False]
async def when_touch_fl(robot):
    pass

@event(robot.when_touched, [False, True]
async def when_touch_fr(robot):
    pass
```

2. Use the command await robot.play_note(440, 0.25) to play an A4 quarter note. The first parameter determines the note frequency and the second parameter determines note duration (in seconds). Explore playing different notes with our Python[^1] Note Frequencies Guide.

3. Under a Button 1 event, list at least three notes together in a sequence to create a “happy sound” melody. Our example snippet is below:
```
@event(robot.when_touched, [True, False])
async def when_touch_fl(robot):
    await robot.play_note(F4, .125)
    await robot.play_note(G4, .125)
    await robot.play_note(A4, .125)
```

4. Under a Button 2 event, list at least three notes together in a sequence to create an “angry sound.” When finished, you have the beginnings of a robot personality!

## Going Further
Take your robot’s personality to new heights by programming it to “grumble” and “shout” via angry melodies when it bumps into obstacles as it drives around the room.

OR

Transform your robot into a random guess machine! Create a program that will randomly play a happy or angry sound when a button is pressed. Use the robot to answer Yes or No questions randomly.

[^1]: Python is governed by the Python Software Foundation.
[^2]: All trademarks mentioned are the property of their respective owners.
