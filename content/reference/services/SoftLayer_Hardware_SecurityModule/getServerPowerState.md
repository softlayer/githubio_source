---
title: "getServerPowerState"
description: "Retrieves the power state for the server.  The server's power status is retrieved from its remote management card.  This will return 'on' or 'off'. "
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

### [REST Example](#getServerPowerState-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServerPowerState-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getServerPowerState'
```
