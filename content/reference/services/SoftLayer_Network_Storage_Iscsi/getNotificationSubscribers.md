---
title: "getNotificationSubscribers"
description: "Retrieve the subscribers that will be notified for usage amount warnings and overages."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::getNotificationSubscribers
## Overview 
Retrieve the subscribers that will be notified for usage amount warnings and overages.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_IscsiInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_IscsiObjectMask
* SoftLayer_Network_Storage_IscsiObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a>
