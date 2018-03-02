---
title: "createSubscriberDeliveryMethods"
description: "Create delivery methods for a notification that the user is subscribed to. Multiple delivery method keyNames can be supp... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::createSubscriberDeliveryMethods
## Overview 
Create delivery methods for a notification that the user is subscribed to. Multiple delivery method keyNames can be supplied to create multiple delivery methods for the specified notification. Available delivery methods - 'EMAIL'. Available notifications - 'PLANNED_MAINTENANCE', 'UNPLANNED_INCIDENT'. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|notificationKeyName| string| A friendly keyname for the notification|
|deliveryMethodKeyNames| array of strings| Friendly delivery method keynames|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean

