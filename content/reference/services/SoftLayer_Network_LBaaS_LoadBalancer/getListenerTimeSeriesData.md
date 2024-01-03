---
title: "getListenerTimeSeriesData"
description: "Return listener time series datapoints. The time series data is available for Throughput, ConnectionRate and ActiveConnections. Throughput is in bits per second. The values are an average over the time range. The time series data is available for 1hour, 6hours, 12hours, 1day, 1week or 2weeks. 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_LoadBalancer"
---

# [REST Example](#getListenerTimeSeriesData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getListenerTimeSeriesData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/getListenerTimeSeriesData'
```
