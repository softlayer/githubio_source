---
title: "getCustomerInvoicingMetrics"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Metrics"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_metrics/getCustomerInvoicingMetrics"
---
# [SoftLayer_Network_CdnMarketplace_Metrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics)::getCustomerInvoicingMetrics

Get the static & dynamic bandwidth and mapping hits of predetermined statistics for direct display (no graph) for a customer's account over a given period of time. Frequency can be 'day', 'aggregate'. If the value 'day' is specified for Frequency, return data will be ordered based on startDate to endDate, and if the value 'aggregate' is specified for Frequency, aggregated data from startDate to endDate will be returned. There is a delay within 3 days(including today) for fetching the metrics data. 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|vendorName| string| |
|startDate| integer| The start data timestamp(UTC+0), the date can not be earlier than 93 days ago|
|endDate| integer| The end data timestamp(UTC+0), the date can not be later than 3 days ago|
|frequency| string| The frequency for query, supported type 'day', 'aggregate'|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Metrics'>SoftLayer_Container_Network_CdnMarketplace_Metrics[] </a>




