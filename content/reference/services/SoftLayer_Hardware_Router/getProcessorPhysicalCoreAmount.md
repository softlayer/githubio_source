---
title: "getProcessorPhysicalCoreAmount"
description: "The total number of physical processor cores, summed from all processors that are attached to a piece of hardware"
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

# [REST Example](#getProcessorPhysicalCoreAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getProcessorPhysicalCoreAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getProcessorPhysicalCoreAmount'
```
