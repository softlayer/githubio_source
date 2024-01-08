---
title: "getPrivateBandwidthData"
description: "Retrieve a graph of a server's private network bandwidth usage over the specified timeframe. If no timeframe is specified then getPublicBandwidthGraphImage retrieves the last 24 hours of public bandwidth usage. getPrivateBandwidthGraphImage returns a PNG image measuring 827 pixels by 293 pixels. "
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

### [REST Example](#getPrivateBandwidthData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPrivateBandwidthData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getPrivateBandwidthData'
```
