---
title: "getBandwidthForDateRange"
description: "Retrieve a collection of bandwidth data from an individual public or private network tracking object. Data is ideal if you with to employ your own traffic storage and graphing systems. "
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

# [REST Example](#getBandwidthForDateRange-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBandwidthForDateRange-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getBandwidthForDateRange'
```
