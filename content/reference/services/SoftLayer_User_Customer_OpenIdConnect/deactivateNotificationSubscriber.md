---
title: "deactivateNotificationSubscriber"
description: "Create a new subscriber for a given resource."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/deactivateNotificationSubscriber"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::deactivateNotificationSubscriber


Delete a subscriber for a given resource.


## Overview 
Create a new subscriber for a given resource. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|keyName| string| The key name of the notification to subscribe. Optional, but must be provided if $resourceTableId is provided.|
|resourceTableId| integer| The resource subscribing to receive notification.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean




