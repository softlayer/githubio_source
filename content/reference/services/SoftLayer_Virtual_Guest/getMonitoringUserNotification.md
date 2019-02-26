---
title: "getMonitoringUserNotification"
description: "Retrieve the monitoring notification objects for this guest. Each object links this guest instance to a user account tha... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getMonitoringUserNotification"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getMonitoringUserNotification

Retrieve the monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails


## Overview 
Retrieve the monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Virtual_GuestInitParameters
* authenticate


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_Virtual_GuestObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest'>SoftLayer_User_Customer_Notification_Virtual_Guest[] </a>




