---
title: "list_vlan_firewall.py"
description: "list_vlan_firewall.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Component_Firewall"
tags:
    - "firewalls"
---


```
# List VLan firewalls
#
# This script will display a list of network VLan with firewall configured on them
# using the SoftLayer_Account::getNetworkVlans and filtering the result the "dedicatedFirewallFlag"
# will indicate if firewall is configured on the VLan, a view like the
# following will be displayed
# +---------+-----------------+-------------+--------------+----------------+
# | VLan ID |    VLan Name    | VLan Number |    Router    |    Subnet      |
# +---------+-----------------+-------------+--------------+----------------+
# |  361652 | FirewallTesting |     1763    | fcr01a.ams01 | ['5.153.7.72'] |
# +---------+-----------------+-------------+--------------+----------------+
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component_Firewall
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component_Firewall
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

# Connect to the SoftLayer_Account API service.
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

objectMask = 'mask[dedicatedFirewallFlag,primaryRouter,subnets,firewallNetworkComponents]'
table = []
try:
    vlans = client['Account'].getNetworkVlans(mask=objectMask)
    for vlan in vlans:
        if vlan['dedicatedFirewallFlag']:
            subnets = []
            for subnet in vlan['subnets']:
                subnets.append(subnet['networkIdentifier'])
            vlanName = ''
            if 'name' in vlan:
                vlanName = vlan['name']
            table.append([vlan['id'], vlanName, vlan['vlanNumber'],
                          vlan['primaryRouter']['hostname'], subnets])
    vlanFirewall = PrettyTable(["VLan ID", "VLan Name", "VLan Number", "Router", "Subnet"])
    vlanFirewall.align["ID"] = "l"
    vlanFirewall.padding_width = 1
    for row in table:
        vlanFirewall.add_row([row[0], row[1], row[2], row[3], row[4]])
    print(vlanFirewall)
except SoftLayer.SoftLayerAPIError as e:
    print("Error faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
