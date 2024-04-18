# C3, Phone Home
## Details
Use a coordinate system to command your robot to return to its starting position.
### Downloads and Resources
* [PDF: C3, Phone Home Activity Sheet](./Create3-C3_Phone_Home.pdf)

## The Main Idea
The Create® 3 robot keeps track of its position on an invisible coordinate grid as it moves around. This feature can be particularly handy when you’d like to tell your robot to drive to a specific set of coordinates, landmark, etc. Here we will use the invisible coordinate system to tell your robot to return to its starting position after roaming around a room.

## Project Steps
1. Remove your robot from the Home Base™ Charging Dock and place it on an empty space on the floor. This starting position will be registered as (0, 0) by the robot when you press “Play” on your program.

2. Create a program that drives the robot forward until it bumps into an obstacle. With a bump event, back up a few centimeters and then use await robot.navigate_to(0 , 0) to send your robot back to its original starting point. See the example below for help:
```
@event(robot.when_play)
async def play(robot):
    await robot.set_wheel_speeds(25, 25)

@event(robot.when_bumped, [True, True])
async def when_bumper(robot):
    await robot.move(-15)
    await robot.navigate_to(0, 0)

robot.play()
```
3. Press play to watch your robot drive forward until it bumps into an obstacle. Once it bumps, it should reverse, turn around and drive back to its original starting position.

## Going Further
Can you use the command await robot.get_position() to program your robot to list the coordinates of the obstacles it bumps into? How might you turn that list into a basic map?

Try combining the navigate_to() commands with the Create® 3 Light Painting Activity to create precise drawings from a coordinate grid.

Try measuring out your robot’s arena in centimeters and placing stickers or other flat landmarks down on specific coordinates. Program your robot to drive to each of the coordinates. How similar are you measurements?