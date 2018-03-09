---
title: "allowAccessFromSubnet"
description: "This method is used to modify the access control list for this Storage volume.  The SoftLayer_Network_Subnet objects whi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::allowAccessFromSubnet

Allow access to this volume from multiple SoftLayer_Network_Subnet objects.


## Overview 
This method is used to modify the access control list for this Storage volume.  The SoftLayer_Network_Subnet objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetObjectTemplate| <a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
boolean

