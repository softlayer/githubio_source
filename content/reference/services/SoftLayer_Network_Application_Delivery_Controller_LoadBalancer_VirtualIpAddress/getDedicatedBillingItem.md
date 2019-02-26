---
title: "getDedicatedBillingItem"
description: "Retrieve the current billing item for the load balancing device housing the virtual IP. This billing item represents a d... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller_loadbalancer_virtualipaddress/getDedicatedBillingItem"
---
# [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress](/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress)::getDedicatedBillingItem

Retrieve the current billing item for the load balancing device housing the virtual IP. This billing item represents a device which could contain other virtual IPs. Caution should be taken when canceling. This is only valid when dedicatedFlag is true.


## Overview 
Retrieve the current billing item for the load balancing device housing the virtual IP. This billing item represents a device which could contain other virtual IPs. Caution should be taken when canceling. This is only valid when dedicatedFlag is true.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressObjectMask
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Item_Network_LoadBalancer'>SoftLayer_Billing_Item_Network_LoadBalancer </a>




