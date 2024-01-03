---
title: "createObject"
description: "Create a allotment for servers to pool bandwidth and avoid overages in billing if they use more than there allocated bandwidth. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Bandwidth_Version1_Allotment"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Bandwidth_Version1_Allotment]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject'
```
