---
title: "get_firewall_ip_address.py"
description: "get_firewall_ip_address.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vlan"
tags:
    - "firewalls"
---


```
"""
Get the IP address from a VLan

The script lists the IP address of VLAN, it makes a single call to the
SoftLayer_Network_Vlan::getFirewallProtectableIpAddresses method.
For more information see below:

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableIpAddresses
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The Vlan Id you which get the IP address
vlanId = 361652

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # Getting the ip address
    result = client['SoftLayer_Network_Vlan'].getFirewallProtectableIpAddresses(id=vlanId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
