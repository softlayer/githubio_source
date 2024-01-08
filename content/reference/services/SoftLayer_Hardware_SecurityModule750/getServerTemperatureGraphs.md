---
title: "getServerTemperatureGraphs"
description: "Retrieve the server's temperature and displays them using thermometer graphs.  Temperatures retrieved are CPU(s) and system temperatures.  Data used to construct graphs is retrieved from the server's remote management card.  All graphs returned will have a title associated with it. "
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

### [REST Example](#getServerTemperatureGraphs-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServerTemperatureGraphs-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getServerTemperatureGraphs'
```
