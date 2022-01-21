#!/bin/bash

# Copyright (c) 2017-2020, NVIDIA CORPORATION.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

script_dir="$(cd "$(dirname "$0")" && pwd)"
. "${script_dir}/nv-l4t-usb-device-mode-config.sh"

if [ -f "${script_dir}/IP_ADDRESS_FOR_CREATE3_ROBOT.conf" ]; then
    robot_ip_conf_file=${script_dir}/IP_ADDRESS_FOR_CREATE3_ROBOT.conf
    cat $robot_ip_conf_file
fi

/sbin/ifconfig l4tbr0 up
# The interface might lose the address when down. Add it here to make sur
# it's configured.
/sbin/ifconfig l4tbr0 ${net_ip} netmask ${net_mask}
/sbin/ifconfig l4tbr0 add ${net_ipv6}

# IF the config file for iRobot Create® 3 (IP_ADDRESS_FOR_CREATE3_ROBOT.conf) exists, 
# then apply the static IP address (192.168.186.3), instead of enabling DHCP server
if [ -n "$robot_ip_conf_file" ]; then
    static_ip_for_robot=`cat $robot_ip_conf_file`
    /sbin/ifconfig l4tbr0 $static_ip_for_robot netmask 255.255.255.0 broadcast 192.168.186.255
    echo "Static IP address set to $static_ip_for_robot"
else

# Start a DHCP server so that connected systems automatically receive an IP
# address. This avoids users having to manually configure the connection, and
# also prevents Network Manager on Linux from destroying any manually applied
# configuration.
#
# The DHCP server must be started here, because it won't start if it's told to
# run on an interface that's down.
if [ -n "${net_dhcp_start}" ]; then
    echo "### IN"
    dhcpd_conf="${script_dir}/dhcpd.conf"
    dhcpd_leases="/run/l4t-usb-devmode-dhcpd.leases"
    dhcpd_pid="/run/l4t-usb-devmode-dhcpd.pid"
    cat > "${dhcpd_conf}" <<ENDOFHERE
max-lease-time ${net_dhcp_lease_time};
default-lease-time ${net_dhcp_lease_time};

subnet ${net_net} netmask ${net_mask} {
    range ${net_dhcp_start} ${net_dhcp_end};
}
ENDOFHERE
    rm -f "${dhcpd_leases}"
    touch "${dhcpd_leases}"
    /usr/sbin/dhcpd \
        -cf "${dhcpd_conf}" \
        -pf "${dhcpd_pid}" \
        -lf "${dhcpd_leases}" \
        l4tbr0
fi

# When an interface is set to "down", all routes through it are lost, so we
# must restore any routes when setting the interface to "up".
if [ -n "${net_ipv4_defroute_router}" ]; then
    route add default gw ${net_ipv4_defroute_router} dev l4tbr0 \
        ${net_ipv4_defroute_metric:+metric ${net_ipv4_defroute_metric}}
fi

fi

exit 0
