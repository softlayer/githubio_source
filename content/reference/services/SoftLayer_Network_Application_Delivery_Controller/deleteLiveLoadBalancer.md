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
---
# SoftLayer_Network_Application_Delivery_Controller::deleteLiveLoadBalancer
## Overview 
Remove a virtual IP address from an application delivery controller based load balancer. Only the ''name'' property in the loadBalancer parameter must be populated. Changes are reflected immediately in the application delivery controller. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancer| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>| The virtual IP address interface you wish to remove|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters

### Optional Headers

### Return Values
boolean
