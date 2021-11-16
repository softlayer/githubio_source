---
title: "getPossibleInsideVlans"
description: "Get all VLANs that can become inside VLANs on this gateway. This means the VLAN must not already be an inside VLAN, on t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
aliases:
    - "/reference/services/softlayer_network_gateway/getPossibleInsideVlans"
---
# [SoftLayer_Network_Gateway](/reference/services/SoftLayer_Network_Gateway)::getPossibleInsideVlans


Get Possible Inside VLANs


## Overview 
Get all VLANs that can become inside VLANs on this gateway. This means the VLAN must not already be an inside VLAN, on the same router as this gateway, not a gateway transit VLAN, and not firewalled. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_GatewayInitParameters


### Optional Headers
* SoftLayer_Network_GatewayObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>




