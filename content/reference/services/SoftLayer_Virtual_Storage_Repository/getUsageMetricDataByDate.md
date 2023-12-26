---
title: "getUsageMetricDataByDate"
description: "Retrieve disk usage data on a [SoftLayer_Virtual_Guest](/reference/datatypes/SoftLayer_Virtual_Guest) image for the time range you provide.  Each data entry objects contain ''dateTime'' and ''counter'' properties. ''dateTime'' property indicates the time that the disk usage data was measured and ''counter'' property holds the disk usage in bytes. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Storage_Repository/{SoftLayer_Virtual_Storage_RepositoryID}/getUsageMetricDataByDate'
```
