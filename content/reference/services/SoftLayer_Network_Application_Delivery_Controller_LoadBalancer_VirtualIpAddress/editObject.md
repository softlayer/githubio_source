---
title: "editObject"
description: "Like any other API object, the load balancers can have their exposed properties edited by passing in a modified version... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller_loadbalancer_virtualipaddress/editObject"
---
# [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress](/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress)::editObject


Edit the object by passing in a modified instance of the object


## Overview 
Like any other API object, the load balancers can have their exposed properties edited by passing in a modified version of the object.  The load balancer object also can modify its services in this way.  Simply request the load balancer object you wish to edit, then modify the objects in the services array and pass the modified object to this function.  WARNING:  Services cannot be deleted in this manner, you must call deleteObject() on the service to physically remove them from the load balancer. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress </a>| A skeleton SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "You are not authorized to change virtualIpAddress" any time a change to the Virtual IP Address is attempted.  For address changes, open a networking ticket. 

* SoftLayer_Exception_Public 

> Throw the exception "You are not authorized to change connectionLimit" any time a change to the connection limit is attempted.  For connection upgrades, use the upgradeConnectionLimit() function 

* SoftLayer_Exception_Public_Validation 

> Throws an exception whose text is a newline-delimited list of validation errors.  Each error describes the value that is missing or incorrect, and usually includes your value and a list of acceptable values 

* SoftLayer_Exception_Public 

> Throw the exception "Virtual IPs must be assigned to an account before they can be added to a load balancer" if this load balancer is somehow not linked to an account.  If this is your load balancer, please open a ticket to have this issue resolved. 

* SoftLayer_Exception_Public 

> Throw the exception "The load balancer could not be contacted.  It may be currently in use for maintenance.  Please try again in 3-5 minutes.  If the problem persists, please open a networking ticket."  Exception text is self-explanatory. 

* SoftLayer_Exception_Public 

> Throw the exception "Errors encountered when setting up the load balancer!  Please contact customer service."  if an error has been thrown by the hardware load balancer device itself.  If the problem persists, please open a networking ticket. 

* SoftLayer_Exception_Public 

> Throw the exception "There was an error with your inital commands.  Your old configuration has been restored.  Please contact customer service." if there was an error with your configuration.  If you receive this message, your load balancer has been successfully rolled back to its previous values and will continue working, but a ticket may need to be opened to perform the changes you were attempting. 

* SoftLayer_Exception_Public 

> Throw the exception "You are not authorized to change peakConnections.  Please use the function resetPeakConnections to reset peak connections to zero" if you have edited the peak connections on a service.  This is a read-only value that can only be reset by the specified function. 

* SoftLayer_Exception_Public 

> Throw the exception "An attempt was made to modify a service group with id [service group id] that is not associated with the specified virtual server." if a service grou[p 



