---
title: "getDedicatedHostsForImageTemplate"
description: "This returns a collection of dedicated hosts that are valid for a given image template. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#getDedicatedHostsForImageTemplate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDedicatedHostsForImageTemplate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getDedicatedHostsForImageTemplate'
```
