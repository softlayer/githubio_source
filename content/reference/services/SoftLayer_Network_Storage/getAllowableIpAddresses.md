---
title: "getAllowableIpAddresses"
description: "This method retrieves a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this SoftLayer_Network_Stor... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# SoftLayer_Network_Storage::getAllowableIpAddresses
## Overview 
This method retrieves a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this SoftLayer_Network_Storage. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The Id of the Subnet required|
|filterIpAddress| string| a string to filter the IpAddress by.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers
* SoftLayer_Network_StorageObjectMask
* SoftLayer_ObjectMask
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>

