---
title: "getSubnetForIpAddress"
description: "Retrieve the subnet associated with an IP address. You may only retrieve subnets assigned to your SoftLayer customer acc... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
aliases:
    - "/reference/services/softlayer_network_subnet/getSubnetForIpAddress"
---
# [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet)::getSubnetForIpAddress

Retrieve an IP addresses's associated subnet.


## Overview 
Retrieve the subnet associated with an IP address. You may only retrieve subnets assigned to your SoftLayer customer account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The IP address to search for.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_SubnetObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "You must provide a valid IP address." if the ''ipAddress'' parameter is not a valid IP address. 

* SoftLayer_Exception 

> Throw the exception "Unable to determine a subnet for the specified address of {ipAddress}" if the API is unable to locate a subnet associated with the given IP address. 



