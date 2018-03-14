---
title: "getBillingCycleBandwidthUsage"
description: "Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this s... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getBillingCycleBandwidthUsage"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getBillingCycleBandwidthUsage

Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.


## Overview 
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_SecurityModuleInitParameters
* authenticate

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_Hardware_SecurityModuleObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>

