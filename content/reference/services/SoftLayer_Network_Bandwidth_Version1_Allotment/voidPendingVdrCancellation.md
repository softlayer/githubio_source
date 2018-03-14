---
title: "voidPendingVdrCancellation"
description: "This method will void a pending cancellation on a bandwidth pool. Note however any servers that belonged to the rack wil... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/voidPendingVdrCancellation"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::voidPendingVdrCancellation

Void a pending cancellation on a bandwidth pool.


## Overview 
This method will void a pending cancellation on a bandwidth pool. Note however any servers that belonged to the rack will have to be restored individually using the method voidPendingServerMove($id, $type). 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters

### Optional Headers

### Return Values
boolean

