---
title: "findByGuestId"
description: "This method returns all SoftLayer_User_Customer_Notification_Virtual_Guest objects associated with the passed in ID as long as that Virtual Guest ID is owned by the current user's account. 

This behavior can also be accomplished by simply tapping monitoringUserNotification on the Virtual_Guest object. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Notification_Virtual_Guest/findByGuestId'
```
