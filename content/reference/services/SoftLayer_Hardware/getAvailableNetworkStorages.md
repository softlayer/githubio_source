---
title: "getAvailableNetworkStorages"
description: "This method retrieves a list of SoftLayer_Network_Storage volumes that can be authorized to this SoftLayer_Hardware."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# SoftLayer_Hardware::getAvailableNetworkStorages
## Overview 
This method retrieves a list of SoftLayer_Network_Storage volumes that can be authorized to this SoftLayer_Hardware. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nasType| string| either 'ISCSI', 'NAS', or '*' for both|


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters

### Optional Headers
* SoftLayer_HardwareObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

