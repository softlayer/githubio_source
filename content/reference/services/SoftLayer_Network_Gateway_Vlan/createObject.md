---
title: "createObject"
description: "Create a new VLAN attachment. If the bypassFlag is false, this will also create an asynchronous process to route the VLA... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Vlan"
aliases:
    - "/reference/services/softlayer_network_gateway_vlan/createObject"
---
# [SoftLayer_Network_Gateway_Vlan](/reference/services/SoftLayer_Network_Gateway_Vlan)::createObject


Attach a VLAN to a gateway


## Overview 
Create a new VLAN attachment. If the bypassFlag is false, this will also create an asynchronous process to route the VLAN through the gateway. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan </a>| The SoftLayer_Network_Gateway_Vlan object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Gateway_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan </a>




