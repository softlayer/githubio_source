---
title: "getMappingIntegratedMetrics"
description: "Get the integrated metrics data for the given mapping. You can get the the hits, bandwidth, hits by type and bandwidth by region. It will return both the total data and the detail data. "
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

### [REST Example](#getMappingIntegratedMetrics-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMappingIntegratedMetrics-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Metrics/getMappingIntegratedMetrics'
```
