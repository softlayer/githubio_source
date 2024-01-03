---
title: "getAllObjects"
description: "Returns a collection of impacted users, an account master user has the ability to see all impacted users under the account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_User"
type: "reference"
layout: "method"
mainService : "SoftLayer_Notification_Occurrence_User"
---

# [REST Example](#getAllObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_User/getAllObjects'
```
