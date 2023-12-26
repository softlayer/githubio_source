---
title: "nsLookup"
description: "A method used to return the nameserver information for a given address"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Utility"
classes:
    - "SoftLayer_Utility_Network"
type: "reference"
layout: "method"
mainService : "SoftLayer_Utility_Network"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Utility_Network/nsLookup'
```
