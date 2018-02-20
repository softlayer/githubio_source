---
title: "removeAccessToReplicantFromHardwareList"
description: "This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Hardware objects... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault::removeAccessToReplicantFromHardwareList
## Overview 
This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Hardware objects which have been allowed access to this storage volume's replica will be listed in the allowedReplicationHardware property of this storage volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareObjectTemplates| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
boolean
