---
title: "addL7Policies"
description: "This function creates multiple policies with rules for the given listener. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Policy"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_L7Policy"
---

### [REST Example](#addL7Policies-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addL7Policies-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_PolicyRule]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Policy/addL7Policies'
```
