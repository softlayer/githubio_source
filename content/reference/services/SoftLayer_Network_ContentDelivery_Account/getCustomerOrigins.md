---
title: "getCustomerOrigins"
description: "An origin pull mapping is a combination of your customer origin record and a CNAME (optional) record. You can now keep t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getCustomerOrigins"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getCustomerOrigins

Returns customer origins


## Overview 
An origin pull mapping is a combination of your customer origin record and a CNAME (optional) record. You can now keep track of your customer origin records separate from your CNAME records. This service returns your customer origin records. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|mediaType| string| |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping'>SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping[] </a>

