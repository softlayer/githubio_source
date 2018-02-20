---
title: "getScaleLoadBalancers"
description: "Retrieve collection of scale load balancers that use this health check."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check"
---
# SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check::getScaleLoadBalancers
## Overview 
Retrieve collection of scale load balancers that use this health check.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_CheckInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_CheckObjectMask
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_CheckObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer[] </a>
