---
title: "getSanStorageCapabilityFlag"
description: "A flag indicating that a VLAN on the router can be assigned to a host that has SAN disk functionality."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

### [REST Example](#getSanStorageCapabilityFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSanStorageCapabilityFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getSanStorageCapabilityFlag'
```
