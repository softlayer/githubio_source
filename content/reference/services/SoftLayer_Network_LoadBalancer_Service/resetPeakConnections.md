---
title: "resetPeakConnections"
description: "Calling resetPeakConnections will set the peakConnections variable to zero on this particular object. Peak connections w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_service/resetPeakConnections"
---
# [SoftLayer_Network_LoadBalancer_Service](/reference/services/SoftLayer_Network_LoadBalancer_Service)::resetPeakConnections

Update the PeakConnections value on the service to zero.


## Overview 
Calling resetPeakConnections will set the peakConnections variable to zero on this particular object. Peak connections will continue to increase normally after this method call, it will only temporarily reset the statistic to zero, until the next time it is polled. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_ServiceInitParameters

### Optional Headers

### Return Values
boolean

