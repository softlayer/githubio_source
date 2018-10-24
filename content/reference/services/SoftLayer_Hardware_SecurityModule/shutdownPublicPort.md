---
title: "shutdownPublicPort"
description: "<b>Note:</b> All error handling and parameter documentation is referencing behavior available on January 4th, 2019. 

<h... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/shutdownPublicPort"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::shutdownPublicPort

Disconnect a server's public network interface.


## Overview 
<b>Note:</b> All error handling and parameter documentation is referencing behavior available on January 4th, 2019. 

<h3>Behavior deprecated on January 4th, 2019</h3> 

Shuts down the public network port 

<h3>NEW! Behavior on January 4th, 2019</h3> 

Disconnect a server's public network interface. This operation is an alias for [[SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed]] with a $newSpeed of 0 and default $redundancy. 

Receipt of a response does not indicate completion of the configuration change. Any subsequent attempts to request the interface change speed or state, while changes are pending, will result in a busy error. 

A response of true indicates a change was required to disconnect the interface; thus changes are pending. A response of false indicates the interface was already disconnected, and thus no changes are pending. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Hardware_Server::setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed )
*  [SoftLayer_Hardware_Server::activatePublicPort](/reference/services/SoftLayer_Hardware_Server/activatePublicPort )
*  [SoftLayer_Hardware_Server::shutdownPrivatePort](/reference/services/SoftLayer_Hardware_Server/shutdownPrivatePort )

