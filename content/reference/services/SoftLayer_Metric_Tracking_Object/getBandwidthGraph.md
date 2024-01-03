---
title: "getBandwidthGraph"
description: "Retrieve a PNG image of a bandwidth graph representing the bandwidth usage over time recorded by SofTLayer's bandwidth pollers. "
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

# [REST Example](#getBandwidthGraph-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBandwidthGraph-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string, int, int, int, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/{SoftLayer_Metric_Tracking_ObjectID}/getBandwidthGraph'
```
