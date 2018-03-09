---
title: "getGraphImage"
description: "Get the graph image for a load balancer service based on the supplied graph type and metric.  The available graph types... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service"
---
# [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service](/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service)::getGraphImage

Get the connection or status graph image for a load balancer service.


## Overview 
Get the graph image for a load balancer service based on the supplied graph type and metric.  The available graph types are: 'connections' and 'status', and the available metrics are: 'day', 'week' and 'month'. 

This method returns the raw binary image data. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|graphType| string| The graph type can be either 'connections' or 'status'.|
|metric| string| The metric can be 'day', 'week', or 'month'.|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_ServiceInitParameters

### Optional Headers

### Return Values
binary data

