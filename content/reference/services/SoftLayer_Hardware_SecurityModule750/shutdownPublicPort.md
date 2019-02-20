---
title: "shutdownPublicPort"
description: "Disconnect a server's public network interface. This operation is an alias for [[SoftLayer_Hardware_Server/setPublicNetw... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/shutdownPublicPort"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::shutdownPublicPort

Disconnect a server's public network interface.


## Overview 
Disconnect a server's public network interface. This operation is an alias for [[SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed]] with a $newSpeed of 0 and unspecified $redundancy. 

Receipt of a response does not indicate completion of the configuration change. Any subsequent attempts to request the interface change speed or state, while changes are pending, will result in a busy error. 

A response of true indicates a change was required to disconnect the interface; thus changes are pending. A response of false indicates the interface was already disconnected, and thus no changes are pending. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Hardware_Server::setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed )
*  [SoftLayer_Hardware_Server::activatePublicPort](/reference/services/SoftLayer_Hardware_Server/activatePublicPort )
*  [SoftLayer_Hardware_Server::shutdownPrivatePort](/reference/services/SoftLayer_Hardware_Server/shutdownPrivatePort )

