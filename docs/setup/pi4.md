# Connect Create® 3 to Raspberry Pi® 4 and set up ROS 2 Galactic

## Before you start
!!! attention
    **These directions are written for someone with experience with embedded Linux and basic embedded computers.**
It is highly recommended to read through the following documents before beginning:

* [How to install Ubuntu Server on your Raspberry Pi](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi) - official Canonical documentation
* [Installing ROS 2 on Ubuntu Linux](https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Binary.html) - official Open Robotics documentation

## Step-by-step

1. Download [Ubuntu® Server 20.04 64-bit](https://ubuntu.com/download/raspberry-pi) and write onto a microSD card.
1. In the system-boot partition, edit usercfg.txt and add `dtoverlay=dwc2,dr_mode=peripheral`. For convenience, [here's a copy of this file](data/usercfg.txt).
1. In the system-boot partition, edit cmdline.txt to add `modules-load=dwc2,g_ether` after `rootwait`. For convenience, [here's a copy of this file](data/cmdline.txt).
1. In the system-boot partition, edit network-config to optionally add information about your Wi-Fi connection, and also add the following under `ethernets`

                usb0:
                    dhcp4: false
                    optional: true
                    addresses: [192.168.186.3/24]

    For convenience, [here's a copy of this file](data/network-config.txt). Be sure to remove the `.txt` extension.
    Note that the robot uses the default IP address of 192.168.186.2 on its usb0 interface.
    Please note also that after initial boot, editing `network-config` in the boot partition will not do anything; instead, the file to edit can be found at `/etc/netplan/50-cloud-init.yaml`.

1. If you would like your Raspberry Pi® 4 to communicate with the Create® 3 over its USB-C® port (and not just to power it), be sure that the [USB/BLE toggle on the robot's adapter board](../../hw/electrical/#adapter-board-overview) is set to the USB position.
1. Insert the microSD card into the Raspberry Pi® 4, and then use a USB-C® to USB-C® cable to connect the Raspberry Pi® 4 to the Create® 3.
A photo of this connection can be found [here](../../hw/hookup/#raspberry-pi-4).
The first boot may take a few minutes. (It may help to have a monitor and keyboard set up in case of any trouble on the first boot.)

1. Log in with the default username and password (ubuntu/ubuntu), change your password, and then change your locale to be one that uses UTF-8. For example, in the US, type

        sudo apt update
        sudo apt install locales
        sudo locale-gen en_US en_US.UTF-8
        sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
        export LANG=en_US.UTF-8

1. Then, execute the following commands:

        sudo apt update && sudo apt install -y curl gnupg2 lsb-release build-essential git cmake
        sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
        sudo apt update
        sudo apt install -y ros-galactic-ros-base python3-colcon-common-extensions python3-rosdep

        echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
        echo "export _colcon_cd_root=/opt/ros/galactic/" >> ~/.bashrc
        echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
        echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc

        source ~/.bashrc
        mkdir -p ~/ros2_ws/src
        cd ~/ros2_ws/src
        git clone https://github.com/iRobotEducation/irobot_create_msgs.git
        cd ..
        sudo rosdep init
        rosdep update
        rosdep install -i --from-path src --rosdistro galactic -y
        colcon build
        echo "source /home/ubuntu/ros2_ws/install/setup.bash" >> ~/.bashrc

1. Log out and log back in. Once you do, test things out with a `ros2 topic list`.
A full Create® 3 API description can be found [here](../../api/ros2).

<sub><sup>Ubuntu is a registered trademark of Canonical Ltd. USB-C® is a trademark of USB Implementers Forum. Raspberry Pi is a trademark of Raspberry Pi Trading. All other trademarks mentioned are the property of their respective owners.</sup></sub>
