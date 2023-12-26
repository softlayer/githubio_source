---
title: "findByIpAddress"
description: "The '''findByIpAddress''' method finds hardware using its primary public or private IP address. IP addresses that have a secondary subnet tied to the hardware will not return the hardware. If no hardware is found, no errors are generated and no data is returned. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/findByIpAddress'
```
