---
title: "createSubnetRouteUpdateTransaction"
description: "***DEPRECATED***
This endpoint is deprecated in favor of the more expressive and capable SoftLayer_Network_Subnet::route... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
aliases:
    - "/reference/services/softlayer_network_subnet/createSubnetRouteUpdateTransaction"
---
# [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet)::createSubnetRouteUpdateTransaction

create a new transaction to modify a subnet route.


## Overview 

***DEPRECATED***
This endpoint is deprecated in favor of the more expressive and capable SoftLayer_Network_Subnet::route, to which this endpoint now proxies. Refer to it for more information. 

Similarly, unroute requests are proxied to SoftLayer_Network_Subnet::clearRoute. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newEndPointIpAddress| string| The IP address to route the subnet to|


### Required Headers
* authenticate
* SoftLayer_Network_SubnetInitParameters


### Return Values
* boolean




