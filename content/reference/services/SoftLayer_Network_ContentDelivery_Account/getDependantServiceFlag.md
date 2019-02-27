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
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getDependantServiceFlag"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getDependantServiceFlag

Retrieve indicates if CDN account is dependent on other service. If set, this CDN account is limited to these services: createOriginPullMapping, deleteOriginPullRule, getOriginPullMappingInformation, getCdnUrls, purgeCache, loadContent, manageHttpCompression


## Overview 
Retrieve indicates if CDN account is dependent on other service. If set, this CDN account is limited to these services: createOriginPullMapping, deleteOriginPullRule, getOriginPullMappingInformation, getCdnUrls, purgeCache, loadContent, manageHttpCompression

-----

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
* boolean




