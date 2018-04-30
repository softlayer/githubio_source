---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_LoadBalancer_Service object whose ID number corresponds to the ID number of th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_service/getObject"
---
# [SoftLayer_Network_LoadBalancer_Service](/reference/services/SoftLayer_Network_LoadBalancer_Service)::getObject

Retrieve a SoftLayer_Network_LoadBalancer_Service record.


## Overview 
getObject retrieves the SoftLayer_Network_LoadBalancer_Service object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_LoadBalancer_Service service. You can only retrieve services on load balancers assigned to your account, and it is recommended that you simply retrieve the entire load balancer, as an individual service has no explicit purpose without its "siblings". 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_LoadBalancer_ServiceInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_LoadBalancer_ServiceObjectMask
* SoftLayer_Network_LoadBalancer_ServiceObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service'>SoftLayer_Network_LoadBalancer_Service </a>

