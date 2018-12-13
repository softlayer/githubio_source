---
title: "isConnectedToPrivateEndpointService"
description: "Accessing select IBM Cloud services attached to the private back-end network is made possible by establishing a network... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
aliases:
    - "/reference/services/softlayer_network/isConnectedToPrivateEndpointService"
---
# [SoftLayer_Network](/reference/services/SoftLayer_Network)::isConnectedToPrivateEndpointService

Checks the current Service Endpoint network connection status.


## Overview 
Accessing select IBM Cloud services attached to the private back-end network is made possible by establishing a network relationship between an account's private network and the Service Endpoint network. 



<h2>Responses</h2> 

<code>True</code> The account and Service Endpoint networks are currently connected. 

<code>False</code> The account and Service Endpoint networks are not connected; both networks are properly configured to connect. 



<h2>Exceptions</h2> 

<code>SoftLayer_Exception_NotReady</code> Thrown when the current network configuration will not support connection alteration. 





### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network::connectPrivateEndpointService](/reference/services/SoftLayer_Network/connectPrivateEndpointService )
*  [SoftLayer_Network::disconnectPrivateEndpointService](/reference/services/SoftLayer_Network/disconnectPrivateEndpointService )

