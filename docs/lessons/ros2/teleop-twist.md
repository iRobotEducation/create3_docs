# Teleop Twist with the Create® 3 Robot
## Details
In this project, you'll build the Create 3 Examples repository from GitHub and drive the Create® 3 Robot around with your computer's keyboard.

### Downloads and Resources
* [Create 3 Examples GitHub](https://github.com/iRobotEducation/create3_examples)
* [Tutorial Video](https://bcove.video/3BOpW9D)

## Build the Create® 3 Examples Repository
Example nodes to drive the iRobot® Create® 3 Educational Robot.

### Dependencies
* [ROS 2 Galactic](https://docs.ros.org/en/galactic/Installation.html)
* [irobot_create_msgs](https://github.com/iRobotEducation/irobot_create_msgs)

### Build instructions
First, source your ROS 2 workspaces with all the required dependencies. Then, you are ready to clone and build this repository. You should only have to do this once per install.

```
mkdir -p create3_examples_ws/src
cd create3_examples_ws/src
git clone https://github.com/iRobotEducation/create3_examples.git
cd ..
rosdep install --from-path src --ignore-src -yi
colcon build
```

### Initialization instructions
You will have to do this in every new session in which you wish to use these examples:
```
source ~/create3_examples_ws/install/local_setup.sh
```

## Teleoperation & Teleprescence Project Instructions
In this example, you will learn to control a Create®3 robot with the keyboard on your laptop. Being able to control the robot from a distance makes it teleoperational. To make it have telepresence, design a phone stand that can attach to the top of the Create®3 robot. Facetime or Zoom into your phone so you can see the environment where you are driving the robot. This allows you to feel present as your robot navigates around.

![A Create 3 robot driving around a classroom from a student perspective](./teleop-1.gif)
![A Create 3 robot driving around a classroom from the robot's perspective](./teleop-2.gif)

## Get Started
Make sure to follow the instructions above in the "Build the Create 3 Examples Repository" section to install the necessary package and dependencies for this example.

### Install Dependencies
First, let's install the ROS Teleop Twist package. Copy & paste this line into the open terminal:
```
sudo apt install ros-galactic-teleop-twist-keyboard
```

### Disabling Motion Control Safety

Next, we need to disable the motion control safety features of the Create®3 robot. This will allow you to drive the robot in reverse.
```
ros2 param set /motion_control safety_override full
```
Then we can run the teleop_twist_keyboard package that we previously installed.
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
### What You'll See
When you run this package & executable you will see the following information in your terminal. Now you can use the keys on your keyboard to remotely control your Create®3 robot. Happy Driving!

```
Reading from the keyboard and Publishing to Twist!
---------------------------
Moving around:
 u i o
 j k l
 m , .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
 U I O
 J K L
 M < >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
```