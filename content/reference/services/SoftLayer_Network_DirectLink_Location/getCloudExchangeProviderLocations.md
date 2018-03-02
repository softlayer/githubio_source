---
title: "getCloudExchangeProviderLocations"
description: "Retrieve all locations for a Cloud Exchange Provider. IBM SoftLayer's datacenters exist in various cities and each conta... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_DirectLink_Location"
---
# SoftLayer_Network_DirectLink_Location::getCloudExchangeProviderLocations
## Overview 
Retrieve all locations for a Cloud Exchange Provider. IBM SoftLayer's datacenters exist in various cities and each contain one or more infrastructure. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|provider| string| Direct Link Cloud Exchange provider name|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_DirectLink_LocationObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Network_DirectLink_LocationObjectFilter

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_DirectLink_Location'>SoftLayer_Network_DirectLink_Location[] </a>

