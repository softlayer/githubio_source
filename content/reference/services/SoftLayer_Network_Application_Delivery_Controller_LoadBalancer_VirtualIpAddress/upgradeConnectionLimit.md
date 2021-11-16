---
title: "upgradeConnectionLimit"
description: "Upgrades the connection limit on the Virtual IP to Address to the next, higher connection limit of the same product."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller_loadbalancer_virtualipaddress/upgradeConnectionLimit"
---
# [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress](/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress)::upgradeConnectionLimit


Upgrades the connection limit on the Virtual IP Address and changes the billing item on your account to reflect the change.


## Overview 
Upgrades the connection limit on the Virtual IP to Address to the next, higher connection limit of the same product. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_AccessDenied 

> Throw the exception "You are not authorized to upgrade this service" If you are not the primary account holder or listed as a master user 

* SoftLayer_Exception_Public 

> Throw the exception "No further upgrades available." if there are no more available upgrades 

* SoftLayer_Exception_Public 

> Throw the exception "There was an issue completing your billing changes, please open a billing ticket if the problem persists" if there was an issue completing the billing process. Open a billing ticket if the problem persists. 



