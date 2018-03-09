---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Bandwidth_Version1_Allotment object whose ID number corresponds to the ID numb... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::getObject

Retrieve a SoftLayer_Network_Bandwidth_Version1_Allotment record.


## Overview 
getObject retrieves the SoftLayer_Network_Bandwidth_Version1_Allotment object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Hardware service. You can only retrieve an allotment associated with the account that your portal user is assigned to. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Bandwidth_Version1_AllotmentObjectMask
* SoftLayer_Network_Bandwidth_Version1_AllotmentObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>

