# Using multiple Create® 3 robots

This page describes how to manage multiple Create® 3 robots connected to the same Wi-Fi network.
Note that if you have multiple robots, but they are not on the same network, then you can ignore this as they are effectively isolated.

!!! attention
    **If you have multiple Create® 3 robots connected to the same Wi-Fi network it is required to adopt at least one of the following procedures, otherwise they will not work.**

## Basic Concepts on ROS 2 Communication

ROS 2 communication is based on the underlying DDS middleware.
After two ROS processes discover each others, they will automatically start to communicate if their topics, services or actions match.

The default discovery protocol used by ROS 2 is based on broadcast.
This means that when a ROS 2 process is started it will advertise its own discovery messages to all other ROS processes that are connected to the same network.

The main advantage of using a broadcast discovery protocol is that as long as your ROS 2 processes are connected to the same network, they will automatically connect to each others and start to communicate.
The basic use-case does not require any special configuration from the users.

### Potential Problems with multiple robots 

Having ROS 2 process to automatically start to communicate is not always a good thing.
Usually if two ROS 2 processes that are meant to be executed in isolation will start to communicate, they will end up mixing up their own messages, without being able to understand if what they are receiving was meant for them or for the other robot.

!!! important 
    **Create® 3 robots should never communicate between each others.**

There may be cases where two ROS 2 processes had no intentions to communicate and they just happened to be under the same Wi-Fi.
On the other hand, users with multiple robots running at the same time may want to be able to select to which robot to communicate from their laptop, while still preventing them to communicate between each others.

The following sections will describe how to mitigate and solve these problems.
Different solutions are presented, as each of them may be more suitable to a different scenario.

## ROS 2 Namespaces

The easiest way to prevent multiple ROS 2 processes from communicating with each others is to use ROS 2 namespaces.
As you know, each ROS 2 entity is uniquely identified by its name (for example the topic named `cmd_vel` is used to control the robot).
By specifying a namespace for a ROS 2 process you are effectively pre-pending a word in front of the name of all the entities created by it.

The ROS 2 namespace can be set from the Application &rarr; Configuration menu in the Create® 3 robot's web server.
Note that the namespace name must start with a slash `/`.

If you have two robots and you specify the following namespaces: `/robot_1` and `/robot_2` you will then be able to see their individual topics well separated:

```sh
$ ros2 topic list
/robot_1/cmd_vel
/robot_1/dock
/robot_1/odom
...
/robot_2/cmd_vel
/robot_2/dock
/robot_2/odom
...
```

Note that if you want to publish or subscribe to a specific topic, now you have to prepend the appropriate namespace in front of it.
For example:

```sh
$ ros2 topic echo /robot_1/odom
```

Using a custom ROS 2 namespace for your robots is the recommended solution if you don't have too many robots or if you have an additional application that needs to communicate with all of them at the same time.

## ROS 2 Domain IDs

A different approach for isolating multiple ROS 2 processes consists in specifying the `ROS_DOMAIN_ID` environment variable.

If two processes use a different `ROS_DOMAIN_ID` value they will be completely isolated from each others, which means that they will not only avoid to communicate, but they also will not discover each others. 
You can read more details about this variable in the [ROS 2 official documentation](https://docs.ros.org/en/galactic/Concepts/About-Domain-ID.html).

The ROS 2 domain ID can be set from the Application &rarr; Configuration menu in the Create® 3 robot's web server.
Note that the domain ID must be a value between 0 and 101.
By default, ROS 2 processes use a `ROS_DOMAIN_ID` value of 0.

If you want to communicate with a specific robot from your laptop, it is required to set also here the corresponding value for the domain ID.
For example:

```sh
$ export ROS_DOMAIN_ID=42
$ ros2 topic list
/cmd_vel
/dock
/odom
...
```

Note that a ROS 2 process can only use one domain ID at the same time.
If needed you can always have multiple robots under the same domain ID and then also add namespaces to prevent them from communicating.

Using a custom ROS 2 domain ID for your robots is the recommended solution when you have a large number of robots and you want your tools to communicate only with a subset of them.
