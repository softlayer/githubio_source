---
title: "getRedfishPowerState"
description: "Retrieves the power state for the server.  The server's power status is retrieved from its remote management card.  This will return 'on' or 'off'. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule750"
---

### [REST Example](#getRedfishPowerState-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRedfishPowerState-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getRedfishPowerState'
```
