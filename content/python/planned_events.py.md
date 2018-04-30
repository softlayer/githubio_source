---
title: "planned_events.py"
description: "planned_events.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "ocurrenceevents"
---


```
"""
Get the planned events.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Notification_Occurrence_Event
http://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event
http://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event/getAllObjects
http://sldn.softlayer.com/article/Object-Filters
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer.API
import json
import datetime

USERNAME = 'set me'
API_KEY = 'set me'

# Gets the current date.
now = datetime.datetime.now()
now = now.strftime("%m/%d/%Y")

# Creates the API service.
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
notificationEventService = client['SoftLayer_Notification_Occurrence_Event']

# Declares a object mask to get more information about the events.
objectMask = "mask[updateCount,statusCode,notificationOccurrenceEventType[keyName],impactedUsers[user[id],acknowledgedFlag]]"

# Declares a object filter to get the planned events whose status is active and the end date of the event is greater than today.
objectFilter = { "endDate" : {"operation" : "greaterThanDate", "options":  [{"name": "date","value": [now]}]} , "notificationOccurrenceEventType" : {"keyName" : {"operation" : "PLANNED"}},"statusCode": {"keyName" : {"operation": "in","options":[{"name": "data", "value": ["ACTIVE"]}]}}}

try:
    events = notificationEventService.getAllObjects(mask=objectMask, filter=objectFilter)
    print(json.dumps(events, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the events. " % (e.faultCode, e.faultString))
    exit(1)

```
