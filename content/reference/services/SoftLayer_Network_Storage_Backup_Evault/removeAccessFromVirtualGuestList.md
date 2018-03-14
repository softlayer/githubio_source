---
title: "removeAccessFromVirtualGuestList"
description: "This method is used to modify the access control list for this Storage volume.  The SoftLayer_Virtual_Guest objects whic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/removeAccessFromVirtualGuestList"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::removeAccessFromVirtualGuestList

Remove access to this volume from multiple SoftLayer_Virtual_Guest objects.


## Overview 
This method is used to modify the access control list for this Storage volume.  The SoftLayer_Virtual_Guest objects which have been allowed access to this storage will be listed in the allowedVirtualGuests property of this storage volume. 

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

