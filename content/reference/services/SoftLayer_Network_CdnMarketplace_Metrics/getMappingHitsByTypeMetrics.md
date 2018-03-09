---
title: "getMappingHitsByTypeMetrics"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Metrics"
---
# [SoftLayer_Network_CdnMarketplace_Metrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics)::getMappingHitsByTypeMetrics

Get the total number of hits at a certain frequency over a given range of time. Frequency can be day, week, and month where each interval is one plot point for a graph. Return Data must be ordered based on startDate, endDate and frequency 


## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|mappingUniqueId| string| |
|startDate| integer| |
|endDate| integer| |
|frequency| string| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Metrics'>SoftLayer_Container_Network_CdnMarketplace_Metrics[] </a>

