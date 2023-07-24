# Connect Create® 3 to Raspberry Pi® 4 and set up ROS 2 Humble

!!! note
    As of March 2023, use of Galactic is recommended, as it is more performant than Humble on Create 3.

## Before you start
!!! attention
    **These directions are written for someone with experience with embedded Linux and basic embedded computers.**
It is highly recommended to read through the following documents before beginning:

* [How to install Ubuntu Server on your Raspberry Pi](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi)[^1] - official Canonical documentation
* [Installing ROS 2 on Ubuntu Linux](https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html)[^1] - official Open Robotics documentation

## Step-by-step

1. Download and install the appropriate version of the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your computer.

1. Open the imager and under operating system, select "Other general-purpose OS" then "Ubuntu" and finally, "Ubuntu Server 22.04 LTS (64-bit)".

1. Insert your microSD card into your computer and under storage in the Raspberry Pi Imager, select your microSD card.

1. Select the gear icon to optionally customize advanced options including enabling SSH, setting a unique username and password, and configuring a wireless LAN.
It is recommended to uncheck the "Eject media when finished" box in advanced options so you can edit the necessary files in the following steps without re-inserting the SD card.

1. Once all options have been selected, click the "WRITE" button to write the image to your SD card.

1. In the system-boot partition, edit config.txt and add `dtoverlay=dwc2,dr_mode=peripheral` at the end of the file.

1. In the system-boot partition, edit cmdline.txt to add `modules-load=dwc2,g_ether` after `rootwait`.

1. In the system-boot partition, edit the `network-config` executable to optionally add information about your Wi-Fi connection, and also add the following under `ethernets`

                usb0:
                    dhcp4: false
                    optional: true
                    addresses: [192.168.186.3/24]

    For convenience, [here's a copy of this file](data/network-config.txt). Be sure to remove the `.txt` extension.
    Note that the robot uses the default IP address of 192.168.186.2 on its usb0 interface.
    Please note also that after initial boot, editing `network-config` in the boot partition will not do anything; instead, you will need to edit `/etc/netplan/50-cloud-init.yaml`.
    After editing that file, you will need to run `sudo netplan generate` followed by `sudo netplan apply` to update your network configuration.

1. If you would like your Raspberry Pi® 4[^3] to communicate with the Create® 3 over its USB-C®[^2] port (and not just to power it), be sure that the [USB/BLE toggle on the robot's adapter board](../../hw/electrical/#adapter-board-overview) is set to the USB position.

1. Insert the microSD card into the Raspberry Pi® 4[^3], and then use a USB-C®[^2] to USB-C®[^2] cable to connect the Raspberry Pi® 4[^3] to the Create® 3.
A photo of this connection can be found [here](../../hw/hookup/#raspberry-pi-4).
The first boot may take a few minutes. (It may help to have a monitor and keyboard set up in case of any trouble on the first boot.)

    !!! attention
        If you are new to ROS 2 and would like to utilize the turtlesim tutorials, it necessary to install a desktop environment to do this.
        We have had success with xubuntu which can be installed with the following command: `sudo apt install xubuntu-desktop`.
        Please see the [Ubuntu docs](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#5-install-a-desktop) for more details.


1. Log in with the default username and password (ubuntu/ubuntu), change your password, and then change your locale to be one that uses UTF-8. For example, in the US, type

        sudo apt update
        sudo apt install locales
        sudo locale-gen en_US en_US.UTF-8
        sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
        export LANG=en_US.UTF-8

1. Recommended: follow the procedure to [Setup NTP on this compute board](compute-ntp.md) so the Create 3 can sync its clock.
2. Optional: Run `timedatectl` and see if `System clock synchronized: ` says `yes`. If not, you may want setup NTP on your raspi so the clock stays accurate. To do so, specify some NTP servers for time syncronization. Edit `/etc/systemd/timesyncd.conf` (`sudo nano /etc/systemd/timesyncd.conf`) to have the below contents, then run `systemctl restart systemd-timesyncd.service` to load the new NTP server configuration.

        [Time]
        NTP=ntp.ubuntu.com
        FallbackNTP=0.us.pool.ntp.org 1.us.pool.ntp.org

1. Then, execute the following blocks of commands to install ROS 2[^4]:

        sudo apt update && sudo apt install -y curl gnupg2 lsb-release build-essential git cmake
   then

        sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
        sudo apt update
   then

        sudo apt install -y ros-humble-desktop
        sudo apt install -y ros-humble-irobot-create-msgs
        sudo apt install -y build-essential python3-colcon-common-extensions python3-rosdep ros-humble-rmw-cyclonedds-cpp
   finally

        echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

1. At this point, we recommend setting your default RMW. The RMW you set here has to match the RMW on your robot, which can be found from its Application Configuration page. More detail on RMW can be found [here](../xml-config). Depending on your robot's RMW implementation, type one of the following:

        echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
   or

        echo "export RMW_IMPLEMENTATION=rmw_fastrtps_cpp" >> ~/.bashrc

1. Log out and log back in. Once you do, test things out with a `ros2 topic list`.
A full Create® 3 API description can be found [here](../../api/ros2).

    !!! attention
        **If you are using CycloneDDS, your Raspberry Pi® may be running with multiple network interfaces (usb0 to talk to robot and wlan0 to talk to laptop).**
        **You will need to export a path on the Raspberry Pi® to an xml config file that registers those interfaces in the CYCLONEDDS_URI.**
        **See [CycloneDDS Multiple Network Interfaces](../xml-config/#cyclonedds).**

[^1]: Ubuntu is a registered trademark of Canonical Ltd.
[^2]: USB-C® is a trademark of USB Implementers Forum.
[^3]: Raspberry Pi® is a trademark of Raspberry Pi Trading. All other trademarks mentioned are the property of their respective owners.
[^4]: ROS 2 is governed by Open Robotics
