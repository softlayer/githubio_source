---
title: "getAveragePublicUsageMetricDataByDate"
description: "Returns the average disk space usage for all public repositories. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#getAveragePublicUsageMetricDataByDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAveragePublicUsageMetricDataByDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getAveragePublicUsageMetricDataByDate'
```
