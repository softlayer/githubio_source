---
title: "deleteLiveLoadBalancerService"
description: "Remove an entire load balancer service, including all virtual IP addresses, from and application delivery controller bas... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller/deleteLiveLoadBalancerService"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::deleteLiveLoadBalancerService

Remove load balancer service


## Overview 
Remove an entire load balancer service, including all virtual IP addresses, from and application delivery controller based load balancer. The ''name'' property the and ''name'' property within the ''vip'' property of the service parameter must be provided. Changes are reflected immediately in the application delivery controller. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|service| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service'>SoftLayer_Network_LoadBalancer_Service </a>| The load balancer service you wish to remove with at least one ''vip'' property populated.|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_Application_Delivery_Controller::updateLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::createLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/createLiveLoadBalancer )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "The vip name must be specified for this service in order to remove it from the load balancer." is the ''name'' property within the ''vip'' property in the service parameter is not populated. 

* SoftLayer_Exception_ObjectNotFound 

> Throw the exception "''name''" if the API is unable to locate the virtual IP address with the name specified in the ''name'' property within the ''vip'' property in the service parameter. 

* SoftLayer_Exception_ObjectNotFound 

> Throw the exception "''name''" if the API is unable to locate the load balancer service with the name specified in the ''name'' property in the service parameter. 



