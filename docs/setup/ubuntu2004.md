# Install ROS 2 Galactic with Create 3 Messages on an Ubuntu 20.04 Machine

## Before you start
If you are running Ubuntu 20.04 natively on your machine, there is no extra setup required.
These directions should work in a virtualized container within another operating system, as well.

## Step-by-step

1. If you haven't already, download and install [Ubuntu® Server 20.04 64-bit](https://releases.ubuntu.com/20.04/ubuntu-20.04.4-live-server-amd64.iso)[^1].

1. Once logged in, check to ensure that you are using a UTF-8 locale by typing
        echo $LANG

1. Execute the following commands to install ROS 2[^2]:

        sudo apt update && sudo apt install -y curl gnupg2 lsb-release build-essential git cmake
        sudo curl -ksSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
        sudo apt update
        sudo apt install -y ros-galactic-ros-base python3-colcon-common-extensions python3-rosdep ros-galactic-rmw-fastrtps-cpp ros-galactic-rmw-cyclonedds-cpp ros-galactic-irobot-create-msgs

        echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
        echo "export _colcon_cd_root=/opt/ros/galactic/" >> ~/.bashrc
        echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
        echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc

        source ~/.bashrc

1. At this point, we recommend setting your default RMW. The RMW you set here has to match the RMW on your robot, which can be found from its Application Configuration page. More detail on RMW can be found [here](../xml-config). Right now, the Create® 3 robot supports `rmw_cyclonedds_cpp` and `rmw_fastrtps_cpp`. The default for Galactic is `rmw_cyclonedds_cpp`. Depending on your robot's RMW implementation, type one of the following:

        echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
or

        echo "export RMW_IMPLEMENTATION=rmw_fastrtps_cpp" >> ~/.bashrc

1. You should now be able to test things out with a `ros2 topic list`.
A full Create® 3 API description can be found [here](../../api/ros2).

    !!! attention
        **If you are using CycloneDDS (Galactic default), your Raspberry Pi® may be running with multiple network interfaces (usb0 to talk to robot and wlan0 to talk to laptop).**
        **You will need to export a path on the Raspberry Pi® to an xml config file that registers those interfaces in the CYCLONEDDS_URI.**
        **See [CycloneDDS Multiple Network Interfaces](../xml-config/#cyclonedds).**

[^1]: Ubuntu is a registered trademark of Canonical Ltd.
[^2]: ROS 2 is governed by Open Robotics
