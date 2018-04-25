---
title: "unplanned_events.py"
description: "unplanned_events.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "ocurrenceevents"
---


```
"""
Get the unplanned events.

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

# Declares the API services.
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
notificationEventService = client['SoftLayer_Notification_Occurrence_Event']
accountService = client['SoftLayer_Account']

# Declares a object mask to get more information about the events.
objectMask = "mask[updateCount,statusCode,notificationOccurrenceEventType[keyName],impactedUsers[user[id],acknowledgedFlag]]"

# Gets the master user to use his id in the filter.
try:
    masterUser = accountService.getMasterUser()
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the master user. " % (e.faultCode, e.faultString))
    exit(1)

# Declares a object filter to get the unplanned events whose status is active, the impacted user is this account and the end date of the event is greater than today.
objectFilter = {"endDate" : {"operation" : "greaterThanDate", "options":  [{"name": "date","value": [now]}]} ,"impactedUsers" : {"usrRecordId" : {"operation" : masterUser["id"]}},"notificationOccurrenceEventType" : {"keyName" : {"operation" : "UNPLANNED_INCIDENT"}},"statusCode": {"keyName" : {"operation": "in","options":[{"name": "data", "value": ["ACTIVE"]}]}}}

try:
    events = notificationEventService.getAllObjects(mask=objectMask, filter=objectFilter)
    print(json.dumps(events, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the events. " % (e.faultCode, e.faultString))
    exit(1)

```
