---
title: "createObject"
description: "Create a load balancer for a scale group. Once created, the configuration will be used to configure the load balancers f... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_LoadBalancer"
aliases:
    - "/reference/services/softlayer_scale_loadbalancer/createObject"
---
# [SoftLayer_Scale_LoadBalancer](/reference/services/SoftLayer_Scale_LoadBalancer)::createObject


Create a load balancer for a scale group. 


## Overview 
Create a load balancer for a scale group. Once created, the configuration will be used to configure the load balancers for autoscaled members. 

If the given virtual server port exists for the given virtual IP address, it is reused here if all the other values match. Otherwise, the virtual server port will be created. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer </a>| The SoftLayer_Scale_LoadBalancer object that you wish to create.|
|templateObject| <a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer </a>| The SoftLayer_Scale_LoadBalancer object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Scale_LoadBalancerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer </a>




