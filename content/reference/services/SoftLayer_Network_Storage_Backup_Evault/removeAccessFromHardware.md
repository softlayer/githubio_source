---
title: "removeAccessFromHardware"
description: "This method is used to modify the access control list for this Storage volume.  The SoftLayer_Hardware objects which hav... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::removeAccessFromHardware

Remove access to this volume from a specified SoftLayer_Hardware object.


## Overview 
This method is used to modify the access control list for this Storage volume.  The SoftLayer_Hardware objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareObjectTemplate| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
boolean

