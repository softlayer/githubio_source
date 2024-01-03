---
title: "validatePartitionsForOperatingSystem"
description: "Validates a collection of partitions for an operating system"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

# [REST Example](#validatePartitionsForOperatingSystem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validatePartitionsForOperatingSystem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Software_Description, SoftLayer_Hardware_Component_Partition]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/validatePartitionsForOperatingSystem'
```
