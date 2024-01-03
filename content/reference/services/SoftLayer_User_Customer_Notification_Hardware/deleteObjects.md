---
title: "deleteObjects"
description: "Like any other API object, the customer notification objects can be deleted by passing an instance of them into this function.  The ID on the object must be set. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_Notification_Hardware"
---

# [REST Example](#deleteObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer_Notification_Hardware]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Notification_Hardware/deleteObjects'
```
