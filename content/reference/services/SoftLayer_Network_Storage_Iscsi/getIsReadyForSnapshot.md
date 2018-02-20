---
title: "getIsReadyForSnapshot"
description: "Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to as... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::getIsReadyForSnapshot
## Overview 
Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_IscsiInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_IscsiObjectMask
* SoftLayer_Network_Storage_IscsiObjectFilter
* SoftLayer_ObjectMask

### Return Values
boolean
