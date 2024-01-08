---
title: "getSensorData"
description: "Retrieve a server's hardware state via its internal sensors. Remote sensor data is transmitted to the SoftLayer API by way of the server's remote management card. Sensor data measures system temperatures, voltages, and other local server settings. Sensor data is cached for 30 seconds. Calls made to getSensorData for the same server within 30 seconds of each other will return the same data. Subsequent calls will return new data once the cache expires. "
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

### [REST Example](#getSensorData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSensorData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getSensorData'
```
