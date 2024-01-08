---
title: "getImpactedResources"
description: "A collection of resources impacted by this event. Each record will relate to some physical resource that the user has access to such as [SoftLayer_Hardware](/reference/datatypes/SoftLayer_Hardware) or [SoftLayer_Virtual_Guest](/reference/datatypes/SoftLayer_Virtual_Guest)."
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

### [REST Example](#getImpactedResources-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getImpactedResources-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/{SoftLayer_Notification_Occurrence_EventID}/getImpactedResources'
```
