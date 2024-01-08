---
title: "updateNotificationSubscriber"
description: "Update the active status for a notification that the user is subscribed to. A notification along with an active flag can be supplied to update the active status for a particular notification subscription. "
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

### [REST Example](#updateNotificationSubscriber-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateNotificationSubscriber-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/updateNotificationSubscriber'
```
