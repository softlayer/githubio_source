---
title: "deleteObjects"
description: "Detach several VLANs. This will not detach them right away, but rather start an asynchronous process to detach."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Vlan"
aliases:
    - "/reference/services/softlayer_network_gateway_vlan/deleteObjects"
---
# [SoftLayer_Network_Gateway_Vlan](/reference/services/SoftLayer_Network_Gateway_Vlan)::deleteObjects

Attach a VLAN to a gateway


## Overview 
Detach several VLANs. This will not detach them right away, but rather start an asynchronous process to detach. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan[] </a>| An array of skeleton SoftLayer_Network_Gateway_Vlan objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate


### Return Values
* boolean




