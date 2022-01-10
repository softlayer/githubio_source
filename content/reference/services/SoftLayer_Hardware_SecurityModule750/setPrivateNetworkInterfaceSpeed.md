---
title: "setPrivateNetworkInterfaceSpeed"
description: "Set the private network interface speed and redundancy configuration. 

Possible $newSpeed values are -1 (maximum availa... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/setPrivateNetworkInterfaceSpeed"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::setPrivateNetworkInterfaceSpeed


Set the speed and redundancy configuration of a server's private network interface.


## Overview 
Set the private network interface speed and redundancy configuration. 

Possible $newSpeed values are -1 (maximum available), 0 (disconnect), 10, 100, 1000, and 10000; not all values are available to every server. The maximum speed is limited by the speed requested during provisioning. All intermediate speeds are limited by the capability of the pod the server is deployed in. No guarantee is made that a speed other than what was requested during provisioning will be available. 

If specified, possible $redundancy values are either "redundant" or "degraded". Not specifying a redundancy mode will use the best possible redundancy available to the server. However, specifying a redundacy mode that is not available to the server will result in an error. "redundant" indicates all available interfaces should be active. "degraded" indicates only the primary interface should be active. Irrespective of the number of interfaces available to a server, it is only possible to have either a single interface or all interfaces active. 

Receipt of a response does not indicate completion of the configuration change. Any subsequent attempts to request the interface change speed or state, while changes are pending, will result in a busy error. 

A response of true indicates a change was required to achieve the desired interface configuration; thus changes are pending. A response of false indicates the current interface configuration matches the desired configuration, and thus no changes are pending. 

<h4>Backwards Compatibility Until February 27th, 2019</h4> 

In order to provide a period of transition to the new API, some backwards compatible behaviors will be active during this period. <ul> <li> A "doubled" (eg. 200) speed value will be translated to a redundancy value of "redundant". If a redundancy value is specified, it is assumed no translation is needed and will result in an error due to doubled speeds no longer being valid.</li> <li> A non-doubled (eg. 100) speed value <i>without</i> a redundancy value will be translated to a redundancy value of "degraded".</li> </ul> After the compatibility period, a doubled speed value will result in an error, and a non-doubled speed value without a redundancy value specified will result in the best available redundancy state. An exception is made for the new relative speed value -1. When using -1 without a redundancy value, the best possible redundancy will be used. Please transition away from using doubled speed values in favor of specifying redundancy (when applicable) or using relative speed values 0 and -1. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newSpeed| integer| Desired speed or -1 for maximum available, 0 for disconnect|
|redundancy| string| The desired state of redundancy for the interface(s)|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Hardware_Server::setPrivateNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed )
*  [SoftLayer_Hardware_Server::activatePublicPort](/reference/services/SoftLayer_Hardware_Server/activatePublicPort )
*  [SoftLayer_Hardware_Server::shutdownPublicPort](/reference/services/SoftLayer_Hardware_Server/shutdownPublicPort )



### Error Handling

* SoftLayer_Exception_InvalidValue 

> Throws If speed is not a sane value 

* SoftLayer_Exception_InvalidValue 

> Throws If a specified redundancy mode is not 'redundant' or 'degraded' 

* SoftLayer_Exception_NotSupported 

> Throws If the requested speed is not available to the server 

* SoftLayer_Exception_NotSupported 

> Throws If the requested redundancy mode is not available to the server 

* SoftLayer_Exception_Unavailable 

> Throws If the requested network is not available to the server 

* SoftLayer_Exception_NotReady 

> Throws If a change, not necessarily a speed change, is pending against the server 

* SoftLayer_Exception_NotReady 

> Throws If the server is not yet available for interface speed changes 

* SoftLayer_Exception_AccessDenied 

> Throws If the user requesting the change lacks the Port Control permission 



