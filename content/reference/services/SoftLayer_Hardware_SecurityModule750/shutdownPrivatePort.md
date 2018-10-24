---
title: "shutdownPrivatePort"
description: "<b>Note:</b> All error handling and parameter documentation is referencing behavior available on January 4th, 2019. 

<h... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/shutdownPrivatePort"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::shutdownPrivatePort

Disconnect a server's private network interface.


## Overview 
<b>Note:</b> All error handling and parameter documentation is referencing behavior available on January 4th, 2019. 

<h3>Behavior deprecated on January 4th, 2019</h3> 

Shuts down the private network port 

<h3>NEW! Behavior on January 4th, 2019</h3> 

Disconnect a server's private network interface. This operation is an alias for calling [[SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed]] with a $newSpeed of 0 and default $redundancy. 

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

*  [SoftLayer_Hardware_Server::setPrivateNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed )
*  [SoftLayer_Hardware_Server::activatePrivatePort](/reference/services/SoftLayer_Hardware_Server/activatePrivatePort )
*  [SoftLayer_Hardware_Server::shutdownPublicPort](/reference/services/SoftLayer_Hardware_Server/shutdownPublicPort )

