---
title: "getMemoryMetricImage"
description: "Use this method when needing a memory usage image for a single guest.  It will gather the correct input parameters for the generic graphing utility automatically based on the snapshot specified. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#getMemoryMetricImage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMemoryMetricImage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [enum, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getMemoryMetricImage'
```
