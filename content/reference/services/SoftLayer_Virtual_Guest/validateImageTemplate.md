---
title: "validateImageTemplate"
description: "Validate an image template for OS Reload "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#validateImageTemplate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validateImageTemplate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/validateImageTemplate'
```
