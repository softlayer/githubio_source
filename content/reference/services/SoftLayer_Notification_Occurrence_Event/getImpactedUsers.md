---
title: "getImpactedUsers"
description: "A collection of users impacted by this event. Each impacted user record relates directly to a [SoftLayer_User_Customer](/reference/datatypes/SoftLayer_User_Customer)."
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

# [REST Example](#getImpactedUsers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getImpactedUsers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/{SoftLayer_Notification_Occurrence_EventID}/getImpactedUsers'
```
