---
title: "getPrivateVlanByIpAddress"
description: "*** DEPRECATED ***
Retrieve the private network VLAN associated with an IP address."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getPrivateVlanByIpAddress"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getPrivateVlanByIpAddress

Retrieve the private network VLAN associated with an IP address.


## Overview 

*** DEPRECATED ***
Retrieve the private network VLAN associated with an IP address. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The IPv4 address to search for|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>


### Associated Methods

*  [SoftLayer_Network_Vlan::getVlanForIpAddress](/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "You must provide a valid IP address." if the ''ipAddress'' parameter is not a valid IPv4 address. 

* SoftLayer_Exception 

> Throw the exception "Unable to find a subnet" if the API is unable to locate any subnets on this VLAN. 

* SoftLayer_Exception 

> Throw the exception "Unable to find a valid network component for this IP address." if the API is unable to locate any network components on this VLAN. 



