---
title: "isWindowsServer"
description: "Determine if the server runs any version of the Microsoft Windows operating systems. Return ''true'' if it does and ''false if otherwise. "
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

### [REST Example](#isWindowsServer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isWindowsServer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/isWindowsServer'
```
