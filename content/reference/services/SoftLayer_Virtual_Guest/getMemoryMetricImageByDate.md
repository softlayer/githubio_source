---
title: "getMemoryMetricImageByDate"
description: "Use this method when needing a image displaying the amount of memory used over time for a single computing instance. It will gather the correct input parameters for the generic graphing utility based on the date ranges "
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

### [REST Example](#getMemoryMetricImageByDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMemoryMetricImageByDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getMemoryMetricImageByDate'
```
