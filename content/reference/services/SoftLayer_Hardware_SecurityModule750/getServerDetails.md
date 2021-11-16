---
title: "getServerDetails"
description: "Retrieve a server's hardware components, software, and network components. getServerDetails is an aggregation function t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getServerDetails"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getServerDetails


Retrieve a server's hardware components, software, and network components.


## Overview 
Retrieve a server's hardware components, software, and network components. getServerDetails is an aggregation function that combines the results of [SoftLayer_Hardware_Server::getComponents]({{<ref "reference/services/SoftLayer_Hardware_Server/getComponents">}}), [SoftLayer_Hardware_Server::getSoftware]({{<ref "reference/services/SoftLayer_Hardware_Server/getSoftware">}}), and [SoftLayer_Hardware_Server::getNetworkComponents]({{<ref "reference/services/SoftLayer_Hardware_Server/getNetworkComponents">}}) in a single container. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Details'>SoftLayer_Container_Hardware_Server_Details </a>




