---
title: "findByHardwareId"
description: "This method returns all Customer_Notification_Hardware objects associated with the passed in hardware ID as long as that hardware ID is owned by the current user's account. 

This behavior can also be accomplished by simply tapping monitoringUserNotification on the Hardware_Server object. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Notification_Hardware/findByHardwareId'
```
