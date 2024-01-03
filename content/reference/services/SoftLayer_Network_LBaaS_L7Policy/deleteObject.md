---
title: "deleteObject"
description: "Deletes a l7 policy instance and the rules associated with the policy "
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

# [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Policy/{SoftLayer_Network_LBaaS_L7PolicyID}/deleteObject'
```
