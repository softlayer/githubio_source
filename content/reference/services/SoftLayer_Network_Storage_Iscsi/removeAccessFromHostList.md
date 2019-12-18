---
title: "removeAccessFromHostList"
description: "This method is used to modify the access control list for this Storage volume.  The [SoftLayer_Hardware]({{<ref 'referen... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/removeAccessFromHostList"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::removeAccessFromHostList

Remove access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.


## Overview 
This method is used to modify the access control list for this Storage volume.  The [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) property of this storage volume. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hostObjectTemplates| <a href='/reference/datatypes/SoftLayer_Container_Network_Storage_Host'>SoftLayer_Container_Network_Storage_Host[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Optional Headers
* SoftLayer_Network_Storage_IscsiObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host[] </a>




