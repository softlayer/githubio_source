---
title: "removeAccessFromHost"
description: "This method is used to modify the access control list for this Storage volume.  The [SoftLayer_Hardware]({{<ref 'referen... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/removeAccessFromHost"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::removeAccessFromHost


Remove access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.


## Overview 
This method is used to modify the access control list for this Storage volume.  The [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) property of this storage volume. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|typeClassName| string| The type of class name, among: 'SoftLayer_Hardware', 'SoftLayer_Virtual_Guest', 'SoftLayer_Network_Subnet', 'SoftLayer_Network_Subnet_IpAddress'.|
|hostId| integer| |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters


### Optional Headers
* SoftLayer_Network_StorageObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>




