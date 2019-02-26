---
title: "getBillingCycleBandwidthUsage"
description: "Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this s... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getBillingCycleBandwidthUsage"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getBillingCycleBandwidthUsage

Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.


## Overview 
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_SecurityModule750InitParameters
* authenticate


### Optional Headers
* SoftLayer_Hardware_SecurityModule750ObjectMask
* SoftLayer_Hardware_SecurityModule750ObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>




