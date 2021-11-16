---
title: "List Planned Events"
description: "The script retrieves all the planned events that impact your account"
date: "2017-11-23"
classes: 
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "brands"
---


```python
'''
List planned events.

The script retrieves all the planned events
'''

import SoftLayer.API
from pprint import pprint as pp
import datetime


# Gets the current date.
now = datetime.datetime.now()
now = now.strftime("%m/%d/%Y")

client = SoftLayer.create_client_from_env()

eventService = client['SoftLayer_Notification_Occurrence_Event']
objectMask = "mask[updateCount, statusCode, notificationOccurrenceEventType[keyName], impactedUsers[user[id], acknowledgedFlag]]"
objectFilterEndDate = {
    "endDate": {
        "operation": "greaterThanDate", 
        "options": [{"name": "date", "value": [now]}]},
    "notificationOccurrenceEventType": {"keyName": {"operation": "PLANNED"}}, 
    "statusCode": {
        "keyName": {
            "operation": "in", 
            "options": [
                {"name": "data", "value": ["ACTIVE", "COMPLETED", "PUBLISHED"]}
            ]
        }
    }
}
objectFilterNoEndDate = {
    "endDate": {"operation": 'is null'}, 
    "notificationOccurrenceEventType": {"keyName": {"operation": "PLANNED"}},
    "statusCode": {
        "keyName": {
            "operation": "in",
            "options": [
                {"name": "data", "value": ["ACTIVE", "COMPLETED", "PUBLISHED"]}
            ]
        }
    }
}

try:
    resultEndDate = eventService.getAllObjects(mask=objectMask, filter=objectFilterEndDate)
    resultNoEndDate = eventService.getAllObjects(mask=objectMask, filter=objectFilterNoEndDate)
    pp(resultEndDate)
    pp(resultNoEndDate)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the planned events. "
          % (e.faultCode, e.faultString))

```
