# Connect Create® 3 to Raspberry Pi® 4 and set up ROS 2 Galactic

1. Download [Ubuntu® Server 20.04 64-bit](https://ubuntu.com/download/raspberry-pi) and write onto a microSD card.
1. In the system-boot partition, edit usercfg.txt and add `dtoverlay=dwc2,dr_mode=peripheral`
1. In the system-boot partition, edit cmdline.txt to add `modules-load=dwc2,g_ether` after `rootwait`
1. In the system-boot partition, edit network-config to optionally add information about your Wi-Fi connection, and also add the following under `ethernets`

                usb0:
                    dhcp4: false
                    optional: true
                    addresses: [192.168.186.3/24]

    Note that the robot uses the default IP address of 192.168.186.2 on its usb0 interface.

1. Insert the microSD card into the Raspberry Pi® 4, and then use a USB-C® to USB-C® cable to connect the Raspberry Pi® 4 to the Create® 3. The first boot may take a few minutes. (It may help to have a monitor and keyboard set up in case of any trouble on the first boot.)
1. Log in with the default username and password (ubuntu/ubuntu), change your password, and then change your locale to be one that uses UTF-8. For example, in the US, type

        sudo locale-gen en_US en_US.UTF-8
        sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
        export LANG=en_US.UTF-8

1. Then, execute the following commands:

        sudo apt update && sudo apt install curl gnupg2 lsb-release build-essential
        sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
        sudo apt update
        sudo apt install ros-galactic-ros-base python3-colcon-common-extensions python3-rosdep2

        echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
        echo "export _colcon_cd_root=/opt/ros/galactic/" >> ~/.bashrc
        echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
        echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc

        source ~/.bashrc
        mkdir -p ~/ros2_ws/src
        cd ~/ros2_ws/src
        git clone https://github.com/iRobotEducation/irobot_create_msgs.git
        cd ..
        rosdep update
        rosdep install -i --from-path src --rosdistro galactic -y
        colcon build
        echo "source /home/ubuntu/ros2_ws/install/setup.bash" >> ~/.bashrc

1. Log out and log back in. Once you do, test things out with a `ros2 topic list`

<sub><sup>Ubuntu is a registered trademark of Canonical Ltd. USB-C® is a trademark of USB Implementers Forum. Raspberry Pi is a trademark of Raspberry Pi Trading. All other trademarks mentioned are the property of their respective owners.</sup></sub>