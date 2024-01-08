---
title: "getAcknowledgedFlag"
description: "Indicates whether or not this event has been acknowledged by the user."
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

### [REST Example](#getAcknowledgedFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAcknowledgedFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/{SoftLayer_Notification_Occurrence_EventID}/getAcknowledgedFlag'
```
