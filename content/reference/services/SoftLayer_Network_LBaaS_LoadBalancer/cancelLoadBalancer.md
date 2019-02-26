---
title: "cancelLoadBalancer"
description: "Cancel a load balancer with the given uuid. The billing system will execute the deletion of load balancer and all object... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
aliases:
    - "/reference/services/softlayer_network_lbaas_loadbalancer/cancelLoadBalancer"
---
# [SoftLayer_Network_LBaaS_LoadBalancer](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer)::cancelLoadBalancer

Cancel the specified load balancer. 


## Overview 
Cancel a load balancer with the given uuid. The billing system will execute the deletion of load balancer and all objects associated with it such as load balancer appliances, listeners, pools and members in the background. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|uuid| string| |


### Required Headers
* authenticate


### Return Values
* boolean




