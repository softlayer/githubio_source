---
title: "createObjects"
description: "Passing in a collection of unsaved instances of SoftLayer_Customer_Notification_Virtual_Guest objects into this function will create all objects and return the results to the user. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_Notification_Virtual_Guest"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer_Notification_Virtual_Guest]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Notification_Virtual_Guest/createObjects'
```
