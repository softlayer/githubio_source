---
title: "rebuildvSRXHACluster"
description: "Rebuild a vSRX gateway with HA cluster by destroying existing vSRX and installing new vSRX on both gateway servers, then... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
aliases:
    - "/reference/services/softlayer_network_gateway/rebuildvSRXHACluster"
---
# [SoftLayer_Network_Gateway](/reference/services/SoftLayer_Network_Gateway)::rebuildvSRXHACluster

Rebuild Juniper vSRX HA Gateway


## Overview 
Rebuild a vSRX gateway with HA cluster by destroying existing vSRX and installing new vSRX on both gateway servers, then creating HA cluster between 2 vSRX. This is a destructive process which will remove existing vSRX configuration and stop all gateway capabilities. vSRX will need to be re-configured after this operation. 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_GatewayInitParameters


### Return Values
* boolean




