---
title: "getAssignedReplicationVolumes"
description: "Retrieve the SoftLayer_Network_Storage primary volumes whose replicas are allowed access."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_VirtualGuest"
---
# SoftLayer_Network_Storage_Allowed_Host_VirtualGuest::getAssignedReplicationVolumes
## Overview 
Retrieve the SoftLayer_Network_Storage primary volumes whose replicas are allowed access.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_Allowed_Host_VirtualGuestInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_Allowed_Host_VirtualGuestObjectMask
* SoftLayer_Network_Storage_Allowed_Host_VirtualGuestObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>
