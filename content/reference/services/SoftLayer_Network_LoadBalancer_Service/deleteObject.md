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
aliases:
    - "/reference/services/softlayer_network_loadbalancer_service/deleteObject"
---
# [SoftLayer_Network_LoadBalancer_Service](/reference/services/SoftLayer_Network_LoadBalancer_Service)::deleteObject

Delete this service, removing it from the load balancer.


## Overview 
Calling deleteObject on a particular server will remove it from the load balancer.  This is the only way to remove a service from your load balancer.  If you wish to remove a server, first call this function, then reload the virtualIpAddress object and edit the remaining services to reflect the other changes that you wish to make. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_ServiceInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public_Validation 

> Throws an exception whose text is a newline-delimited list of validation errors.  Each error describes the value that is missing or incorrect, and usually includes your value and a list of acceptable values 

* SoftLayer_Exception_Public 

> Throw the exception "The load balancer could not be contacted.  It may be currently in use for maintenance.  Please try again in 3-5 minutes.  If the problem persists, please open a networking ticket."  Exception text is self-explanatory. 

* SoftLayer_Exception_Public 

> Throw the exception "Errors encountered when setting up the load balancer!  Please contact customer service."  if an error has been thrown by the hardware load balancer device itself.  If the problem persists, please open a networking ticket. 

* SoftLayer_Exception_Public 

> Throw the exception "There was an error with your inital commands.  Your old configuration has been restored.  Please contact customer service." if there was an error with your configuration.  If you receive this message, your load balancer has been successfully rolled back to its previous values and will continue working, but a ticket may need to be opened to perform the changes you were attempting. 



