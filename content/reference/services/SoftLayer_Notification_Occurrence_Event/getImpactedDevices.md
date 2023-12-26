---
title: "getImpactedDevices"
description: "This method will return a collection of SoftLayer_Notification_Occurrence_Resource objects which is a listing of the current users' impacted devices that are associated with this event. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Event"
type: "reference"
layout: "method"
mainService : "SoftLayer_Notification_Occurrence_Event"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/{SoftLayer_Notification_Occurrence_EventID}/getImpactedDevices'
```
