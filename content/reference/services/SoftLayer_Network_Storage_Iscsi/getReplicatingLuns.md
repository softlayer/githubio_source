---
title: "getReplicatingLuns"
description: "Retrieve the iSCSI LUN volumes being replicated by this network storage volume."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::getReplicatingLuns
## Overview 
Retrieve the iSCSI LUN volumes being replicated by this network storage volume.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_IscsiInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_IscsiObjectMask
* SoftLayer_Network_Storage_IscsiObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

