---
title: "getAttachedFile"
description: "Retrieve the contents of the file attached to a SoftLayer event by it's given identifier. "
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

### [REST Example](#getAttachedFile-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAttachedFile-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/{SoftLayer_Notification_Occurrence_EventID}/getAttachedFile'
```
