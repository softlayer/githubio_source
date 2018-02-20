---
title: "getLiveLoadBalancerServiceGraphImage"
description: "Get the graph image for an application delivery controller service based on the supplied graph type and metric.  The ava... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
---
# SoftLayer_Network_Application_Delivery_Controller::getLiveLoadBalancerServiceGraphImage
## Overview 
Get the graph image for an application delivery controller service based on the supplied graph type and metric.  The available graph types are: 'connections' and 'status', and the available metrics are: 'day', 'week' and 'month'. 

This method returns the raw binary image data. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|service| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service'>SoftLayer_Network_LoadBalancer_Service </a>| The load balancer object you wish to retrieve a graph for|
|graphType| string| The string "connections" or "status" depending on the type of graph you wish to retrieve|
|metric| string| The string "day", "week", or "month" depending on the duration of data you wish to retrieve in your graph|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters

### Optional Headers

### Return Values
binary data
