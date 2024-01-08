---
title: "getMappingRealTimeMetrics"
description: "Get the real time metrics data for the given mapping "
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

### [REST Example](#getMappingRealTimeMetrics-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMappingRealTimeMetrics-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Metrics/getMappingRealTimeMetrics'
```
