---
title: "getPrivateBandwidthDataSummary"
description: "Retrieve a brief summary of a server's private network bandwidth usage. getPrivateBandwidthDataSummary retrieves a serve... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getPrivateBandwidthDataSummary"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getPrivateBandwidthDataSummary

Retrieve a server's private bandwidth usage summary


## Overview 
Retrieve a brief summary of a server's private network bandwidth usage. getPrivateBandwidthDataSummary retrieves a server's bandwidth allocation for its billing period, its estimated usage during its billing period, and an estimation of how much bandwidth it will use during its billing period based on its current usage. A server's projected bandwidth usage increases in accuracy as it progresses through its billing period. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_Bandwidth_Data_Summary'>SoftLayer_Container_Network_Bandwidth_Data_Summary </a>

