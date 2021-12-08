---
title: "createLiveLoadBalancer"
description: "Create or add to an application delivery controller based load balancer service. The loadBalancer parameter must have it... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller/createLiveLoadBalancer"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::createLiveLoadBalancer


Add to or create load balancer service from a virtual IP address


## Overview 
Create or add to an application delivery controller based load balancer service. The loadBalancer parameter must have its ''name'', ''type'', ''sourcePort'', and ''virtualIpAddress'' properties populated. Changes are reflected immediately in the application delivery controller. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancer| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>| The virtual IP address interface you wish to attach to the load balancer service|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_Application_Delivery_Controller::updateLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancerService](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancerService )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Invalid port supplied." if the ''sourcePort'' property in the loadBalancr parameter is empty. 

* SoftLayer_Exception_Public 

> Throw the exception "A service with the name of ''name'' already exists." if a load balancer service with the ''name'' parameter in the loadBalancer parameter already exists. 

* SoftLayer_Exception_Public 

> Throw the exception "The ip address provided is either invalid or does not belong to your account." if an invalid ''virtualIpAddress'' property in the loadBalancer parameter is provided. 

* SoftLayer_Exception_Public 

> Throw the exception "Only public IP addresses may be used." if the ''virtualIpAddress'' parameter in the loadBalancer parameter contains a private IP address. 



