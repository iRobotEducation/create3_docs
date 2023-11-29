import os, sys
import subprocess
import requests

class color:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

settings = {
    'Computer Linux Distro': 'Unknown',
    'Computer ROS Distro': 'Unknown',
    'Computer RMW': 'Unknown',
    'Computer Wi-Fi Network': 'Unknown',
    'Computer Domain ID': 'Unknown',
    'Robot ROS Distro': 'Unknown',
    'Robot Firmware': 'Unknown',
    'Robot RMW': 'Unknown',
    'Robot Wi-Fi Network': 'Unknown',
    'Robot Domain ID': 'Unknown',
    'Robot Namespace': 'Unknown',
    'Discovery Server': 'Unknown'
}

def computer_settings():
    print('\n Testing Computer Configurations')

    # check linux distro
    get_linux = subprocess.run(['lsb_release','-d'],capture_output=True)
    if get_linux.returncode != 0:
        computer_linux= 'Unable to retrieve Linux distro info'
    else:
    	computer_linux = get_linux.stdout.decode('utf-8').split('Description:\t')[1].split('\n')[0]
    settings['Computer Linux Distro'] = computer_linux

    # check computer ROS version
    computer_ros = os.environ['ROS_DISTRO']
    if 'humble' in computer_ros:
        computer_ros = 'Humble'
    elif 'galactic' in computer_ros:
        computer_ros = 'Galactic'
    elif computer_ros == None:
        computer_ros = 'ROS 2 Not Installed or ROS Distro Not Set'
    else:
        computer_ros = computer_ros + ': this ROS distribution is not compatible with current Create 3 firmware'
    settings['Computer ROS Distro'] = computer_ros
    
    # check computer RMW
    computer_rmw = os.environ['RMW_IMPLEMENTATION']
    if computer_rmw == None:
        computer_rmw = 'Not Set'
    settings['Computer RMW'] = computer_rmw
    
    # check computer network
    get_ssid = subprocess.run('iwgetid',capture_output=True)
    if get_ssid.returncode != 0:
        computer_network = 'No Wi-Fi connection found'
    else:
    	computer_network = get_ssid.stdout.decode('utf-8').split('ESSID:')[1].split('"')[1]
    settings['Computer Wi-Fi Network'] = computer_network
    
    # check computer domain ID
    computer_did = os.environ.get('ROS_DOMAIN_ID')
    if computer_did == None:
        computer_did = str(0)
    settings['Computer Domain ID'] = computer_did

    # print computer settings
    for x,y in settings.items():
    	if 'Computer' in x:
            print('    '+x+': '+str(y))

def robot_settings():
    print('\n Testing Robot Configurations')   

    # import robot logs
    try:
        logs = requests.get(URL+'/logs-raw')
        logs = logs.text.split('\n')
        
        #scrape robot logs for configurations          
        for line in logs:
        # check robot RMW
            if line.find('RMW') != -1:
                robot_rmw = line.split('RMW_IMPLEMENTATION=')[1].split('\n')[0]
                settings['Robot RMW'] = robot_rmw

            # check robot wi-fi network SSID
            elif line.find('network={ 	ssid=') != -1:
                robot_network_hex = line.split('ssid=')[1].split(' \tp')[0] 
                robot_network = bytes.fromhex(robot_network_hex).decode('utf-8')
                settings['Robot Wi-Fi Network'] = robot_network

            # check robot domain ID
            elif line.find('ROS_DOMAIN_ID') != -1:
                robot_did = line.split('ROS_DOMAIN_ID=')[1].split(' ')[0]
                settings['Robot Domain ID'] = robot_did

            # check robot namespace    
            elif line.find('ROS_NAMESPACE') != -1:
                robot_namespace = line.split('ROS_NAMESPACE=')[1].split('\n')[0]
                if robot_namespace == '':
                    robot_namespace = 'None'
                settings['Robot Namespace'] = robot_namespace

            # check if discovery server is enabled
            elif line.find('FAST_DISCOVERY_ENABLED') != -1:
                discovery_server = line.split('ENABLED=')[1].split('\n')[0]
                settings['Discovery Server'] = discovery_server
        
        if settings['Robot Wi-Fi Network'] == 'Unknown':
            settings['Robot Wi-Fi Network'] = 'Not found in logs'
            # check robot firmware version
        
        homepage = requests.get(URL+'/home').text
        robot_firmware = homepage.split('VERSION: ')[1].split('</pre>')[0]
        settings['Robot Firmware'] = robot_firmware

        # check robot ROS distribution
        if 'H' in robot_firmware:
            robot_ros = 'Humble'
        elif 'G' in robot_firmware:
            robot_ros = 'Galactic'
        settings['Robot ROS Distro'] = robot_ros

    except requests.exceptions.RequestException as e:
        print (f'{color.FAIL}\nError connecting to the Create 3 Webserver. To enable receive full troubleshooting information check to make sure you have entered the correct IP address for the Create 3 robot and try again.\n\nError Output:',e,f'\n {color.ENDC}')

    # print robot settings
    for x,y in settings.items():
    	if 'Robot' in x or 'Discovery' in x:
            print('    '+x+': '+str(y))                  

