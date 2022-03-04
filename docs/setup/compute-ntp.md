# Setup NTP on compute board to serve time to Create® 3

## Why should I do this?

ROS 2 is dependent upon synchronized clocks between nodes to have all data in the same reference time.
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

        server 192.168.186.2 presend 0 minpoll 0 maxpoll 0 iburst  prefer trust
        # Enable serving time to ntp clients on 192.168.186.0 subnet.
        allow 192.168.186.0/24

1. Restart chrony

        sudo service chrony restart

1. Verify compute NTP server is talking to Create® 3

        sudo chronyc clients

1. Confirm 192.168.182.2 shows non 0 number in NTP column

        Hostname                      NTP   Drop Int IntL Last     Cmd   Drop Int  Last
        ===============================================================================
        192.168.186.2                  51      0   5   -    32       0      0   -     -
        localhost                       0      0   -   -     -      31      0   7     4