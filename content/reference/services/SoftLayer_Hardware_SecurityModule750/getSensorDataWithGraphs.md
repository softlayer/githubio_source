---
title: "getSensorDataWithGraphs"
description: "Retrieves the raw data returned from the server's remote management card.  For more details of what is returned please refer to the getSensorData method.  Along with the raw data, graphs for the cpu and system temperatures and fan speeds are also returned. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getSensorDataWithGraphs'
```
