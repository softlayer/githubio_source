---
title: "list_planned_events.py"
description: "list_planned_events.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "brands"
---


```
'''
List planned events.

The script retrieves all the planned events in a brand account.
It displays the same result like in https://agent.softlayer.com/support/event/planned

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
import datetime

USERNAME = 'set me'
API_KEY = 'set me'

# Gets the current date.
now = datetime.datetime.now()
now = now.strftime("%m/%d/%Y")

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)

eventService = client['SoftLayer_Notification_Occurrence_Event']
objectMask = "mask[updateCount, statusCode, notificationOccurrenceEventType[keyName], impactedUsers[user[id], acknowledgedFlag]]"
objectFilterEndDate = {"endDate": {"operation": "greaterThanDate", "options": [{"name": "date", "value": [now]}]}, "notificationOccurrenceEventType": {"keyName": {"operation": "PLANNED"}}, "statusCode": {"keyName": {"operation": "in", "options": [{"name": "data", "value": ["ACTIVE", "COMPLETED"]}, {"name": "data", "value": ["ACTIVE", "COMPLETED", "PUBLISHED"]}]}}}
objectFilterNoEndDate = {"endDate": {"operation": 'is null'}, "notificationOccurrenceEventType": {"keyName": {"operation": "PLANNED"}}, "statusCode": {"keyName": {"operation": "in", "options": [{"name": "data", "value": ["ACTIVE", "COMPLETED"]}, {"name": "data", "value": ["ACTIVE", "COMPLETED", "PUBLISHED"]}]}}}

try:
    resultEndDate = eventService.getAllObjects(mask=objectMask, filter=objectFilterEndDate)
    resultNoEndDate = eventService.getAllObjects(mask=objectMask, filter=objectFilterNoEndDate)
    print(json.dumps(resultEndDate, sort_keys=True, indent=2, separators=(',', ': ')))
    print(json.dumps(resultNoEndDate, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the planned events. "
          % (e.faultCode, e.faultString))

```
