---
title: "getAllowedNetworkStorageReplicas"
description: "Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
---
# SoftLayer_Network_Subnet::getAllowedNetworkStorageReplicas
## Overview 
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_SubnetInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_SubnetObjectMask
* SoftLayer_Network_SubnetObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

