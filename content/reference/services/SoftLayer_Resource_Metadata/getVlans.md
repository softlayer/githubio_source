---
title: "getVlans"
description: "The getVlans method returns a list of VLAN numbers for the network component matching the provided MAC address associate... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
aliases:
    - "/reference/services/softlayer_resource_metadata/getVlans"
---
# [SoftLayer_Resource_Metadata](/reference/services/SoftLayer_Resource_Metadata)::getVlans


A list of VLAN numbers for a network component


## Overview 
The getVlans method returns a list of VLAN numbers for the network component matching the provided MAC address associated with the resource. For each return, the native VLAN will appear first, followed by any trunked VLANs associated with the network component. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|macAddress| string| The MAC address to obtain the VLAN numbers for|


### Required Headers


### Return Values
* array of integers



### Error Handling

* SoftLayer_Exception_NotFound 

> Thrown when a network component is not found for the provided MAC address 

* SoftLayer_Exception_NotFound 

> Thrown when VLANs are not found for the network component 

* SoftLayer_Exception_InvalidValue 

> Thrown when the MAC address provided is invalid 



