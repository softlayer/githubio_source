---
title: "getHardwareNotifications"
description: "Retrieve hardware notifications associated with this user. A hardware notification links a user to a piece of hardware,... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/getHardwareNotifications"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::getHardwareNotifications

Retrieve hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'.


## Overview 
Retrieve hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_Customer_OpenIdConnectInitParameters
* authenticate

### Optional Headers
* SoftLayer_User_Customer_OpenIdConnectObjectMask
* SoftLayer_User_Customer_OpenIdConnectObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware[] </a>

