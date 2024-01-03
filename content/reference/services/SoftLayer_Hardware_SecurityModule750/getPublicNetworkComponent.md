---
title: "getPublicNetworkComponent"
description: "Retrieve a SoftLayer server's public network component. Some servers are only connected to the private network and may not have a public network component. In that case getPublicNetworkComponent returns a null object. "
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

# [REST Example](#getPublicNetworkComponent-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPublicNetworkComponent-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getPublicNetworkComponent'
```
