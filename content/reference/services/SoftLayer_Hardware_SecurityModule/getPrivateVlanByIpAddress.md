---
title: "getPrivateVlanByIpAddress"
description: "
*** DEPRECATED ***
Retrieve a backend network VLAN by searching for an IP address "
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

### [REST Example](#getPrivateVlanByIpAddress-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPrivateVlanByIpAddress-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/getPrivateVlanByIpAddress'
```
