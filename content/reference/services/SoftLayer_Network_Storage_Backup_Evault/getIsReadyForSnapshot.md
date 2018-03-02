---
title: "getIsReadyForSnapshot"
description: "Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to as... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault::getIsReadyForSnapshot
## Overview 
Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_Backup_EvaultInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_Backup_EvaultObjectMask
* SoftLayer_Network_Storage_Backup_EvaultObjectFilter
* SoftLayer_ObjectMask

### Return Values
boolean

