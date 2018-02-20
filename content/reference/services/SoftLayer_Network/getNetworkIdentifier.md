---
title: "getNetworkIdentifier"
description: "Retrieve the starting IP address of the Network. Specified in conjunction with the ``cidr`` property to specify the boun... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
---
# SoftLayer_Network::getNetworkIdentifier
## Overview 
Retrieve the starting IP address of the Network. Specified in conjunction with the ``cidr`` property to specify the bounding IP address space for the Network. Required for creation. See [[SoftLayer_Network/createObject]] documentation for creation details.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_NetworkInitParameters
* authenticate

### Optional Headers
* SoftLayer_NetworkObjectMask
* SoftLayer_NetworkObjectFilter
* SoftLayer_ObjectMask

### Return Values
string
