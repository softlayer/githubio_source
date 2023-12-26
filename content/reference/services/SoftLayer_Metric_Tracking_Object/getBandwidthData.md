---
title: "getBandwidthData"
description: "Retrieve a collection of raw bandwidth data from an individual public or private network tracking object. Raw data is ideal if you with to employ your own traffic storage and graphing systems. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/{SoftLayer_Metric_Tracking_ObjectID}/getBandwidthData'
```
