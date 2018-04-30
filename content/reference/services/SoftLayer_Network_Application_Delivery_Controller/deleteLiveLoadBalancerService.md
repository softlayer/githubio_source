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

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|service| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service'>SoftLayer_Network_LoadBalancer_Service </a>| The load balancer service you wish to remove with at least one ''vip'' property populated.|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_Application_Delivery_Controller::updateLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::createLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/createLiveLoadBalancer )

