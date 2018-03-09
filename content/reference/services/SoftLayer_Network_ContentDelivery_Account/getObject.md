---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_ContentDelivery_Account object whose ID number corresponds to the ID number of... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getObject

Retrieve a SoftLayer_Network_ContentDelivery_Account record.


## Overview 
getObject retrieves the SoftLayer_Network_ContentDelivery_Account object whose ID number corresponds to the ID number of the initial parameter passed to the SoftLayer_Network_ContentDelivery_Account service. You can only retrieve CDN accounts assigned to your SoftLayer customer account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_ContentDelivery_AccountInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_ContentDelivery_AccountObjectMask
* SoftLayer_Network_ContentDelivery_AccountObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Account'>SoftLayer_Network_ContentDelivery_Account </a>

