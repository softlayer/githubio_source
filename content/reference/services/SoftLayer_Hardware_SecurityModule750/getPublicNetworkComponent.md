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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getPublicNetworkComponent'
```
