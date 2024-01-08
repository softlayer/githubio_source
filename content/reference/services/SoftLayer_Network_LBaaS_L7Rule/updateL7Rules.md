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

### [REST Example](#updateL7Rules-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateL7Rules-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_L7Rule]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Rule/updateL7Rules'
```
