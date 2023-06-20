# Fast DDS Discovery Server

This page gives instructions on how to use a Fast-DDS discovery server with the Create® 3 robot as a client.
For more information on the Fast-DDS discovery server, please refer to the [eProsima documentation](https://fast-dds.docs.eprosima.com/en/latest/fastdds/ros2/discovery_server/ros2_discovery_server.html).

*We’ll use the term computer to refer to any SBC (single board computer), virtual machine, personal computer, etc.*

## Configure Server

1. Start the discovery server on the computer that you wish to use as your server by replacing <SERVER_IP> with the server’s IP.

        fastdds discovery -i 0 -l <SERVER_IP> -p 11811
   
   ![](./data/fastdds.png)

## Configure Create® 3 Robot as a Client
1. Make sure your Create® 3 robot is connected to wifi. If it isn't, follow the directions [here](../provision/).

!!! important
    If you have enabled the discovery server previously, make sure it is disabled in the configuration settings **before** connecting it to a new wifi.*

2. Navigate to the robot’s web server via its IP.
Go to configuration settings and turn the discovery server on.
In the field `Address and port of Fast DDS discovery server`, enter the IP of your server followed by `:11811`.

3. If you intend on connecting multiple robots to the same discovery server, make sure to give the Create® 3 robot a namespace.
Restart the application after saving all settings.
  ![](./data/app-config.png)

!!! attention
      It is recommended you check the [logs](../../webserver/logs/) to confirm the discovery server has been enabled on the robot. ![](./data/logs.png)

## Configure Other Devices as Super Clients 
When using a discovery server with a Create® 3 Robot, all other devices connected to the discovery server must be set up as super clients in order to communicate with the Create® 3 Robot.

1. Before starting, stop the ROS 2 Daemon with `ros2 daemon stop`.

2. Download the .xml file found [here](data/super_client_configuration_file.xml) and replace VM_IP with your device’s IP address.

3. Navigate to your device and open terminal.

!!! important
    If the super client and server are on the same computer, make sure to open a new tab in terminal (separate terminal from where the server is running).*

4. Assign your .xml file as your default profile by entering the following.

        export FASTRTPS_DEFAULT_PROFILES_FILE=/path/to/the/xml/profile

5. Now, try running a topic list by typing `ros2 topic list`.
