---
title: "resetPeakConnections"
description: "Calling resetPeakConnections will set the peakConnections variable to zero on this particular object. Peak connections w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_service/resetPeakConnections"
---
# [SoftLayer_Network_LoadBalancer_Service](/reference/services/SoftLayer_Network_LoadBalancer_Service)::resetPeakConnections


Update the PeakConnections value on the service to zero.


## Overview 
Calling resetPeakConnections will set the peakConnections variable to zero on this particular object. Peak connections will continue to increase normally after this method call, it will only temporarily reset the statistic to zero, until the next time it is polled. 

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



