---
title: "assignCredential"
description: "This method will assign an existing credential to the current volume. The credential must have been created using the 'a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::assignCredential

This method will assign an existing credential to the current volume.


## Overview 
This method will assign an existing credential to the current volume. The credential must have been created using the 'addNewCredential' method. The volume type must support an additional credential. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| A username assigned to a different volume.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean

