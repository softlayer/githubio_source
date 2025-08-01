---
title: "getPublicBandwidthData"
description: "Retrieve this server's public bandwidth data. If no timeframe is specified then getPublicBandwidthData retrieves the last 24 hours of public bandwidth usage. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

### [REST Example](#getPublicBandwidthData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPublicBandwidthData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getPublicBandwidthData'
```
