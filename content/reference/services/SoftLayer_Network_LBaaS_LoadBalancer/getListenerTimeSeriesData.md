---
title: "getListenerTimeSeriesData"
description: "Return listener time series datapoints. The time series data is available for Throughput, ConnectionRate and ActiveConne... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
aliases:
    - "/reference/services/softlayer_network_lbaas_loadbalancer/getListenerTimeSeriesData"
---
# [SoftLayer_Network_LBaaS_LoadBalancer](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer)::getListenerTimeSeriesData

Return time series datapoints


## Overview 
Return listener time series datapoints. The time series data is available for Throughput, ConnectionRate and ActiveConnections. Throughput is in bits per second. The values are an average over the time range. The time series data is available for 1hour, 6hours, 12hours, 1day, 1week or 2weeks. 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|metricName| string| Values are Throughput, ConnectionRate, ActiveConnections|
|timeRange| string| Values are 1hour, 6hours, 12hours, 24hours, 1week, 2weeks|
|listenerUuid| string| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerMonitoringMetricDataPoint'>SoftLayer_Network_LBaaS_LoadBalancerMonitoringMetricDataPoint[] </a>




