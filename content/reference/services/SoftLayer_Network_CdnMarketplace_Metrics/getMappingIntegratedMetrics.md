---
title: "getMappingIntegratedMetrics"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Metrics"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_metrics/getMappingIntegratedMetrics"
---
# [SoftLayer_Network_CdnMarketplace_Metrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics)::getMappingIntegratedMetrics

Get the integrated metrics data for the given mapping. You can get the the hits, bandwidth, hits by type and bandwidth by region. It will return both the total data and the detail data. 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|mappingUniqueId| string| |
|startTime| integer| |
|endTime| integer| |
|frequency| string| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Metrics'>SoftLayer_Container_Network_CdnMarketplace_Metrics[] </a>




