---
title: "deleteLiveLoadBalancer"
description: "Remove a virtual IP address from an application delivery controller based load balancer. Only the ''name'' property in t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller/deleteLiveLoadBalancer"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::deleteLiveLoadBalancer


Remove a virtual IP address from a load balancer


## Overview 
Remove a virtual IP address from an application delivery controller based load balancer. Only the ''name'' property in the loadBalancer parameter must be populated. Changes are reflected immediately in the application delivery controller. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancer| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>| The virtual IP address interface you wish to remove|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_Application_Delivery_Controller::updateLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::createLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/createLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancerService](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancerService )



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the exception "''name''" if the API is unable to locate a virtual IP address on the load balancer with the name specified in the ''name'' property in the loadBalancer parameter. 



