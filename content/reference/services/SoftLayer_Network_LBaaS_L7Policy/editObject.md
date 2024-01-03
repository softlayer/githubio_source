---
title: "editObject"
description: "Edit a l7 policy instance's properties "
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

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_LBaaS_L7Policy]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Policy/{SoftLayer_Network_LBaaS_L7PolicyID}/editObject'
```
