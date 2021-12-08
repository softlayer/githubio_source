---
title: "getAvailableSecureTransportProtocols"
description: "Yields a list of the secure communication protocols that are currently supported on this virtual IP address instance. Th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller_loadbalancer_virtualipaddress/getAvailableSecureTransportProtocols"
---
# [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress](/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress)::getAvailableSecureTransportProtocols


Lists the secure communication protocols available to this virtual IP address 


## Overview 
Yields a list of the secure communication protocols that are currently supported on this virtual IP address instance. The list of supported ciphers for each protocol is culled to match availability. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Security_SecureTransportProtocol'>SoftLayer_Security_SecureTransportProtocol[] </a>


### Associated Methods

*  [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress::getAvailableSecureTransportCiphers](/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/getAvailableSecureTransportCiphers )




