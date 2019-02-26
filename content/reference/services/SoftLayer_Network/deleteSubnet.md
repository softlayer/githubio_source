---
title: "deleteSubnet"
description: "Provide a Subnet template containing the following properties: 
* networkIdentifier
* cidr
The ``networkIdentifier`` mus... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
aliases:
    - "/reference/services/softlayer_network/deleteSubnet"
---
# [SoftLayer_Network](/reference/services/SoftLayer_Network)::deleteSubnet

Remove a Subnet from the Network


## Overview 


Provide a Subnet template containing the following properties: 
* networkIdentifier
* cidr
The ``networkIdentifier`` must represent an IP address within that specified by the Network. The ``cidr`` must be an integer between 24 and 29, inclusive, and represent a subnet size smaller than the Network's. The ``networkIdentifier``/``cidr`` must represent a valid subnet specification. Or: 
* id
The ``id`` must identify a Subnet in the Network. If the ``id`` is provided, the ``networkIdentifier``/``cidr`` will be ignored. 

Subnets may only be removed when no compute resources are utilizing them. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnet| <a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>| Subnet to be deleted|


### Required Headers
* authenticate
* SoftLayer_NetworkInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_NotFound 

> <<< EOT 

* SoftLayer_Exception_NotReady 

> <<< EOT 



