---
title: "getAllowableSubnets"
description: "This method retrieves a list of SoftLayer_Network_Subnet that can be authorized to this SoftLayer_Network_Storage."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/getAllowableSubnets"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::getAllowableSubnets

Return a list of SoftLayer_Network_Subnet that can be authorized to this volume. 


## Overview 
This method retrieves a list of SoftLayer_Network_Subnet that can be authorized to this SoftLayer_Network_Storage. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|filterNetworkIdentifier| string| a string to filter the Name by.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers
* SoftLayer_Network_StorageObjectMask
* SoftLayer_ObjectMask
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>

