---
title: "getCpuMetricDataByDate"
description: "Use this method when needing the metric data for a single guest's CPUs.  It will gather the correct input parameters based on the date ranges "
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

# [REST Example](#getCpuMetricDataByDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCpuMetricDataByDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getCpuMetricDataByDate'
```
