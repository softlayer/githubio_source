---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Subnet_IpAddress object whose ID number corresponds to the ID number of the in... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
---
# SoftLayer_Network_Subnet_IpAddress::getObject
## Overview 
getObject retrieves the SoftLayer_Network_Subnet_IpAddress object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Subnet_IpAddress service. You can only retrieve the IP address whose subnet is associated with a VLAN that is associated with the account that your portal user is assigned to. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Subnet_IpAddressInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Subnet_IpAddressObjectMask
* SoftLayer_Network_Subnet_IpAddressObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>

