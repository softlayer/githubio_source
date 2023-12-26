---
title: "addL7Rules"
description: "This function creates and adds multiple Rules to a given L7 policy with all the details provided for rules "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Rule/addL7Rules'
```
