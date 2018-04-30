---
title: "get_standard_rules.py"
description: "get_standard_rules.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Component_Firewall_Rule"
    - "SoftLayer_Network_Component_Firewall"
tags:
    - "firewalls"
---


```
# Get Standard Rules
# Each SoftLayer_Network_Component_Firewall object stores
# its rules in the "rules" relational property. This property
# contains an array of SoftLayer_Network_Component_Firewall_Rule objects.
# These objects define the firewall rule and how it will behave
# Important Manual Pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component_Firewall/
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component_Firewall_Rule
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

# So we can talk to the SoftLayer API:
import SoftLayer
# For nice output:
from prettytable import PrettyTable

# Your SoftLayer API username and key.
#
# Generate an API key at the SoftLayer Customer Portal

API_USERNAME = 'set_me'
API_KEY = 'set_me'

client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

objectMask = "mask[firewallServiceComponent[rules]]"
# Will list the firewall rules of the server

try:
    servers = client['Account'].getVirtualGuests(mask=objectMask)
    for server in servers:
        tableIpv4 = []
        tableIpv6 = []
        if 'firewallServiceComponent' in server:
            print("Server:" + server['hostname'])
            if 'rules' in server['firewallServiceComponent']:
                rules = server['firewallServiceComponent']['rules']
                for rule in rules:
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
    print("Error  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
