# Network Recommendations
This page details the recommendations for network settings to communicate with the Create® 3 via a Wi-Fi network. 

## Virtual Machines
As noted in the ROS 2 [Galactic](https://iroboteducation.github.io/create3_docs/setup/ubuntu2004/) and [Humble](https://iroboteducation.github.io/create3_docs/setup/ubuntu2204/) installation instructions, it is possible to install Ubuntu 20.04 or 22.04 in a virtualized container if your machine is natively running another operating system. There are three possible ways to communicate over Wi-Fi between ROS 2 on a virtual machine and the Create® 3 robot. 

### Option 1 (Recommended) Bridged Network Connection
While many virtualization applications default to a "shared" or "NAT" network connection, this type of connection will not allow ROS 2 to communicate with the Create® 3. 
