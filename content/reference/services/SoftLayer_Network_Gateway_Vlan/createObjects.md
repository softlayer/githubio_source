---
title: "createObjects"
description: "Create multiple new VLAN attachments. If the bypassFlag is false, this will also create an asynchronous process to route... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Vlan"
aliases:
    - "/reference/services/softlayer_network_gateway_vlan/createObjects"
---
# [SoftLayer_Network_Gateway_Vlan](/reference/services/SoftLayer_Network_Gateway_Vlan)::createObjects

Attach a VLAN to a gateway


## Overview 
Create multiple new VLAN attachments. If the bypassFlag is false, this will also create an asynchronous process to route the VLANs through the gateway. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan[] </a>| An array of SoftLayer_Network_Gateway_Vlan objects that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Gateway_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan[] </a>

