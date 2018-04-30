---
title: "getSnapshotsForVolume"
description: "Retrieves a list of snapshots for this SoftLayer_Network_Storage volume. This method works with the result limits and of... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/getSnapshotsForVolume"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::getSnapshotsForVolume

Retrieves a list of snapshots for a given volume.


## Overview 
Retrieves a list of snapshots for this SoftLayer_Network_Storage volume. This method works with the result limits and offset to support pagination. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers
* SoftLayer_Network_Storage_IscsiObjectMask
* SoftLayer_ObjectMask
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

