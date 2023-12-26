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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/createObjects'
```
