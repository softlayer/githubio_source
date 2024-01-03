---
title: "getUsageMetricImageByDate"
description: "Returns a disk usage image based on disk usage specified by the input parameters. "
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

# [REST Example](#getUsageMetricImageByDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUsageMetricImageByDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Storage_Repository/{SoftLayer_Virtual_Storage_RepositoryID}/getUsageMetricImageByDate'
```
