---
title: "getPrivateBandwidthDataSummary"
description: "Retrieve a brief summary of a server's private network bandwidth usage. getPrivateBandwidthDataSummary retrieves a serve... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getPrivateBandwidthDataSummary"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getPrivateBandwidthDataSummary

Retrieve a server's private bandwidth usage summary


## Overview 
Retrieve a brief summary of a server's private network bandwidth usage. getPrivateBandwidthDataSummary retrieves a server's bandwidth allocation for its billing period, its estimated usage during its billing period, and an estimation of how much bandwidth it will use during its billing period based on its current usage. A server's projected bandwidth usage increases in accuracy as it progresses through its billing period. 

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

> Throw the exception "Unable to load the private bandwidth data summary for the server {id}." if the API is unable to retrieve a server's public bandwidth data. 



