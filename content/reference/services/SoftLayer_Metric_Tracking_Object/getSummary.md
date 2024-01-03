---
title: "getSummary"
description: "Retrieve a metric summary. Ideal if you want to employ your own graphing systems.  Note not all metric types contain a summary.  These return null. "
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

# [REST Example](#getSummary-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSummary-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/{SoftLayer_Metric_Tracking_ObjectID}/getSummary'
```
