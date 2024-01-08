---
title: "addNotificationSubscriber"
description: "Create a notification subscription record for the user. If a subscription record exists for the notification, the record will be set to active, if currently inactive. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

### [REST Example](#addNotificationSubscriber-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addNotificationSubscriber-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/addNotificationSubscriber'
```
