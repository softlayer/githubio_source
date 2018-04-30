---
title: "purcharse_hostids.py"
description: "purcharse_hostids.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Ticket"
tags:
    - "security"
---


```
"""
Purchase a hostIDS for a server.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createUpgradeTicket

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

attachmentId = 164203  # The hardware id where you wish to add the McAfee AntiVirus.
genericUpgrade = "Add / Upgrade Software"
upgradeMaintenanceWindow = "9.30.2015 (Wed) 01:00(GMT-0600) - 04:00(GMT-0600)"  # The time you wish to upgrade the hardware.
details = "I would like additional information on adding McAfee Host IDS ($30.00 monthly) to my account.",
attachmentType = "HARDWARE"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
ticketService = client['SoftLayer_Ticket']

try:
    response = ticketService.createUpgradeTicket(attachmentId, genericUpgrade, upgradeMaintenanceWindow, details, attachmentType)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the ticket. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
