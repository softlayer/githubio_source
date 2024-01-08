---
title: "isBackendPingable"
description: "Issues a ping command and returns the success (true) or failure (false) of the ping command. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

### [REST Example](#isBackendPingable-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isBackendPingable-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/isBackendPingable'
```
