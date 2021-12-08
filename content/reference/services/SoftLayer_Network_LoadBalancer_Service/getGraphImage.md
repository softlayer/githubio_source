---
title: "getGraphImage"
description: "Get the graph image for a load balancer service based on the supplied graph type and metric.  The available graph types... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_service/getGraphImage"
---
# [SoftLayer_Network_LoadBalancer_Service](/reference/services/SoftLayer_Network_LoadBalancer_Service)::getGraphImage


Get the connection or status graph image for a load balancer service.


## Overview 
Get the graph image for a load balancer service based on the supplied graph type and metric.  The available graph types are: 'connections' and 'status', and the available metrics are: 'day', 'week' and 'month'. 

This method returns the raw binary image data. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|graphType| string| The graph type can be either 'connections' or 'status'.|
|metric| string| The metric can be 'day', 'week', or 'month'.|


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_ServiceInitParameters


### Return Values
* binary data



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "The graphType can only be 'connections' or 'status'." when an invalid graphType is supplied. 

* SoftLayer_Exception_Public 

> Throw the exception "The metric can only be 'day', 'week', or 'month'." when an invalid metric is supplied. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to load the <graphType> graph for the <destinationIpAddress> service." when the graph could not be found or is returned in an incorrect image format. 



