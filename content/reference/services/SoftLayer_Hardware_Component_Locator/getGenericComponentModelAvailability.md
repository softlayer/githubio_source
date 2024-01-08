---
title: "getGenericComponentModelAvailability"
description: "An API to retrieve Generic Components Model availability at data centers"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Locator"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Component_Locator"
---

### [REST Example](#getGenericComponentModelAvailability-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getGenericComponentModelAvailability-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Component_Locator/getGenericComponentModelAvailability'
```
