# iRobot® Create® 3 Webserver - Override wpa_supplicant.conf
The wpa_supplicant override page of the Create® 3 webserver allows the user to replace the normal provisioning workflow by supplying a wpa_supplicant.conf file to the robot.

!!!warning
    Please note that this is a beta feature, and as such is not supported by the customer service team.
    Please exercise caution, as improper use of beta features may result in an inoperable robot.

![Picture of edit wpa_supplicant.conf page](data/edit-wpa-supp.png)

To access this page, it is necessary to manually navigate to the `/wpa-supp-override` URL on the robot.
This page is not accessible from the "beta menu" because it conflicts with the normal provisioning workflow of the robot in a way that could be confusing if activated by accident.

This page allows the user to directly change `wpa_supplicant.conf` on the robot.
This file is read in ONLY at boot time.
Any other provisioning done through the [normal workflow](../webserver/connect.md) will be ignored.
After pressing "save," the robot must be rebooted for the supplied wpa_supplicant.conf file to be used.
To revert to the normal provisioning workflow, either delete the text of the file from this page, save, and reboot; or factory reset the robot.

Here is an example file:
```
network={
	ssid="MyAwesomeNetwork"
	psk="$3kr1tP4s$w0rD!"
	priority=2
	scan_ssid=1
}
network={
	ssid=5461686c65656e53686168616e4172656e
	psk=e6fc52f4df9d9dfb32b149e3b6afd324d7ecc7db3852b47bb2a953d9aaca8b02
	priority=1
	scan_ssid=1
}

eapol_version=1
fast_reauth=1
ap_scan=1
filter_ssids=1
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=apps
```

[^1]: All trademarks mentioned are the property of their respective owners.