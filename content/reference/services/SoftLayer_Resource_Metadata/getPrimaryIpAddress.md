---
title: "getPrimaryIpAddress"
description: "The getPrimaryIpAddress method retrieves the primary IP address for the resource. For resources with a frontend network,... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
---
# [SoftLayer_Resource_Metadata](/reference/services/SoftLayer_Resource_Metadata)::getPrimaryIpAddress

The primary IP address for the resource


## Overview 
The getPrimaryIpAddress method retrieves the primary IP address for the resource. For resources with a frontend network, the frontend IP address will be returned. For resources that have been provisioned with only a backend network, the backend IP address will be returned, as a frontend address will not exist. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers

### Optional Headers

### Return Values
string

