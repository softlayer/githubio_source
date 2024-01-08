---
title: "getBandwidthImage"
description: "Use this method when needing a bandwidth image for a single server.  It will gather the correct input parameters for the generic graphing utility automatically based on the snapshot specified.  Use the $draw flag to suppress the generation of the actual binary PNG image. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

### [REST Example](#getBandwidthImage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBandwidthImage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [enum, enum, boolean, dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getBandwidthImage'
```
