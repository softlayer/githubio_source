---
title: "getAvailableRouters"
description: "Returns all routers available for use with placement groups. If a datacenter location ID is provided, this method will f... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_PlacementGroup"
aliases:
    - "/reference/services/softlayer_virtual_placementgroup/getAvailableRouters"
---
# [SoftLayer_Virtual_PlacementGroup](/reference/services/SoftLayer_Virtual_PlacementGroup)::getAvailableRouters




## Overview 
Returns all routers available for use with placement groups. If a datacenter location ID is provided, this method will further restrict the list of routers to ones contained within that datacenter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|datacenterId| integer| An optional datacenter ID to restrict the list of routers to.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Virtual_PlacementGroupObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>




