---
title: "createObject"
description: "Provide a template containing the following properties to create a Network: 
* networkIdentifier
* cidr
* name


The ``n... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
---
# [SoftLayer_Network](/reference/services/SoftLayer_Network)::createObject

Create a Network


## Overview 
Provide a template containing the following properties to create a Network: 
* networkIdentifier
* cidr
* name


The ``networkIdentifier`` must be an IP address within RFC 1918 blocks: 
* 192.168.0.0/16
* 172.16.0.0/12
* 10.0.0.0/8
The ``cidr`` must be an integer between 16 and 24, inclusive. The ``networkIdentifier``/``cidr`` must represent a valid subnet specification. The ``name`` must not be empty, but otherwise can contain up to 50 characters of user specified information to identify the Network. 

The subnet specification of the Network bounds the IP address space which can be utilized and constrains the creation of Subnets within the Network. 

Example networkIdentifier/CIDR combinations: 
* 192.168.0.0/16
* 192.168.0.0/17
* 172.16.0.0/16
* 172.31.0.0/16
* 10.0.0.0/16
* 10.255.0.0/16

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network'>SoftLayer_Network </a>| The SoftLayer_Network object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_NetworkObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network'>SoftLayer_Network </a>

