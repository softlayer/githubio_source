---
title: "reassignServers"
description: "This method will reassign a collection of SoftLayer hardware to a bandwidth allotment Bandwidth Pool."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
# SoftLayer_Network_Bandwidth_Version1_Allotment::reassignServers
## Overview 
This method will reassign a collection of SoftLayer hardware to a bandwidth allotment Bandwidth Pool. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| A collection of servers to be reassigned to a new allotment|
|newAllotmentId| integer| The id of the allotment that the objects will be reassigned to|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

