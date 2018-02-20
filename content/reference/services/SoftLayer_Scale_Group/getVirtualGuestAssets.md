---
title: "getVirtualGuestAssets"
description: "Retrieve collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
---
# SoftLayer_Scale_Group::getVirtualGuestAssets
## Overview 
Retrieve collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks such as resource watches. They do not count towards the auto scaling guest counts of this group in anyway and are never automatically added or removed.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Scale_GroupInitParameters
* authenticate

### Optional Headers
* SoftLayer_Scale_GroupObjectMask
* SoftLayer_Scale_GroupObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Scale_Asset'>SoftLayer_Scale_Asset[] </a>
