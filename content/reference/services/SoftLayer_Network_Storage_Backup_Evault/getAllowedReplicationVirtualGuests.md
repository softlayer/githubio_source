---
title: "getAllowedReplicationVirtualGuests"
description: "Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault::getAllowedReplicationVirtualGuests
## Overview 
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_Backup_EvaultInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_Backup_EvaultObjectMask
* SoftLayer_Network_Storage_Backup_EvaultObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>

