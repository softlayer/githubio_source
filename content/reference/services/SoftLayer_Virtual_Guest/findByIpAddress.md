---
title: "findByIpAddress"
description: "Find CCI by only its primary public or private IP address. IP addresses within secondary subnets tied to the CCI will not return the CCI. If no CCI is found, no errors are generated and no data is returned. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

### [REST Example](#findByIpAddress-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#findByIpAddress-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/findByIpAddress'
```
