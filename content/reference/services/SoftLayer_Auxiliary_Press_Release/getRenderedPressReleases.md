---
title: "getRenderedPressReleases"
description: "Retrieve an array of SoftLayer_Auxiliary_Press_Release data types, which contain all press releases for a given year and... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release"
---
# SoftLayer_Auxiliary_Press_Release::getRenderedPressReleases
## Overview 
Retrieve an array of SoftLayer_Auxiliary_Press_Release data types, which contain all press releases for a given year and or result limit. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|resultLimit| string| |
|year| string| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Auxiliary_Press_ReleaseObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Auxiliary_Press_ReleaseObjectFilter

### Return Values
<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release'>SoftLayer_Auxiliary_Press_Release[] </a>
