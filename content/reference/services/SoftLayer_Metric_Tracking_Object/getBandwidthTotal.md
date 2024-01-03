---
title: "getBandwidthTotal"
description: "Retrieve the total amount of bandwidth recorded by a tracking object within the given date range. This method will only work on SoftLayer_Metric_Tracking_Object for SoftLayer_Hardware objects, and SoftLayer_Virtual_Guest objects. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
type: "reference"
layout: "method"
mainService : "SoftLayer_Metric_Tracking_Object"
---

# [REST Example](#getBandwidthTotal-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBandwidthTotal-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/{SoftLayer_Metric_Tracking_ObjectID}/getBandwidthTotal'
```
