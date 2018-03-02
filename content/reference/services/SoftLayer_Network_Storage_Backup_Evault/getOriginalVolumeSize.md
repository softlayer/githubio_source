---
title: "getOriginalVolumeSize"
description: "Retrieve the size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size exp... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault::getOriginalVolumeSize
## Overview 
Retrieve the size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.

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
string

