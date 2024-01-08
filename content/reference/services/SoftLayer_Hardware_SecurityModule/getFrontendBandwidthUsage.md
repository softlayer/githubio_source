---
title: "getFrontendBandwidthUsage"
description: "Use this method to return an array of public bandwidth utilization records between a given date range. 

This method represents the NEW version of getFrontendBandwidthUse "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

### [REST Example](#getFrontendBandwidthUsage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFrontendBandwidthUsage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getFrontendBandwidthUsage'
```
