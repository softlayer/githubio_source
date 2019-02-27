---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_LoadBalancer_Global_Host object whose ID number corresponds to the ID number o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Host"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_global_host/getObject"
---
# [SoftLayer_Network_LoadBalancer_Global_Host](/reference/services/SoftLayer_Network_LoadBalancer_Global_Host)::getObject

Retrieve a SoftLayer_Network_LoadBalancer_Global_Host record.


## Overview 
getObject retrieves the SoftLayer_Network_LoadBalancer_Global_Host object whose ID number corresponds to the ID number of the init paramater passed to the SoftLayer_Network_LoadBalancer_Global_Host service. You can only retrieve a global load balancer host that is assigned to your SoftLayer global load balancer account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_LoadBalancer_Global_HostInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_LoadBalancer_Global_HostObjectMask
* SoftLayer_Network_LoadBalancer_Global_HostObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Host'>SoftLayer_Network_LoadBalancer_Global_Host </a>




