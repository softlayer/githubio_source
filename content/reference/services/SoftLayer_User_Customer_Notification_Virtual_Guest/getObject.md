---
title: "getObject"
description: "getObject retrieves the SoftLayer_User_Customer_Notification_Virtual_Guest object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_User_Customer_Notification_Virtual_Guest service. You can only retrieve guest notifications attached to virtual guests and users that belong to your account "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Notification_Virtual_Guest/{SoftLayer_User_Customer_Notification_Virtual_GuestID}/getObject'
```
