---
title: "getReverseDomainRecords"
description: "Retrieve all reverse DNS records associated with the subnets assigned to a VLAN."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getReverseDomainRecords"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getReverseDomainRecords

Retrieve all reverse DNS records associated with a VLAN.


## Overview 
Retrieve all reverse DNS records associated with the subnets assigned to a VLAN. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_VlanInitParameters


### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>


### Associated Methods

*  [SoftLayer_Network_Subnet::getReverseDomainRecords](/reference/services/SoftLayer_Network_Subnet/getReverseDomainRecords )




