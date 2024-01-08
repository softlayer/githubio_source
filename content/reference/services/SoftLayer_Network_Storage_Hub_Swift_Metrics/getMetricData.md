---
title: "getMetricData"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Hub_Swift_Metrics"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Hub_Swift_Metrics"
---

### [REST Example](#getMetricData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMetricData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Hub_Swift_Metrics/{SoftLayer_Network_Storage_Hub_Swift_MetricsID}/getMetricData'
```
