---
title: "createSubnetRouteUpdateTransaction"
description: "This function is used to create a new transaction to modify a subnet route. Routes are updated in one to two minutes dep... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
---
# SoftLayer_Network_Subnet::createSubnetRouteUpdateTransaction
## Overview 
This function is used to create a new transaction to modify a subnet route. Routes are updated in one to two minutes depending on the number of transactions that are pending for a router. 

Usage of this function is restricted and may only be called from authorized accounts. It is not available for general API users without justification and consent from a SoftLayer representative. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newEndPointIpAddress| string| The IP address to route the subnet to|


### Required Headers
* authenticate
* SoftLayer_Network_SubnetInitParameters

### Optional Headers

### Return Values
boolean
