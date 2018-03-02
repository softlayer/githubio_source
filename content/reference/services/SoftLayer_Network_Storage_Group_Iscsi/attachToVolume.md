---
title: "attachToVolume"
description: "Use this method to attach a SoftLayer_Network_Storage volume to this group.  This will automatically enable access to th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group_Iscsi"
---
# SoftLayer_Network_Storage_Group_Iscsi::attachToVolume
## Overview 
Use this method to attach a SoftLayer_Network_Storage volume to this group.  This will automatically enable access to this volume for any SoftLayer_Network_Storage_Allowed_Host objects currently attached to this group. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|volume| <a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Group_IscsiInitParameters

### Optional Headers

### Return Values
boolean

