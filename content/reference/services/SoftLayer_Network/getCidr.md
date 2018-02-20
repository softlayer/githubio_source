---
title: "getCidr"
description: "Retrieve the size of the Network specified in CIDR notation. Specified in conjunction with the ``networkIdentifier`` to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
---
# SoftLayer_Network::getCidr
## Overview 
Retrieve the size of the Network specified in CIDR notation. Specified in conjunction with the ``networkIdentifier`` to describe the bounding subnet size for the Network. Required for creation. See [[SoftLayer_Network/createObject]] documentation for creation details.

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
integer
