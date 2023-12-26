---
title: "getSensorDataWithGraphs"
description: "The '''getSensorDataWithGraphs''' method retrieves the raw data returned from the server's remote management card. Along with raw data, graphs for the CPU and system temperatures and fan speeds are also returned. For more details on what information is returned, refer to the ''getSensorData'' method. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getSensorDataWithGraphs'
```