def issue_check():
    print(f'{color.BOLD}\nSummary of Troubleshooting Tests {color.ENDC}')
    # check ROS 2 and Linux compatibility
    print('\nROS 2 and Linux Distribution Compatibility', end='')
    if '22.04' in settings['Computer Linux Distro'] and settings['Computer ROS Distro'] == 'Humble':
        print(f'{color.OKGREEN} OK{color.ENDC}')
    elif '20.04' in settings['Computer Linux Distro'] and settings['Computer ROS Distro'] == 'Galactic':
        print(f'{color.OKGREEN} OK{color.ENDC}')
    else:
        print(f'''{color.WARNING}\nWARNING! You computer is currently using a ROS 2 distribution 
            ('''+settings['Computer ROS Distro']+''') that is not fully supported on
            your computer's Linux distribution (''' +settings['Computer Linux Distro']+f''').
            We recommend using Ubuntu 22.04 with ROS 2 Humble and Ubuntu 20.04 with 
            ROS 2 Galactic. {color.ENDC}''')

    
    if settings['Robot Wi-Fi Network'] == 'Unknown':
        print(f'{color.FAIL}CRITICAL ALERT! This script was unable to connect to the Create 3 webserver. Therefore, only limited tests have been done. We strongly encourage you to check the IP address you entered and try again.{color.ENDC}')
    else:    

        # compare computer and robot values for ROS 2 distribution
        print('\nROS 2 Distribution Comparison:', end='')
        if settings['Computer ROS Distro'] == settings['Robot ROS Distro']:
            print(f'{color.OKGREEN} OK{color.ENDC}')
        else:
            print(f'{color.FAIL} CRITICAL ALERT! ROS 2 distributions do not match. Your computer is using '+ settings['Computer ROS Distro'] +' and your robot is using '+ settings['Robot ROS Distro']+f'.{color.ENDC}')

        # compare computer and robot values for RMW 
        print('\nROS 2 Middleware (RMW) Comparison:', end='')
        if settings['Computer RMW'] == settings['Robot RMW']:
            print(f'{color.OKGREEN} OK{color.ENDC}')
        else:
            print(f'{color.FAIL} CRITICAL ALERT! RMW settings do not match. Your computer is using '+ settings['Computer RMW'] +' and your robot is using '+ settings['Robot RMW']+f'.{color.ENDC}')
        
        # compare computer and robot values for domain ID 
        print('\nROS 2 Domain ID Comparison:', end='')
        if settings['Computer Domain ID'] == settings['Robot Domain ID']:
            print(f'{color.OKGREEN} OK{color.ENDC}')
        else:
            print(f'{color.FAIL} CRITICAL ALERT! Domain IDs do not match. Your computer is on domain ID '+ str(settings['Computer Domain ID']) +' and your robot is on domain ID '+ str(settings['Robot Domain ID'])+f'.{color.ENDC}')

        # check and compare wi-fi network SSIDs
        print('\nWi-Fi Connection:', end='')
        if settings['Robot Wi-Fi Network'] == 'Not found in logs':
            print(f'''{color.WARNING}\nWARNING! No Wi-Fi network was found in the robot's logs. This means one of two things:
            1. The robot is not connected to Wi-Fi. If you wish to use the robot on Wi-Fi go to the 
            connect page on the robot's webserver and connect to a network.
            2. The logs are too old to show the most recent connection. If you believe the robot
            is connected to a Wi-Fi network please fully reboot the robot, wait for the 
            startup chime, and run this script again.{color.ENDC}''')
        
        if settings['Computer Wi-Fi Network'] == 'No Wi-Fi connection found':
            print(f'''{color.WARNING} WARNING! No Wi-Fi network connection was found for your computer. This means one of three things:
            1. Your computer is not connected to a Wi-Fi network. 
            2. You are using a virtual machine that uses a connection type not identified
            by this script (ex. bridged network connection). If you are able to ping 
            websites or other devices on your network, you can ignore this warning. 
            3. You are using the ethernet over USB connection between your Create 3 robot 
            and your computer. In which case, you can ignore this warning. {color.ENDC}''')
        

        elif settings['Robot Wi-Fi Network'] == settings['Computer Wi-Fi Network']:
            print(f'{color.OKGREEN} OK{color.ENDC}')

        

print('This program will cross-check all relevant settings on your computer and robot to expedite troubleshooting. Please fully reboot the robot and wait for the start up chime before proceeding')

running = True

while running == True:
    ready = input('Have you rebooted and waited for the chime? (Y/n) ')
    if ready.casefold() == 'y':
        IP = input("Enter IP address of Robot: ")
        URL = "http://"+str(IP)
        #URL = 'http://192.168.1.114'
    
        computer_settings()
        robot_settings()
        issue_check()
        running = False
    else: 
        pass

