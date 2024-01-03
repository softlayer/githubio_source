---
title: "getMonitoringUserNotification"
description: "The monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#getMonitoringUserNotification-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMonitoringUserNotification-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getMonitoringUserNotification'
```
