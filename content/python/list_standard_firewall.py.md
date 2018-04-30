---
title: "list_standard_firewall.py"
description: "list_standard_firewall.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Component_Firewall"
tags:
    - "firewalls"
---


```
#
# List standard firewalls
#
# This script will display the virtual servers with
# firewall configured on them, a view like the
# following will be displayed
# +-----------+-------------------------+-------------+-------------------------------------+-----------------+
# | Server ID |       Server Name       | Firewall ID | Firewall Guest Network Component ID | Firewall Status |
# +-----------+-------------------------+-------------+-------------------------------------+-----------------+
# |  8121992  |        Test             |    43302    |               4343912               |     no_edit     |
# |  8200941  |       test-host         |    43689    |               4383153               |    allow_edit   |
#
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

# Connect to the SoftLayer_Virtual_Guest API service.

client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

# Will list the servers that have the firewallServiceComponent in the account
table = []
mask = "mask[firewallServiceComponent]"
try:
    servers = client['Account'].getVirtualGuests(mask=mask)
    for server in servers:
        if 'firewallServiceComponent' in server:
            table.append([server['id'], server['hostname'],
                          server['firewallServiceComponent']['id'],
                          server['firewallServiceComponent']['guestNetworkComponentId'],
                          server['firewallServiceComponent']['status']])
    standardFirewall = PrettyTable(["Server ID", "Server Name",
                                    "Firewall ID", "Firewall Guest Network Component ID",
                                    "Firewall Status"])
    standardFirewall.align["ID"] = "l"
    standardFirewall.padding_width = 1
    for row in table:
        standardFirewall.add_row([row[0], row[1], row[2], row[3], row[4]])
    print(standardFirewall)
except SoftLayer.SoftLayerAPIError as e:
    print("error faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
