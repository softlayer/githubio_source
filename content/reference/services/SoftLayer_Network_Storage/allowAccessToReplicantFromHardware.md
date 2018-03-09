---
title: "allowAccessToReplicantFromHardware"
description: "This method is used to modify the access control list for this Storage replicant volume.  The SoftLayer_Hardware objects... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::allowAccessToReplicantFromHardware

Allow access to this replicant volume from a specified SoftLayer_Hardware object.


## Overview 
This method is used to modify the access control list for this Storage replicant volume.  The SoftLayer_Hardware objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage replicant volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareObjectTemplate| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean

