---
title: "deleteObject"
description: "Calling deleteObject on a particular server will remove it from the load balancer.  This is the only way to remove a ser... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
---
# SoftLayer_Network_LoadBalancer_Service::deleteObject
## Overview 
Calling deleteObject on a particular server will remove it from the load balancer.  This is the only way to remove a service from your load balancer.  If you wish to remove a server, first call this function, then reload the virtualIpAddress object and edit the remaining services to reflect the other changes that you wish to make. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_ServiceInitParameters

### Optional Headers

### Return Values
boolean

