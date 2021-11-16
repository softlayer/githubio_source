---
title: "removeAccessFromHostList"
description: "This method is used to modify the access control list for this Storage volume.  The [SoftLayer_Hardware]({{<ref 'referen... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/removeAccessFromHostList"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::removeAccessFromHostList


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
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Optional Headers
* SoftLayer_Network_Storage_Backup_EvaultObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host[] </a>




