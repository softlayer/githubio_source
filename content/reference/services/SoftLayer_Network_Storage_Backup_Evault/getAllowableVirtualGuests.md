---
title: "getAllowableVirtualGuests"
description: "This method retrieves a list of SoftLayer_Virtual_Guest that can be authorized to this SoftLayer_Network_Storage."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/getAllowableVirtualGuests"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::getAllowableVirtualGuests

Return a list of SoftLayer_Virtual_Guest that can be authorized to this volume. 


## Overview 
This method retrieves a list of SoftLayer_Virtual_Guest that can be authorized to this SoftLayer_Network_Storage. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|filterHostname| string| a string to filter the hostname by.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers
* SoftLayer_Network_Storage_Backup_EvaultObjectMask
* SoftLayer_ObjectMask
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>

