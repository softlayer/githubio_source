---
title: "createObject"
description: "Create and return a new gateway. This object can be created with any number of members or VLANs, but they all must be in... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
aliases:
    - "/reference/services/softlayer_network_gateway/createObject"
---
# [SoftLayer_Network_Gateway](/reference/services/SoftLayer_Network_Gateway)::createObject

Create a new server gateway


## Overview 
Create and return a new gateway. This object can be created with any number of members or VLANs, but they all must be in the same pod. By creating a gateway with members and/or VLANs attached, it is the equivalent of individually calling their createObject methods except this will start a single asynchronous process to setup the gateway. The status of this process can be checked using the status field. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>| The SoftLayer_Network_Gateway object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_GatewayObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>




