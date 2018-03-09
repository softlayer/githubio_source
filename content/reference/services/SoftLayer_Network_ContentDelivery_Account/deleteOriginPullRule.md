---
title: "deleteOriginPullRule"
description: "This method removes an Origin Pull domain rule.  Once an Origin Pull rule is removed, you will be able to access the /me... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::deleteOriginPullRule

Removes an Origin Pull domain rule


## Overview 
This method removes an Origin Pull domain rule.  Once an Origin Pull rule is removed, you will be able to access the /media/http directory. It will take 10 to 15 minutes for this to take effect after you remove your Origin Pull rule.  Cached contents on CDN POPs may live longer than 15 minutes. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|originMappingId| string| An origin pull mapping ID|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::createOriginPullRule](/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullRule )

