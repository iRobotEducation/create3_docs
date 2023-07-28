# Setup NTP on compute board to serve time to Create® 3

## Why should I do this?

ROS 2[^1] is dependent upon synchronized clocks between nodes to have all data in the same reference time.
When the Create® 3 is publishing on topics, it is publishing its data with the timestamp of its system clock, which synchronizes with an NTP server.
If the Create® 3's Wi-Fi is connected to a network with internet connection, it will sync to a global time NTP server.
The Create® 3 NTP config is also set to listen for servers on USB IP address 192.168.186.1 and 192.168.186.3.
If the compute board is connected over USB to the Create® 3 with the compute board assigned one of these IP addresses on its USB interface, NTP on the compute board can keep the clocks between the compute board and Create® 3 in sync, even without an internet connection.
If there is an internet connection on both compute board and Create® 3, configuring the NTP server on the compute board to serve the Create® 3 can still add value by reducing jitter between clocks.
If your Create® 3 and compute board have an internet connection, this is not required, but is still recommended.

## Step-by-step

1. On your Compute Board, install chrony NTP server package

        sudo apt install chrony

1. Edit the config file

        sudo vi /etc/chrony/chrony.conf

1. Add the following lines after the `pool #.ubuntu.pool.ntp.org iburst maxsources #` block

        # Enable serving time to ntp clients on 192.168.186.0 subnet.
        allow 192.168.186.0/24

1. Optionally add the following lines immediately afterward if your SBC will not have a connection to a reference clock (i.e., the Internet)

        # Serve time even if not synchronized to a time source
        local stratum 10

1. Restart chrony

        sudo service chrony restart

1. Log into the Create® 3 web application and modify the NTP sources (as of Jul 2023 under "Beta Features") to add the following if it does not exist: 

        server 192.168.186.3 iburst

1. Through the Create® 3 web application, restart the NTPD server (or reboot the robot) if you made changes in the previous step.

1. Verify compute NTP server is talking to the Create® 3

        sudo chronyc clients

1. Confirm 192.168.182.2 shows non 0 number in NTP column

        Hostname                      NTP   Drop Int IntL Last     Cmd   Drop Int  Last
        ===============================================================================
        192.168.186.2                  51      0   5   -    32       0      0   -     -

1. Note that if there is a large jump in the time, the Create® 3 may not accept it until its next reboot.
    This can be verified by checking the Create® 3 robot's log for a line like

        user.notice ntpd: ntpd: reply from 192.168.186.3: delay ### is too high, ignoring
    If this happens, simply restart the robot (not just the application) via the webserver over the network connection.

[^1]: ROS 2 is governed by Open Robotics
