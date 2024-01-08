---
title: "getCustomerRealTimeMetrics"
description: "Get the realtime metrics data for the current account. Takes the startTime and endTime and returns the total metrics data and line graph metrics data divided by the timeInterval. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Metrics"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Metrics"
---

### [REST Example](#getCustomerRealTimeMetrics-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCustomerRealTimeMetrics-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Metrics/getCustomerRealTimeMetrics'
```
