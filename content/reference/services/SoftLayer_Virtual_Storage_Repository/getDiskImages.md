---
title: "getDiskImages"
description: "Retrieve the [[SoftLayer_Virtual_Disk_Image|disk images]] that are in a storage repository. Disk images are the virtual... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
---
# SoftLayer_Virtual_Storage_Repository::getDiskImages
## Overview 
Retrieve the [[SoftLayer_Virtual_Disk_Image|disk images]] that are in a storage repository. Disk images are the virtual hard drives for a virtual guest.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Virtual_Storage_RepositoryInitParameters
* authenticate

### Optional Headers
* SoftLayer_Virtual_Storage_RepositoryObjectMask
* SoftLayer_Virtual_Storage_RepositoryObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>
