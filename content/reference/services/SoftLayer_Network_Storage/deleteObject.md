---
title: "deleteObject"
description: "Delete a network storage volume. '''This cannot be undone.''' At this time only network storage snapshots may be deleted... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# SoftLayer_Network_Storage::deleteObject
## Overview 
Delete a network storage volume. '''This cannot be undone.''' At this time only network storage snapshots may be deleted with this method. 

''deleteObject'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a volume; 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean

