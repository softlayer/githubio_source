---
title: "createObject"
description: "For IPSec network tunnels, customers can create their local subnets using this method.  After the customer is created su... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Customer_Subnet"
---
# SoftLayer_Network_Customer_Subnet::createObject
## Overview 
For IPSec network tunnels, customers can create their local subnets using this method.  After the customer is created successfully, the customer subnet can then be added to the IPSec network tunnel. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet'>SoftLayer_Network_Customer_Subnet </a>| The SoftLayer_Network_Customer_Subnet object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Customer_SubnetObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet'>SoftLayer_Network_Customer_Subnet </a>
