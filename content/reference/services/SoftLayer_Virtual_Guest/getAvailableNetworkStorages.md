---
title: "getAvailableNetworkStorages"
description: "This method retrieves a list of SoftLayer_Network_Storage volumes that can be authorized to this SoftLayer_Virtual_Guest... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getAvailableNetworkStorages
## Overview 
This method retrieves a list of SoftLayer_Network_Storage volumes that can be authorized to this SoftLayer_Virtual_Guest. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nasType| string| either 'ISCSI', 'NAS', or '*' for both|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

