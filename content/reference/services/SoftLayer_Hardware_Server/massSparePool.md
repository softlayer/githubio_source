---
title: "massSparePool"
description: "The ability to place multiple bare metal servers in a state where they are powered down and ports closed yet still allocated to the customer as a part of the Spare Pool program. "
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

# [REST Example](#massSparePool-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#massSparePool-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/massSparePool'
```
