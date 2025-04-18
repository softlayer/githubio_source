---
title: "getPublicBandwidthData"
description: "Retrieve this server's public bandwidth data. If no timeframe is specified then getPublicBandwidthData retrieves the last 24 hours of public bandwidth usage. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule750"
---

### [REST Example](#getPublicBandwidthData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPublicBandwidthData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getPublicBandwidthData'
```
