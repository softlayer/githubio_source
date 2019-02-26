---
title: "connectPrivateEndpointService"
description: "Initiate the automated process to establish connectivity granting the account private back-end network access to the ser... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
aliases:
    - "/reference/services/softlayer_network/connectPrivateEndpointService"
---
# [SoftLayer_Network](/reference/services/SoftLayer_Network)::connectPrivateEndpointService

Establishes a connection between the account and Service Endpoint networks.


## Overview 
Initiate the automated process to establish connectivity granting the account private back-end network access to the services available through IBM Cloud Service Endpoint. Once initiated, the configuration process occurs asynchronously in the background. 



<h2>Responses</h2> 

<code>True</code> The request to connect was successfully initiated. 

<code>False</code> The account and Service Endpoint networks are already connected. 



<h2>Exceptions</h2> 

<code>SoftLayer_Exception_NotReady</code> Thrown when the current network configuration will not support connection alteration. 





-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network::isConnectedToPrivateEndpointService](/reference/services/SoftLayer_Network/isConnectedToPrivateEndpointService )
*  [SoftLayer_Network::disconnectPrivateEndpointService](/reference/services/SoftLayer_Network/disconnectPrivateEndpointService )



### Error Handling

* SoftLayer_Exception_NotReady 

> <<< EOT 



