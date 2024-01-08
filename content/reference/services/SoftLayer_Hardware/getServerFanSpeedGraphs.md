---
title: "getServerFanSpeedGraphs"
description: "The '''getServerFanSpeedGraphs''' method retrieves the server's fan speeds and displays the speeds using tachometer graphs. data used to construct these graphs is retrieved from the server's remote management card. Each graph returned will have an associated title. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware"
---

### [REST Example](#getServerFanSpeedGraphs-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServerFanSpeedGraphs-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/getServerFanSpeedGraphs'
```
