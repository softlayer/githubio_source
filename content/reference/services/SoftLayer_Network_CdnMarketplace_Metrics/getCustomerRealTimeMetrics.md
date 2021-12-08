---
title: "getCustomerRealTimeMetrics"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Metrics"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_metrics/getCustomerRealTimeMetrics"
---
# [SoftLayer_Network_CdnMarketplace_Metrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics)::getCustomerRealTimeMetrics


Get the realtime metrics data for the current account. Takes the startTime and endTime and returns the total metrics data and line graph metrics data divided by the timeInterval. 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|vendorName| string| |
|startTime| integer| |
|endTime| integer| |
|timeInterval| integer| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Metrics'>SoftLayer_Container_Network_CdnMarketplace_Metrics[] </a>




