---
title: "getPublicBandwidthDataSummary"
description: "Retrieve a brief summary of a server's public network bandwidth usage. getPublicBandwidthDataSummary retrieves a server'... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getPublicBandwidthDataSummary"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getPublicBandwidthDataSummary


Retrieve a server's public bandwidth usage summary


## Overview 
Retrieve a brief summary of a server's public network bandwidth usage. getPublicBandwidthDataSummary retrieves a server's bandwidth allocation for its billing period, its estimated usage during its billing period, and an estimation of how much bandwidth it will use during its billing period based on its current usage. A server's projected bandwidth usage increases in accuracy as it progresses through its billing period. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Bandwidth_Data_Summary'>SoftLayer_Container_Network_Bandwidth_Data_Summary </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to load the public bandwidth data summary for the server {id}." if the API is unable to retrieve a server's public bandwidth data. 



