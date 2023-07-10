# Network Recommendations
This page details the recommendations for network settings to communicate with the Create® 3 robot via a network. 


## Wi-Fi Networks
There are several Wi-Fi configurations that must be in place to properly communicate with the Create® 3 robot via a Wi-Fi network. 
Below are the currently supported configurations. 

### Supported Configurations
Authentication: open (no password required) or shared key (password only) 

Frequency: 2.4 GHz

### Troubleshooting
The ROS 2 node discovery process that is handled by the ROS 2 Middleware (RMW) can be network intensive, but there are several options to mitigate excess traffic and ensure your Create® 3 robot can operate on your Wi-Fi network. 

#### Disable Multicasting
Both supported RMWs (Fast and Cyclone) require multicasting to be enabled on your Wi-Fi network by default. 
However, multicasting is often disabled on enterprise networks, and the [creators of Fast DDS recommend disabling multicasting](https://fast-dds.docs.eprosima.com/en/latest/fastdds/use_cases/well_known_deployments/well_known_deployments.html) when operating on a Wi-Fi network.   

A complete overview of the multicast disabling process for both RMWs is outlined on the [ROS 2 Middleware Configuration](../xml-config) page. 

#### Dedicated Network
In cases where multiple robots will be using a busy network (e.g., university or corporate networks) or the existing network configuration is non-functional, creating a dedicated network for your Create® 3 robot can mitigate most issues.

#### Fast DDS Discovery Server
The Fast DDS Discovery Server further limits discovery traffic by routing discovery through a single server. 
This can avoid known issues with scaling and multicasting. 
Instructions on how to set up a discovery server are outlined [here.](../discovery-server)

## Ethernet Over USB
The Create® 3 robot has a USB-C® port that allows for ethernet network connectivity over USB.
To utilize this connection, switch the USB/BLE toggle on the robot to the USB position.
When you switch this toggle, the blue light on the adapter board will turn off, but the yellow and orange lights will remain on. 

![Ethernet Over USB Setup Steps 1-2](data/ethoverusb_step1-2.png "Ethernet Over USB Steps 1-2")

This setup requires a USB-C® to ethernet adapter connected to the Create® 3 robot and then connected to an ethernet cable. 
On the other end of the ethernet cable, connect another ethernet to USB adapter which can be connected directly to your computer. 

![Ethernet Over USB Setup Step 3](data/ethoverusb_step3.png "Ethernet Over USB Step 3")

!!! important
    If the yellow and orange lights on the adapter board turn off during this process, this means your adapter board has disconnected from the Create® 3 robot.
    The adapter board can easily be re-attached by sliding it back into the designated slot. 

On your computer, navigate to your wired connection and change you IPv4 method to `manual` and input an address of `192.168.186.3` and a netmask of `255.255.0.0`. 
![Ethernet Over USB Network Configuration](data/ethoverusb.png "Ethernet Over USB Configuration")

You can check to confirm the connection is functional by navigating to `192.168.186.2` in your web browser. If all is working properly, the [iRobot® Create® 3 Webserver](https://iroboteducation.github.io/create3_docs/webserver/overview/) will load. 

!!! important
    This connection type will mean that your Create® 3 robot is physically attached to your computer, which is not practical for many applications. 
    However, this can be a useful tool when troubleshooting. 

## Virtual Machines
As noted in the ROS 2 [Galactic](../ubuntu2004) and [Humble](../ubuntu2204) installation instructions, it is possible to install Ubuntu 20.04 or 22.04 in a virtualized container if your machine is natively running another operating system. 
There are three possible ways to communicate over a network between a `virtual machine (VM)` and the Create® 3 robot using ROS 2. 

!!! important
    Any time you change your network configuration settings on your virtual machine, you should restart the virtual machine before attempting to confirm connectivity.

### Option 1 (Recommended) Bridged Network Connection
While many virtualization applications default to a "shared" or "NAT" network connection, this type of connection will **not** allow ROS 2 to communicate with the Create® 3 robot. 
Instead, a bridged network connection should be used for the virtual machine. This does require that your Wi-Fi network allows for bridged connections. 
Many enterprise networks prevent bridging and it is recommended you speak with your network administrator to confirm whether bridging is enabled on these networks. 

!!! attention
    **If you have confirmed your network allows bridged connections, but you are unable to pull a topic list, you may need to disable multicasting. Instructions on how to disable multicasting can be found on the [RMW Configuration](../xml-config) page.**

### Option 2 USB Wi-Fi Network Adapter
If you are experiencing difficulty with a bridged network connection, a stable alternative is to provide your virtual machine with its own dedicated network adapter. 
This can be done by purchasing a USB Wi-Fi network adapter that is compatible with Ubuntu. 
Once you plug the USB Wi-Fi network adapter into your computer, assign the USB device to be used by the VM only and this should enable you to select and connect to a Wi-Fi network directly within your VM.

!!! important
    For reliable functionality, you must disconnect your bridged connection between your VM and your computer when using the USB Wi-Fi network adapter. 
    Failure to do so will result in intermittent connection difficulties as the VM attempts to connect to both networks. 

### Option 3 (Advanced) Bridged Network Connnection with MAC Address Mirroring
In the event Option 1 did not work on your network, it may still be possible to communicate between your virtual machine and your Create® 3 robot on the same network attempted in Option 1. 
Typically, a bridged network connection asks your network to assign a new IP address to your virtual machine, which has its own unique MAC address. 
Security and authentication settings on some networks may reject this request. 
A possible work around is to assign your virtual machine the same MAC address as your computer's network adapter. 
Within your virtualization application under network settings, there should be an advanced network settings option that allows you to modify the existing MAC address. 
Entering your computer's network adapter MAC address in this field will mirror the MAC address on your virtual machine. 

!!! attention
    **This work around will likely result in the loss of internet connection on your computer.**

### Option 4 (Advanced) Ethernet Over USB
Follow the instructions outlined in the Ethernet Over USB section above but assign the USB device to your virtual machine as instructed in Option 3. 

!!! important
    This connection type will mean that your Create® 3 robot is physically attached to your computer, which is not practical for many applications. 
    However, this can be a useful tool when troubleshooting. 


