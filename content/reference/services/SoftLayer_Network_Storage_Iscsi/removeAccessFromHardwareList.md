---
title: "removeAccessFromHardwareList"
description: "This method is used to modify the access control list for this Storage volume.  The SoftLayer_Hardware objects which hav... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/removeAccessFromHardwareList"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::removeAccessFromHardwareList

Remove access to this volume from multiple SoftLayer_Hardware objects.


## Overview 
This method is used to modify the access control list for this Storage volume.  The SoftLayer_Hardware objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage volume. 

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

