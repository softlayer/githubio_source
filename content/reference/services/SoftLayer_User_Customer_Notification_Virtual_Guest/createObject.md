---
title: "createObject"
description: "Passing in an unsaved instance of a SoftLayer_Customer_Notification_Virtual_Guest object into this function will create the object and return the results to the user. "
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

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer_Notification_Virtual_Guest]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Notification_Virtual_Guest/createObject'
```
