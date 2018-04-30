---
title: "list_tickets.py"
description: "list_tickets.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Brand"
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "brands"
---


```
'''
List tickets.

The script retrieves all the tickets in a brand account.
It displays the same result like in https://agent.softlayer.com/support/ticket/list

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Notification_Occurrence_Event
http://sldn.softlayer.com/article/Object-Filters
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
'''

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

brandId = 4

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY, timeout=500)
brandService = client['SoftLayer_Brand']

objectMask = "mask[group[name], status[name], statusId, id, createDate, title, assignedUser[username], attachedFileCount, totalUpdateCount, modifyDate, lastEditType, newUpdatesFlag, attachedHardwareCount, attachedVirtualGuestCount, priority, account[companyName, accountStatus[name]], assignedAgents[username], state[stateType], scheduledActions[transactionGroup, ticketScheduledActionReference] ]"
objectFilter = {"tickets": {"status": {"name": {"operation": "in", "options":  [{"name": "data", "value": ["Open", "Assigned"]}]}}}}

try:
    result = brandService.getTickets(id=brandId, filter=objectFilter, mask=objectMask)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the tickets. "
          % (e.faultCode, e.faultString))

```
