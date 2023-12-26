---
title: "getSensorData"
description: "The '''getSensorData''' method retrieves a server's hardware state via its internal sensors. Remote sensor data is transmitted to the SoftLayer API by way of the server's remote management card. Sensor data measures various information, including system temperatures, voltages and other local server settings. Sensor data is cached for 30 second; calls made to this method for the same server within 30 seconds of each other will result in the same data being returned. To ensure that the data retrieved retrieves snapshot of varied data, make calls greater than 30 seconds apart. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/getSensorData'
```
