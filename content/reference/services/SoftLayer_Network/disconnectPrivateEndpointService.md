---
title: "disconnectPrivateEndpointService"
description: "Initiate the automated process to revoke mutual connectivity from the account network and IBM Cloud Service Endpoint net... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
aliases:
    - "/reference/services/softlayer_network/disconnectPrivateEndpointService"
---
# [SoftLayer_Network](/reference/services/SoftLayer_Network)::disconnectPrivateEndpointService

Terminates the connection between the account and Service Endpoint networks.


## Overview 
Initiate the automated process to revoke mutual connectivity from the account network and IBM Cloud Service Endpoint network. Once initiated, the configuration process occurs asynchronously in the background. 



<h2>Responses</h2> 

<code>True</code> The request to disconnect was successfully initiated. 

<code>False</code> The account and Service Endpoint networks are already disconnected. 



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
*  [SoftLayer_Network::connectPrivateEndpointService](/reference/services/SoftLayer_Network/connectPrivateEndpointService )



### Error Handling

* SoftLayer_Exception_NotReady 

> <<< EOT 



