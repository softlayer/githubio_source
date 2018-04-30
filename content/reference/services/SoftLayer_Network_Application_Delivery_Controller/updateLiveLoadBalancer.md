---
title: "updateLiveLoadBalancer"
description: "Update the the virtual IP address interface within an application delivery controller based load balancer identified by... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller/updateLiveLoadBalancer"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::updateLiveLoadBalancer

Edit a virtual IP address within a load balancer


## Overview 
Update the the virtual IP address interface within an application delivery controller based load balancer identified by the ''name'' property in the loadBalancer parameter. You only need to set the properties in the loadBalancer parameter that you wish to change. Any virtual IP properties omitted or left empty are ignored. Changes are reflected immediately in the application delivery controller. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancer| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>| The updated virtual IP address interface record|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_Application_Delivery_Controller::createLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/createLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancer )
*  [SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancerService](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancerService )

