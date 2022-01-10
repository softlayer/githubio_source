---
title: "getBackendBandwidthUse"
description: "Use this method to return an array of private bandwidth utilization records between a given date range."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getBackendBandwidthUse"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getBackendBandwidthUse

<div class="deprecated"><span class="deprecation-label">Deprecated </span></div>

Retrieves private bandwidth usage records.


## Overview 
Use this method to return an array of private bandwidth utilization records between a given date range. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| Date from which to begin retrieving bandwidth data (inclusive).|
|endDate| dateTime| Date at which to stop retrieving bandwidth data (inclusive).|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters


### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage_Detail'>SoftLayer_Network_Bandwidth_Version1_Usage_Detail[] </a>




