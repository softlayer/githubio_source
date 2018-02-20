---
title: "getDependantServiceFlag"
description: "Retrieve indicates if CDN account is dependent on other service. If set, this CDN account is limited to these services:... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::getDependantServiceFlag
## Overview 
Retrieve indicates if CDN account is dependent on other service. If set, this CDN account is limited to these services: createOriginPullMapping, deleteOriginPullRule, getOriginPullMappingInformation, getCdnUrls, purgeCache, loadContent, manageHttpCompression

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
boolean
