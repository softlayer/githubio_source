---
title: "getBillingCycleBandwidthUsage"
description: "Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this s... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getBillingCycleBandwidthUsage

Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.


## Overview 
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_ServerInitParameters
* authenticate

### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_Hardware_ServerObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>

