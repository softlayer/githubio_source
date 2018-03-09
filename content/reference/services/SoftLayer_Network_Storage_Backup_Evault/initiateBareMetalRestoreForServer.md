---
title: "initiateBareMetalRestoreForServer"
description: "This method operates the same as the initiateBareMetalRestore() method.  However, using this method, the Bare Metal Rest... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::initiateBareMetalRestoreForServer

Initiate a bare metal restore for the specified server


## Overview 
This method operates the same as the initiateBareMetalRestore() method.  However, using this method, the Bare Metal Restore can be initiated on any Windows server under the account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| hardwareId to perform the bare metal restore on.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
boolean

