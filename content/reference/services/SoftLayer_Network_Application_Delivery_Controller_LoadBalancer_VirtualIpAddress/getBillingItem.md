---
title: "getBillingItem"
description: "Retrieve the current billing item for the load balancer virtual IP. This is only valid when dedicatedFlag is false. This... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller_loadbalancer_virtualipaddress/getBillingItem"
---
# [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress](/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress)::getBillingItem

Retrieve the current billing item for the load balancer virtual IP. This is only valid when dedicatedFlag is false. This is an independent virtual IP, and if canceled, will only affect the associated virtual IP.


## Overview 
Retrieve the current billing item for the load balancer virtual IP. This is only valid when dedicatedFlag is false. This is an independent virtual IP, and if canceled, will only affect the associated virtual IP.

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
* <a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>




