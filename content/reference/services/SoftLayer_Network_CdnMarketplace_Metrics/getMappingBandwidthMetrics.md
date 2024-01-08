---
title: "getMappingBandwidthMetrics"
description: "Get the amount of edge hits for an individual mapping. "
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

### [REST Example](#getMappingBandwidthMetrics-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMappingBandwidthMetrics-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Metrics/getMappingBandwidthMetrics'
```
