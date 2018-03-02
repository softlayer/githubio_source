---
title: "removeAccessFromIpAddress"
description: "This method is used to modify the access control list for this Storage volume.  The SoftLayer_Network_Subnet_IpAddress o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# SoftLayer_Network_Storage::removeAccessFromIpAddress
## Overview 
This method is used to modify the access control list for this Storage volume.  The SoftLayer_Network_Subnet_IpAddress objects which have been allowed access to this storage will be listed in the allowedIpAddresses property of this storage volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddressObjectTemplate| <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean

