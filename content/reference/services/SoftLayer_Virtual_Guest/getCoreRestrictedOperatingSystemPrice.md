---
title: "getCoreRestrictedOperatingSystemPrice"
description: "If the virtual server currently has an operating system that has a core capacity restriction, return the associated core... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getCoreRestrictedOperatingSystemPrice
## Overview 
If the virtual server currently has an operating system that has a core capacity restriction, return the associated core-restricted operating system item price. Some operating systems (e.g., Red Hat Enterprise Linux) may be billed by the number of processor cores, so therefore require that a certain number of cores be present on the server. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>
