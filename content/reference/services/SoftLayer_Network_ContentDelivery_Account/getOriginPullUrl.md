---
title: "getOriginPullUrl"
description: "This method returns the domain name of your Origin Pull rule.  It assumes you have already setup an Origin Pull rule.  O... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::getOriginPullUrl
## Overview 
This method returns the domain name of your Origin Pull rule.  It assumes you have already setup an Origin Pull rule.  Otherwise, it will throw an exception. A returning value is the value of the first parameter (origin pull domain) you provided to [[SoftLayer_Network_ContentDelivery_Account::createOriginPullRule|createOriginPullRule]] method. See Error Handling section below for possible errors. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
string


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::createOriginPullRule](/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullRule )

