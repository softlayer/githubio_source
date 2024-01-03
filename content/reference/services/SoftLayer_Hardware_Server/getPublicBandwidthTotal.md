---
title: "getPublicBandwidthTotal"
description: "Retrieve the total number of bytes used by a server over a specified time period via the data warehouse tracking objects for this hardware. "
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

# [REST Example](#getPublicBandwidthTotal-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPublicBandwidthTotal-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getPublicBandwidthTotal'
```
