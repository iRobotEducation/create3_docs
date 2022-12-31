# Network Recommendations
This page details the recommendations for network settings to communicate with the Create® 3 via a network. 

## Virtual Machines
As noted in the ROS 2 [Galactic](https://iroboteducation.github.io/create3_docs/setup/ubuntu2004/) and [Humble](https://iroboteducation.github.io/create3_docs/setup/ubuntu2204/) installation instructions, it is possible to install Ubuntu 20.04 or 22.04 in a virtualized container if your machine is natively running another operating system. There are three possible ways to communicate over a network between a virtual machine and the Create® 3 robot using ROS 2. 

!!! important
    Any time you change your network configuration settings on your virtual machine, you should restart the virtual machine before attempting to confirm connectivity.

### Option 1 (Recommended) Bridged Network Connection
While many virtualization applications default to a "shared" or "NAT" network connection, this type of connection will **not** allow ROS 2 to communicate with the Create® 3. Instead, a bridged network connection should be used for the virtual machine. This does require that your Wi-Fi network allows for bridged connections. Many corporate, school and university networks prevent bridging and it is recommended you speak with your network administrator to confirm whether bridging is enabled on these networks. 

!!! attention
    **If you have confirmed your network allows bridged connections, but you are unable to pull a topic list, you may need to disable multicasting. Instructions on how to disable multicasting can be found on the [RMW Configuration](https://iroboteducation.github.io/create3_docs/setup/xml-config/) page.**

### Option 2 Bridged Network Connnection with MAC Address Mirroring
In the event option 1 did not work on your network, it may still be possible to communicate between your virtual machine and your Create® 3 on the same network attempted in option 1. Typically, a bridged network connection asks your network to assign a new IP address to your virtual machine, which has its own unique MAC address. Security and authentication settings on some networks may reject this request. A possible work around is to assign your virtual machine the same MAC address as your native machine's network adapter. 

