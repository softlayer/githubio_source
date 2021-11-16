---
title: "getVlanForIpAddress"
description: "Retrieve the VLAN associated with an IP address via the IP's associated subnet."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getVlanForIpAddress"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getVlanForIpAddress


Retrieve an IP addresses's associated VLAN.


## Overview 
Retrieve the VLAN associated with an IP address via the IP's associated subnet. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The IP address to search for.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>


### Associated Methods

*  [SoftLayer_Network_Vlan::getPrivateVlanByIpAddress](/reference/services/SoftLayer_Network_Vlan/getPrivateVlanByIpAddress )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "You must provide a valid IP address." if the ''ipAddress'' parameter is not a valid IPv4 address. 

* SoftLayer_Exception 

> Throw the exception "Unable to determine vlan for the subnet: {networkIdentifier}/{cidr}" if the API is unable to locate a VLAN associated with the subnet that the IP address belongs to. 



