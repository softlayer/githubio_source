---
title: "allowAccessToReplicantFromVirtualGuestList"
description: "This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Virtual_Guest ob... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault::allowAccessToReplicantFromVirtualGuestList
## Overview 
This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Virtual_Guest objects which have been allowed access to this storage volume's replica will be listed in the allowedReplicationVirtualGuests property of this storage volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|virtualGuestObjectTemplates| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
boolean

