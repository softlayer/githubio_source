---
title: "getUsageMetricImageByDate"
description: "Returns a disk usage image based on disk usage specified by the input parameters."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
aliases:
    - "/reference/services/softlayer_virtual_storage_repository/getUsageMetricImageByDate"
---
# [SoftLayer_Virtual_Storage_Repository](/reference/services/SoftLayer_Virtual_Storage_Repository)::getUsageMetricImageByDate

Retrieve an image of the disk usage data on a [[SoftLayer_Virtual_Guest|Cloud Computing Instance]] image for the time range you provide. 


## Overview 
Returns a disk usage image based on disk usage specified by the input parameters. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|


### Required Headers
* authenticate
* SoftLayer_Virtual_Storage_RepositoryInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>




