<!--
# SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-FileCopyrightText: Additions copyright (c) 2022 iRobot Corporation. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
-->

# Connect Create® 3 to NVIDIA® Jetson™ and set up ROS 2 Galactic

!!! important
    **This is community-submitted content. Please feel welcome to submit PRs for additions or corrections.**

## Before you start
!!! attention
    **These directions are written for someone with experience with embedded Linux and basic embedded computers.**
It is highly recommended to read through the getting started document for your NVIDIA® Jetson™ developer kit before beginning:

* [Getting Started With Jetson Xavier NX Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-xavier-nx-devkit)
* [Getting Started with Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)
* [Getting Started with Jetson Nano 2GB Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit)


## Step-by-step

### Getting Started Guide portion

1. Download the SD card image for your Jetson platform and write onto a microSD card.

2. Complete the getting started guide (listed above) until you complete the initial setup.

### Alter "USB Device Mode" to apply static IP

1. To alter the Jetson's "USB Device Mode" feature (specifically, disabling DHCP server and self-assign a static IP address);

    1. First, create a flag file to store IP address for Jetson to be used with Create3.

            sudo bash -c 'echo "192.168.186.3" > /opt/nvidia/l4t-usb-device-mode/IP_ADDRESS_FOR_CREATE3_ROBOT.conf'

    2. Then, modify the "nv-l4t-device-mode-runtime" service script (`/opt/nvidia/l4t-usb-device-mode/nv-l4t-usb-device-mode-runtime-start.sh`). The complete file is [here](data/nv-l4t-usb-device-mode-runtime-start.sh).
     <br>

2. Connect micro-B end of the USB cable from Create® 3 robot to the micro-B USB port of Jetson. Then check if the static IP address is set by issuing `ifconfig` command.

        $ ifconfig l4tbr0

        l4tbr0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                inet 192.168.186.3  netmask 255.255.255.0  broadcast 192.168.186.255
                inet6 fe80::1  prefixlen 128  scopeid 0x20<link>
                inet6 fe80::ecb6:edff:feac:7dd5  prefixlen 64  scopeid 0x20<link>
                ether ee:b6:ed:ac:7d:d5  txqueuelen 1000  (Ethernet)
                RX packets 169  bytes 36206 (36.2 KB)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 1644  bytes 213306 (213.3 KB)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    !!! warning
        Be sure that the [USB/BLE toggle on the robot's adapter board](../../hw/electrical/#adapter-board-overview) is set to the USB position.

    !!! note
        If you ever want to stop using the Jetson device for Create® 3 and re-enable the original USB Device Mode feature (so that you can connect to your Windows PC in headless style), you can simply remove the flag file, or execute the following.

        sudo mv /opt/nvidia/l4t-usb-device-mode/IP_ADDRESS_FOR_CREATE3_ROBOT.conf /opt/nvidia/l4t-usb-device-mode/IP_ADDRESS_FOR_CREATE3_ROBOT.conf.bak


### Start ROS 2 Galactic container

The recommended way to run ROS2 on Jetson is to use pre-built Docker container images.

1. Enable NVIDIA Container Runtime with Docker integration, if this is the first time running containers on Jetson, to allow access to GPU from containers.

    Edit `/etc/docker/daemon.json` to be the following.

        {
            "runtimes": {
                "nvidia": {
                    "path": "/usr/bin/nvidia-container-runtime",
                    "runtimeArgs": []
                }
            },
            "default-runtime": "nvidia"
        }


1. Use `jetson-containers`' script to simplify the invocation of `docker run` command.

        git clone https://github.com/dusty-nv/jetson-containers/
        cd jetson-containers
        scripts/docker_run.sh -c dustynv/ros:galactic-ros-base-l4t-r32.6.1

1. Install additional ROS 2 packages

        sudo apt update && sudo apt install -y ros-galactic-ros-base python3-colcon-common-extensions python3-rosdep ros-galactic-rmw-fastrtps-cpp ros-galactic-rmw-cyclonedds-cpp ros-galactic-irobot-create-msgs

1. Set the default network interface by setting Cyclone DDS configuration.

        export CYCLONEDDS_URI='<CycloneDDS><Domain><General><Interfaces><NetworkInterface name="l4tbr0"></Interfaces></General></Domain></CycloneDDS>'
    !!! attention
        **If you are using CycloneDDS (Galactic default) and want the Jetson to talk to the robot over USB and a laptop via Wi-Fi, you will need to take extra steps to setup CycloneDDS to use multiple interfaces.**
        **You will need to create a CycloneDDS XML configuration file with both USB and Wi-Fi interfaces and then set the CYCLONEDDS_URI environment variable to its path.**
        **See [CycloneDDS Multiple Network Interfaces](../xml-config/#cyclonedds).**
        **Note the differences in Jetson USB and Wi-Fi interface names from the documentation.**

1. Check to ensure Create® 3 topics appear

        ros2 topic list

    You should get

        /battery_state
        /cmd_audio
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
        /wheel_status
        /wheel_ticks
        /wheel_vels

    Check if it read a message on a topic

        ros2 topic echo odom

    You should see continuous repetition of output like following.

        ---
        header:
        stamp:
            sec: 1639388519
            nanosec: 209038110
        frame_id: odom
        child_frame_id: base_link
        pose:
        pose:
            position:
            x: -0.04380033165216446
            y: -0.005811699666082859
            z: 0.0
            orientation:
            x: 0.0037933308631181717
            y: 0.0016814800910651684
            z: 0.03521127253770828
            w: 0.999371349811554
        covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        twist:
        twist:
            linear:
            x: 0.0
            y: 4.972387477511303e-07
            z: -5.194771269447518e-09
            angular:
            x: -0.0006566781590969611
            y: -0.0019107190640370627
            z: 0.0
        covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

