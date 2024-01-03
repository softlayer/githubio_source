---
title: "getDetailsForDateRange"
description: "Retrieve a collection of detailed metric data over a date range. Ideal if you want to employ your own graphing systems.  Note not all metrics support this method.  Those that do not return null. "
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

# [REST Example](#getDetailsForDateRange-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDetailsForDateRange-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/{SoftLayer_Metric_Tracking_ObjectID}/getDetailsForDateRange'
```
