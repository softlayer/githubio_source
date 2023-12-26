---
title: "findByCommonName"
description: "Locate certificates by their common name, traditionally a domain name. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Certificate"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate/findByCommonName'
```
