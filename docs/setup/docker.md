# Create® 3 Desktop Docker Image

We provide a Docker image suitable for developing and running Create® 3 applications on your Desktop.
The docker image is named `irobotedu/create3-galactic` and its source code can be found [here](https://github.com/iRobotEducation/create3-docker).

!!! note
    The Docker image can be run on any base OS. However, non Linux-based OS will require custom networking configuration in order to communicate between a Docker container and a remote ROS 2 application. 

## Description of the Image

The Create® 3 Docker image is based off the official ROS 2 Docker images and runs an Ubuntu OS.
It contains all the core ROS 2 packages contained in the "desktop" variant (i.e. it includes development tools, core libries and visualization tools).

The Create® 3 Docker image includes pre-built all the open-source Create® 3 repositories such as: the Create® 3 ROS 2 message interfaces, the Create® 3 simulator (both Gazebo classic and Gazebo ignition) and the Create® 3 examples.

## Installing Docker

Follow the [official instructions](https://docs.docker.com/get-docker/) to setup Docker on your machine.

## Starting a Docker container

The following instructions may vary depending on your base OS and Docker installation mechanism.

### Linux

The following instructions assume that you have followed the [Docker post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/).

```sh
docker run -it --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-galactic bash
```

The `--network=host` option is required in order to allow the Docker container to communicate using ROS 2 with remote applications (e.g. your Create® 3 robot or compute-board).

The `--privileged -e DISPLAY=$DISPLAY` options are required in order to let the Docker container to access your xhost server and use GUI application (e.g. `rviz` or `gazebo`).

After you started the docker container, if you want to use GUI application, one (or more) extra steps are necessary.
A simple way is to run the following in a new terminal:
```sh
xhost +local:docker:CONTAINER_ID
```
Where `CONTAINER_ID` can be found either running `head -1 /proc/self/cgroup | cut -d / -f 3` inside the Docker container or by running `docker ps` in a new terminal.

You can find other ways to enable GUI in docker [here](http://wiki.ros.org/docker/Tutorials/GUI).
As an alternative, you can use the [rocker tool](https://github.com/osrf/rocker) to wrap the `irobotedu/create3-galactic` image and add capabilities to it.
