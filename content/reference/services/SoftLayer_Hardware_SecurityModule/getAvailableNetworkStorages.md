---
title: "getAvailableNetworkStorages"
description: "This method retrieves a list of SoftLayer_Network_Storage volumes that can be authorized to this SoftLayer_Hardware."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getAvailableNetworkStorages"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getAvailableNetworkStorages

Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 


## Overview 
This method retrieves a list of SoftLayer_Network_Storage volumes that can be authorized to this SoftLayer_Hardware. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nasType| string| either 'ISCSI', 'NAS', or '*' for both|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

