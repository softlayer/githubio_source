---
title: "getAllowableHardware"
description: "This method retrieves a list of SoftLayer_Hardware that can be authorized to this SoftLayer_Network_Storage."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::getAllowableHardware

Return a list of SoftLayer_Hardware that can be authorized to this volume. 


## Overview 
This method retrieves a list of SoftLayer_Hardware that can be authorized to this SoftLayer_Network_Storage. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|filterHostname| string| a string to filter the hostName by.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers
* SoftLayer_Network_StorageObjectMask
* SoftLayer_ObjectMask
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>

