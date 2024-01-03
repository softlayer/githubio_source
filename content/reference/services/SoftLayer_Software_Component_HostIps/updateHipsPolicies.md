---
title: "updateHipsPolicies"
description: "Update the Host IPS policies. To retrieve valid policy options you must use the provided relationships. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_HostIps"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component_HostIps"
---

# [REST Example](#updateHipsPolicies-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateHipsPolicies-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, string, string, string, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component_HostIps/{SoftLayer_Software_Component_HostIpsID}/updateHipsPolicies'
```
