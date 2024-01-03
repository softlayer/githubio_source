---
title: "getPublicBandwidthData"
description: "Retrieve a graph of a server's public network bandwidth usage over the specified timeframe. If no timeframe is specified then getPublicBandwidthGraphImage retrieves the last 24 hours of public bandwidth usage. getPublicBandwidthGraphImage returns a PNG image measuring 827 pixels by 293 pixels. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

# [REST Example](#getPublicBandwidthData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPublicBandwidthData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getPublicBandwidthData'
```
