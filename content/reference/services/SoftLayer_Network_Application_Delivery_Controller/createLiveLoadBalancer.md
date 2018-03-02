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
---
# SoftLayer_Network_Application_Delivery_Controller::createLiveLoadBalancer
## Overview 
Create or add to an application delivery controller based load balancer service. The loadBalancer parameter must have its ''name'', ''type'', ''sourcePort'', and ''virtualIpAddress'' properties populated. Changes are reflected immediately in the application delivery controller. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancer| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>| The virtual IP address interface you wish to attach to the load balancer service|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_Application_Delivery_Controller::updateLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancerService](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancerService )

