Connect Create® 3 to NVIDIA Jetson Nano 2GB (and other variants)

## Before you start
!!! attention
    **These directions are written for someone with experience with embedded Linux and basic embedded computers.**
It is highly recommended to read through the following documents before beginning:

* [Getting Started with Jetson Nano 2GB Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit)

For other Jetson platform:

* [Getting Started with Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)
* [Getting Started With Jetson Xavier NX Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-xavier-nx-devkit)


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

2. Connect micro-B end of the USB cable from Create3 robot to the micro-B USB port of Jetson. Then check if the static IP address is set by issuing `ifconfig` command.

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


!!! note
    If you ever want to stop using the Jetson device for Create3 and re-enable the original USB Device Mode feature (so that you can connect to your Windows PC in headless style), you can simply remove the flag file, or execute the following.

        sudo mv /opt/nvidia/l4t-usb-device-mode/IP_ADDRESS_FOR_CREATE3_ROBOT.conf /opt/nvidia/l4t-usb-device-mode/IP_ADDRESS_FOR_CREATE3_ROBOT.conf.bak


### Start ROS2 Galactic container

The recommended way to run ROS2 on Jetson is to use a pre-built Docker containers.

1. Enable NVIDIA runtime for docker, if this is the first time running Docker containers on Jetson, to allow access to GPU from containers.

    Edit `/etc/docker/daemon.json` to be following.

        {
            "runtimes": {
                "nvidia": {
                    "path": "nvidia-container-runtime",
                    "runtimeArgs": []
                }
            },
            "default-runtime": "nvidia"
        }


2. Use `jetson-containers`' script to simplify the inovocation of `docker run` command.

```
git clone https://github.com/dusty-nv/jetson-containers/
cd jetson-containers
scripts/docker_run.sh -c dustynv/ros:galactic-ros-base-l4t-r32.6.1
```

