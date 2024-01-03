---
title: "createObjects"
description: "Create multiple domains on the SoftLayer name servers. Each domain record passed to ''createObjects'' follows the logic in the SoftLayer_Dns_Domain ''createObject'' method. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain"
---

# [REST Example](#createObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/createObjects'
```
