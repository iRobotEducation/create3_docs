# ROS 2 Middleware (RMW) Configuration

ROS 2[^1] is built on top of DDS/RTPS as its middleware, which provides advanced networking features such as: discovery, serialization and transportation.  This **R**OS 2 **m**iddle**w**are is abbreviated **RMW** for short.

The middleware running on the robot can be selected using the [Application Configuration](../webserver/application.md) page on the webserver. Note that the choice of middleware available may be restricted by the firmware installed on your robot; check the [releases](https://github.com/iRobotEducation/create3_docs/releases) for more details on available firmware.

This page contains some examples that may be useful when interacting with the iRobot® Create® 3.

!!! important
    Depending on the ROS 2 RMW used, the syntax for configuring the network will be different.
    We recommend to visit the RMW vendor documentation for more details.

You can choose a RMW implementation on your machine using

```sh
export RMW_IMPLEMENTATION=name-of-the-RMW
```
Currently, the only supported RMW implementations are: `rmw_cyclonedds_cpp` and `rmw_fastrtps_cpp`.  See [here](https://docs.ros.org/en/rolling/Concepts/About-Different-Middleware-Vendors.html) for more info on the different RMW vendors.

If you are using a bash shell (default on Ubuntu), you can set a default RMW adding the above line to your `.bashrc` file.
You may have already set a default RMW in this file if you followed our [ROS 2 Galactic](https://iroboteducation.github.io/create3_docs/setup/ubuntu2004/) or [ROS 2 Humble](https://iroboteducation.github.io/create3_docs/setup/ubuntu2204/) installation instructions; in that case, you can change the name of the RMW by editing your `.bashrc` file using your preferred text editor.
Nano is an option for a text editor that is standard on most Ubuntu installations. You can also install it using

```sh
sudo apt-get update && sudo apt-get install nano
```
Then the file can be opened and edited
```sh
nano ~/.bashrc
```

Then scroll to the bottom of the file and replace the current `name-of-the-rmw` with either `rmw_cyclonedds_cpp` and `rmw_fastrtps_cpp`. Once you've changed the RMW, press `Ctrl-X` to exit nano and save the file. Finally, either log out and log back in, or simply
```sh
source ~/.bashrc
```

On the robot the same can be controlled through the Create® 3 webserver.

!!! important
    Always make sure that all the ROS 2 processes you are using have selected the same RMW implementation.

## Fast-DDS

Fast-DDS allows to specify DDS configuration through an XML file.
In order to apply a configuration, the path to the XML file must be provided through the following environment variable:

```sh
export FASTRTPS_DEFAULT_PROFILES_FILE=/path/to/the/xml/profile
```

Detailed network configurations are described in the [Fast-DDS documentation](https://fast-dds.docs.eprosima.com/en/latest/).

#### Multiple Network Interfaces

Fast-DDS supports multiple network interfaces out of the box.
A ROS 2 process will automatically use all the interfaces that were available when it started (it will not use network interfaces activated while the process was already running).

#### Disable Multicast

Some networks (e.g., academic or corporate Wi-Fi) may block the multicast packets used by ROS 2 by default.
The following XML profile can be used on your laptop (or compute board) to force using unicast and directly connect to the IP address of your robot.

The file must be edited replacing `ROBOT_IP` with the actual IP value.
```
<?xml version="1.0" encoding="UTF-8" ?>
<profiles xmlns="http://www.eprosima.com/XMLSchemas/fastRTPS_Profiles">
   <participant profile_name="unicast_connection" is_default_profile="true">
       <rtps>
           <builtin>
               <metatrafficUnicastLocatorList>
                   <locator/>
               </metatrafficUnicastLocatorList>
               <initialPeersList>
                   <locator>
                       <udpv4>
                           <address>ROBOT_IP</address>
                       </udpv4>
                   </locator>
               </initialPeersList>
           </builtin>
       </rtps>
   </participant>
</profiles>
```

## Cyclone DDS

Cyclone DDS allows to specify DDS configuration through an XML file.
In order to apply a configuration, the path to the XML file must be provided through the following environment variable:

```sh
export CYCLONEDDS_URI=/path/to/the/xml/profile
```

Detailed network configurations are described in the [Cyclone DDS documentation](https://cyclonedds.io/docs/cyclonedds/latest/config/network-config.html).

#### Multiple Network Interfaces

This feature requires Cyclone DDS version 0.8.0 or higher.
Use the following XML profile specifying the name of all the network interfaces you want to use.
For example `usb0` and `wlan0` in this example.

##### Galactic and Humble
```
<CycloneDDS>
   <Domain>
     <General>
        <NetworkInterfaceAddress>usb0,wlan0</NetworkInterfaceAddress>
    </General>
   </Domain>
</CycloneDDS>
```

##### Humble and future releases
```
<CycloneDDS>
   <Domain>
     <General>
        <Interfaces>
          <NetworkInterface name="usb0" />
          <NetworkInterface name="wlan0" />
        </Interfaces>
    </General>
   </Domain>
</CycloneDDS>
```

Note that the specified network interfaces must be already active when the ROS 2 process is started.

!!! attention
    **If the robot is running with a Compute Board like a [Raspberry Pi®](../pi4) or an [NVIDIA® Jetson™](../jetson) connected via USB, then the robot is using a multiple interface Cyclone DDS config file to communicate both over usb0 and wlan0.**
    **We have found that with CycloneDDS version 0.8.1, for an Ubuntu laptop to see the robot topics with CycloneDDS when running multiple interfaces, the laptop must use the configuration option:**
```
<CycloneDDS>
   <Domain>
     <General>
        <DontRoute>true</DontRoute>
    </General>
   </Domain>
</CycloneDDS>
```
#### Disable Multicast

Some networks (e.g. corporate WiFi) may block the multicast packets used by ROS 2 by default.
The following XML profile can be used on your laptop (or compute board) to force using unicast and directly connect to the IP address of your robot.

The file must be edited replacing `${ROBOT_IP}` with the actual IP value, or exporting the value as an environment variable.

##### Galactic and Humble
```
<CycloneDDS>
  <Domain>
    <Id>any</Id>
    <General>
      <NetworkInterfaceAddress>auto</NetworkInterfaceAddress>
      <AllowMulticast>false</AllowMulticast>
      <EnableMulticastLoopback>true</EnableMulticastLoopback>
    </General>
    <Discovery>
      <ParticipantIndex>0</ParticipantIndex>
      <Peers>
        <Peer Address="${ROBOT_IP}:7410"/>
      </Peers>
    </Discovery>
  </Domain>
</CycloneDDS>
```

##### Humble and future releases
```
<CycloneDDS>
  <Domain>
    <Id>any</Id>
    <General>
      <Interfaces>
        <NetworkInterface autodetermine="true" />
      </Interfaces>
      <AllowMulticast>false</AllowMulticast>
      <EnableMulticastLoopback>true</EnableMulticastLoopback>
    </General>
    <Discovery>
      <ParticipantIndex>0</ParticipantIndex>
      <Peers>
        <Peer Address="${ROBOT_IP}:7410"/>
      </Peers>
    </Discovery>
  </Domain>
</CycloneDDS>
```

[^1]: ROS 2 is governed by Open Robotics
