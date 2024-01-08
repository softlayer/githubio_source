---
title: "editObject"
description: "Edit a dedicated host's properties. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_DedicatedHost"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_DedicatedHost"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_DedicatedHost]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_DedicatedHost/{SoftLayer_Virtual_DedicatedHostID}/editObject'
```
