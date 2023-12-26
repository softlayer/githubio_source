---
title: "getBandwidthImage"
description: "Use this method when needing a bandwidth image for a single server.  It will gather the correct input parameters for the generic graphing utility automatically based on the snapshot specified.  Use the $draw flag to suppress the generation of the actual binary PNG image. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule750"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [enum, enum, boolean, dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getBandwidthImage'
```
