---
title: "restBrandwindthGraph.txt"
description: "restBrandwindthGraph.txt"
date: "2017-11-23"
classes: 
    - "SoftLayer_Metric_Tracking_Object"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
********* TO GET the metrict tracking object ************

URL: https://$USERNAME:$APIKEY@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/$ServerID/getMetricTrackingObject.json
Method: Get

********* TO GET the graph ************
URL : https://$USERNAME:$APIKEY@api.softlayer.com/rest/v3/SoftLayer_Metric_Tracking_Object/$MetricTrackingID/getBandwidthGraph.json

Method: POST

JSON: {
    "parameters": [
        "2010-10-1T21:32:52",
        "2014-8-27T21:32:52",
        "public",
        8,
        827,
        273,
        true
    ]
}
```
