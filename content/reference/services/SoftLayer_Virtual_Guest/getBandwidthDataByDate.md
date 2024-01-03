---
title: "getBandwidthDataByDate"
description: "Use this method when needing the metric data for bandwidth for a single guest.  It will gather the correct input parameters based on the date ranges "
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

# [REST Example](#getBandwidthDataByDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBandwidthDataByDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getBandwidthDataByDate'
```
