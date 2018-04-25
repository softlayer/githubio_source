---
title: "get_vlan_rules.py"
description: "get_vlan_rules.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vlan_Firewall_Rule"
    - "SoftLayer_Network_Vlan"
tags:
    - "firewalls"
---


```
# Get VLAN Firewall Rules
# This script display a list of firewall rules configured
# on a Network VLan
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

# So we can talk to the SoftLayer API:
import SoftLayer.API

# For nice output:
from prettytable import PrettyTable

# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal

API_USERNAME = 'set_me'
API_KEY = 'set_me'
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

# The object mask that we're using we will retrieve the following
# for each server:
# The firewallInterfaces and firewallContextAccessControlLists

objectMask = 'mask[dedicatedFirewallFlag,firewallRules,firewallInterfaces[firewallContextAccessControlLists]]'

try:
    vlans = client['Account'].getNetworkVlans(mask=objectMask)

    for vlan in vlans:
        tableIpv4 = []
        tableIpv6 = []
        if vlan['dedicatedFirewallFlag']:
            print("VLAN number: " + str(vlan['vlanNumber']))
            if 'firewallRules' in vlan:
                for rule in vlan['firewallRules']:
                    if rule['version'] == 4:
                        tableIpv4.append([rule['action'], rule['sourceIpAddress'],
                                          rule['sourceIpCidr'], rule['destinationIpAddress'],
                                          rule['destinationIpCidr'], rule['destinationPortRangeStart'],
                                          rule['destinationPortRangeEnd'], rule['protocol']])
                    elif rule['version'] == 6:
                        tableIpv6.append([rule['action'], rule['sourceIpAddress'],
                                          rule['sourceIpCidr'], rule['destinationIpAddress'],
                                          rule['destinationIpCidr'], rule['destinationPortRangeStart'],
                                          rule['destinationPortRangeEnd'], rule['protocol']])
                if tableIpv4:
                    ipv4Rules = PrettyTable(["Action", "Source", "CIDR Source", "Destination",
                                             "CIDR destination", "Destination Port Range Start",
                                             "Destination Port Range End", "Protocol"])
                    ipv4Rules.align["ID"] = "l"
                    ipv4Rules.padding_width = 1
                    for row in tableIpv4:
                        ipv4Rules.add_row([row[0], row[1], row[2], row[3],
                                           row[4], row[5], row[6], row[7]])
                    print("    " + "Rules IPV 4")
                    print(ipv4Rules)
                if tableIpv6:
                    ipv6Rules = PrettyTable(["Action", "Source", "CIDR Source", "Destination",
                                             "CIDR destination", "Destination Port Range Start",
                                             "Destination Port Range End", "Protocol"])
                    ipv6Rules.align["ID"] = "l"
                    ipv6Rules.padding_width = 1
                    for row in tableIpv6:
                        ipv6Rules.add_row([row[0], row[1], row[2], row[3],
                                           row[4], row[5], row[6], row[7]])
                    print("    " + "Rules IP V6")
                    print(ipv6Rules)

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to Verify Order faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
