---
title: "getStatus"
description: "Returns an array of SoftLayer_Container_Network_LoadBalancer_StatusEntry objects.  A SoftLayer_Container_Network_LoadBal... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_service/getStatus"
---
# [SoftLayer_Network_LoadBalancer_Service](/reference/services/SoftLayer_Network_LoadBalancer_Service)::getStatus


Returns various status entries for this service as an array of SoftLayer_Container_Network_LoadBalancer_StatusEntry objects


## Overview 
Returns an array of SoftLayer_Container_Network_LoadBalancer_StatusEntry objects.  A SoftLayer_Container_Network_LoadBalancer_StatusEntry object has two variables, "Label" and "Value" 

Calling this function executes a command on the physical load balancer itself, and therefore should be called infrequently.  For a general idea of the load balancer service, use the "peakConnections" variable on the Type 

Possible values for "Label" are: 


* IP Address
* Port
* Server Status
* Load Status
* Current Connections
* Total Hits


Not all labels are guaranteed to be returned. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_ServiceInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_LoadBalancer_StatusEntry'>SoftLayer_Container_Network_LoadBalancer_StatusEntry[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Bad data received from load balancer, no status could be determined." If no data could be retrieved from the load balancer 



