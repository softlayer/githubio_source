---
title: "createObjects"
description: "Create multiple secondary DNS records. Each record passed to ''createObjects'' follows the logic in the SoftLayer_Dns_Secondary [SoftLayer_Dns_Secondary::createObject](/reference/datatypes/$1/#$2) method. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Secondary"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Secondary]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/createObjects'
```
