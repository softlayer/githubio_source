---
title: "getDownstreamNetworkHardwareWithIncidents"
description: "All network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware. [DEPRECATED]"
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

### [REST Example](#getDownstreamNetworkHardwareWithIncidents-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDownstreamNetworkHardwareWithIncidents-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getDownstreamNetworkHardwareWithIncidents'
```
