---
title: "getExpiredFlag"
description: "Retrieve a flag to indicate that the presale event is expired. A presale event is expired if the current time is after t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Sales"
classes:
    - "SoftLayer_Sales_Presale_Event"
---
# SoftLayer_Sales_Presale_Event::getExpiredFlag
## Overview 
Retrieve a flag to indicate that the presale event is expired. A presale event is expired if the current time is after the end date.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Sales_Presale_EventInitParameters
* authenticate

### Optional Headers
* SoftLayer_Sales_Presale_EventObjectMask
* SoftLayer_Sales_Presale_EventObjectFilter
* SoftLayer_ObjectMask

### Return Values
boolean

