---
title: "getMappingHitsMetrics"
description: "Get the total number of hits at a certain frequency over a given range of time per domain mapping. Frequency can be day, week, and month where each interval is one plot point for a graph. Return Data will be ordered based on startDate, endDate and frequency. "
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

# [REST Example](#getMappingHitsMetrics-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMappingHitsMetrics-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Metrics/getMappingHitsMetrics'
```
