---
title: "removeAccessToReplicantFromHardwareList"
description: "This method is used to modify the access control list for this Storage replica volume.  The SoftLayer_Hardware objects w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::removeAccessToReplicantFromHardwareList
## Overview 
This method is used to modify the access control list for this Storage replica volume.  The SoftLayer_Hardware objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage replica volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareObjectTemplates| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers

### Return Values
boolean

