---
title: "getIsReadyToMount"
description: "Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether anot... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/getIsReadyToMount"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::getIsReadyToMount

Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.


## Overview 
Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.

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

