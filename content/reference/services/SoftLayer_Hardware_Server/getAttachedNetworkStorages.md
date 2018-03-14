---
title: "getAttachedNetworkStorages"
description: "This method is retrieve a list of SoftLayer_Network_Storage volumes that are authorized access to this SoftLayer_Hardwar... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getAttachedNetworkStorages"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getAttachedNetworkStorages

Return a list of SoftLayer_Network_Storage volumes authorized to this device. 


## Overview 
This method is retrieve a list of SoftLayer_Network_Storage volumes that are authorized access to this SoftLayer_Hardware. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nasType| string| either 'ISCSI', 'NAS', or '*' for both|


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters

### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

