---
title: "removeAccessToReplicantFromVirtualGuestList"
description: "This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Virtual_Guest ob... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/removeAccessToReplicantFromVirtualGuestList"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::removeAccessToReplicantFromVirtualGuestList

Remove access to this volume's replica from multiple SoftLayer_Virtual_Guest objects.


## Overview 
This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Virtual_Guest objects which have been allowed access to this storage volume's replica will be listed in the allowedReplicationVirtualGuests property of this storage volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|virtualGuestObjectTemplates| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean

