# ROS 2 Network Configuration

ROS 2[^1] is built on top of DDS/RTPS as its middleware, which provides advanced networking features such as: discovery, serialization and transportation.  This **R**OS 2 **m**iddle**w**are is abbreviated **RMW** for short.

This page contains some examples that may be useful when interacting with the iRobot® Create® 3.

!!! important
    Depending on the ROS 2 RMW used, the syntax for configuring the network will be different. We recommend to visit the RMW vendor documentation for more details.

You can choose a RMW implementation on your machine using

```sh
export RMW_IMPLEMENTATION=name-of-the-rmw
```
Currently, the only supported RMW implementations are: `rmw_cyclonedds_cpp` and `rmw_fastrtps_cpp`.  See [here](https://docs.ros.org/en/rolling/Concepts/About-Different-Middleware-Vendors.html) for more info on the different RMW vendors.

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

## CycloneDDS

CycloneDDS allows to specify DDS configuration through an XML file.
In order to apply a configuration, the path to the XML file must be provided through the following environment variable:

```sh
export CYCLONEDDS_URI=/path/to/the/xml/profile
```

Detailed network configurations are described in the [CycloneDDS documentation](https://cyclonedds.io/docs/cyclonedds/latest/config/cyclonedds_specifics.html#network-and-discovery-configuration).

#### Multiple Network Interfaces

This feature requires CycloneDDS version 0.8.0 or higher.
Use the following XML profile specifying the name of all the network interfaces you want to use.
For example `usb0` and `wlan0` in this example.

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
    **If the robot is running with a Compute Board like a [Raspberry Pi®](../pi4) or an [NVIDIA® Jetson™](../jetson) connected via USB, then the robot is using a multiple interface CycloneDDS config file to communicate both over usb0 and wlan0.**
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
