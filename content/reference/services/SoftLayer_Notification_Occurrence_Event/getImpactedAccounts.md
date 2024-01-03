---
title: "getImpactedAccounts"
description: "A collection of accounts impacted by this event. Each impacted account record relates directly to a [SoftLayer_Account](/reference/datatypes/SoftLayer_Account)."
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

# [REST Example](#getImpactedAccounts-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getImpactedAccounts-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/{SoftLayer_Notification_Occurrence_EventID}/getImpactedAccounts'
```
