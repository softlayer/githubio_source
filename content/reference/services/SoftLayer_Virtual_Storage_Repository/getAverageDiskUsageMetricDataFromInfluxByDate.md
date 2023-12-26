---
title: "getAverageDiskUsageMetricDataFromInfluxByDate"
description: "Returns the average disk space usage for a storage repository. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Storage_Repository"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Storage_Repository/{SoftLayer_Virtual_Storage_RepositoryID}/getAverageDiskUsageMetricDataFromInfluxByDate'
```
