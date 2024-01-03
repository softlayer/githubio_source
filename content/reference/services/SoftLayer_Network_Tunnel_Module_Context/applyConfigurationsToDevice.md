---
title: "applyConfigurationsToDevice"
description: "An asynchronous task will be created to apply the IPSec network tunnel's configuration to network devices. During this time, an IPSec network tunnel cannot be modified in anyway. Only one network tunnel configuration task can be created at a time. If a task has already been created and has not completed, a new task cannot be created. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Tunnel_Module_Context"
---

# [REST Example](#applyConfigurationsToDevice-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#applyConfigurationsToDevice-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/applyConfigurationsToDevice'
```
