---
title: "updateSubscriberDeliveryMethod"
description: "Update a delivery method for a notification that the user is subscribed to. A delivery method keyName along with an acti... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/updateSubscriberDeliveryMethod"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::updateSubscriberDeliveryMethod

Update a delivery method for the subscriber.


## Overview 
Update a delivery method for a notification that the user is subscribed to. A delivery method keyName along with an active flag can be supplied to update the active status of the delivery methods for the specified notification. Available delivery methods - 'EMAIL'. Available notifications - 'PLANNED_MAINTENANCE', 'UNPLANNED_INCIDENT'. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|notificationKeyName| string| A friendly keyname for the notification|
|deliveryMethodKeyNames| array of strings| Friendly delivery method keynames|
|active| integer| |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean




