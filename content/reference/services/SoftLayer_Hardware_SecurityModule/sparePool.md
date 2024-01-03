---
title: "sparePool"
description: "The ability to place bare metal servers in a state where they are powered down, and ports closed yet still allocated to the customer as a part of the Spare Pool program. "
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

# [REST Example](#sparePool-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#sparePool-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/sparePool'
```
