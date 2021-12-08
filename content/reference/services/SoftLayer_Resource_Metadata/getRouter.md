---
title: "getRouter"
description: "The getRouter method will return the router associated with a network component. When the router is redundant, the hostn... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
aliases:
    - "/reference/services/softlayer_resource_metadata/getRouter"
---
# [SoftLayer_Resource_Metadata](/reference/services/SoftLayer_Resource_Metadata)::getRouter


The router associated with a network component


## Overview 
The getRouter method will return the router associated with a network component. When the router is redundant, the hostname of the redundant group will be returned, rather than the router hostname. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|macAddress| string| The MAC address to obtain the router for|


### Required Headers


### Return Values
* string



### Error Handling

* SoftLayer_Exception_NotFound 

> Thrown when a network component is not found for the provided MAC address 

* SoftLayer_Exception_NotFound 

> Thrown when a router is not found for the network component 

* SoftLayer_Exception_InvalidValue 

> Thrown when the MAC address provided is invalid 



