---
title: "updateL7Rules"
description: "This function updates multiple Rules to a given policy with all the details for rules. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Rule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_L7Rule"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_L7Rule]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Rule/updateL7Rules'
```
