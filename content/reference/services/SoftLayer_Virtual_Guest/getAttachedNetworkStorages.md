---
title: "getAttachedNetworkStorages"
description: "This method is retrieve a list of SoftLayer_Network_Storage volumes that are authorized access to this SoftLayer_Virtual... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getAttachedNetworkStorages"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getAttachedNetworkStorages


Return a list of SoftLayer_Network_Storage volumes authorized to this device. 


## Overview 
This method is retrieve a list of SoftLayer_Network_Storage volumes that are authorized access to this SoftLayer_Virtual_Guest. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>




