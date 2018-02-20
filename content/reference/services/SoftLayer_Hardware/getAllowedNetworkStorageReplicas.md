---
title: "getAllowedNetworkStorageReplicas"
description: "Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# SoftLayer_Hardware::getAllowedNetworkStorageReplicas
## Overview 
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_HardwareInitParameters
* authenticate

### Optional Headers
* SoftLayer_HardwareObjectMask
* SoftLayer_HardwareObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>
