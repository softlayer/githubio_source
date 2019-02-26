---
title: "activatePublicPort"
description: "Activate a server's public network interface to the maximum available speed. This operation is an alias for [[SoftLayer_... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/activatePublicPort"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::activatePublicPort

Activate a server's public network interface.


## Overview 
Activate a server's public network interface to the maximum available speed. This operation is an alias for [[SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed]] with a $newSpeed of -1 and a $redundancy of "redundant" or unspecified (which results in the best available redundancy state). 

Receipt of a response does not indicate completion of the configuration change. Any subsequent attempts to request the interface change speed or state, while changes are pending, will result in a busy error. 

A response of true indicates a change was required to activate the interface; thus changes are pending. A response of false indicates the interface was already active, and thus no changes are pending. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Hardware_Server::setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed )
*  [SoftLayer_Hardware_Server::shutdownPublicPort](/reference/services/SoftLayer_Hardware_Server/shutdownPublicPort )
*  [SoftLayer_Hardware_Server::activatePrivatePort](/reference/services/SoftLayer_Hardware_Server/activatePrivatePort )



### Error Handling

* SoftLayer_Exception_Unavailable 

> Throws If the requested network is not available to the server 

* SoftLayer_Exception_NotReady 

> Throws If a change, not necessarily a speed change, is pending against the server 

* SoftLayer_Exception_NotReady 

> Throws If the server is not yet available for interface speed changes 

* SoftLayer_Exception_AccessDenied 

> Throws If the user requesting the change lacks the Port Control permission 



