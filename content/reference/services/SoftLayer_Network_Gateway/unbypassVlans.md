---
title: "unbypassVlans"
description: "Start the asynchronous process to unbypass the provided VLANs. The VLANs must already be attached. Any VLANs that are al... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
aliases:
    - "/reference/services/softlayer_network_gateway/unbypassVlans"
---
# [SoftLayer_Network_Gateway](/reference/services/SoftLayer_Network_Gateway)::unbypassVlans

Bypass VLANs


## Overview 
Start the asynchronous process to unbypass the provided VLANs. The VLANs must already be attached. Any VLANs that are already unbypassed will be ignored. The status field can be checked for progress. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|vlans| <a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_GatewayInitParameters


### Return Values
* void




