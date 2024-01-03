---
title: "getImpactedDeviceCount"
description: "This method will return the number of impacted devices associated with this event for the current user. "
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

# [REST Example](#getImpactedDeviceCount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getImpactedDeviceCount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/{SoftLayer_Notification_Occurrence_EventID}/getImpactedDeviceCount'
```
