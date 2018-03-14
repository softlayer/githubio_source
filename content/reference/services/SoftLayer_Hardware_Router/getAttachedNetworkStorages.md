---
title: "getAttachedNetworkStorages"
description: "This method is retrieve a list of SoftLayer_Network_Storage volumes that are authorized access to this SoftLayer_Hardwar... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
aliases:
    - "/reference/services/softlayer_hardware_router/getAttachedNetworkStorages"
---
# [SoftLayer_Hardware_Router](/reference/services/SoftLayer_Hardware_Router)::getAttachedNetworkStorages

Return a list of SoftLayer_Network_Storage volumes authorized to this device. 


## Overview 
This method is retrieve a list of SoftLayer_Network_Storage volumes that are authorized access to this SoftLayer_Hardware. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nasType| string| either 'ISCSI', 'NAS', or '*' for both|


### Required Headers
* authenticate
* SoftLayer_Hardware_RouterInitParameters

### Optional Headers
* SoftLayer_Hardware_RouterObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

