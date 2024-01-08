---
title: "getObject"
description: "getObject retrieves the SoftLayer_User_Customer_Notification_Hardware object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_User_Customer_Notification_Hardware service. You can only retrieve hardware notifications attached to hardware and users that belong to your account "
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

### [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Notification_Hardware/{SoftLayer_User_Customer_Notification_HardwareID}/getObject'
```
