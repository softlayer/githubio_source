---
title: "getBillingCycleBandwidthUsage"
description: "Retrieve a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for ea... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
# SoftLayer_Network_Bandwidth_Version1_Allotment::getBillingCycleBandwidthUsage
## Overview 
Retrieve a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Bandwidth_Version1_AllotmentObjectMask
* SoftLayer_Network_Bandwidth_Version1_AllotmentObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>

