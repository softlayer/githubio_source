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
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/createSubscriberDeliveryMethods"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::createSubscriberDeliveryMethods

Create delivery methods for the subscriber.


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

