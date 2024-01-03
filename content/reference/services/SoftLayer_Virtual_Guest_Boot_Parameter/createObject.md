---
title: "createObject"
description: "Create a boot parameter record to be used at next boot"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Boot_Parameter"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest_Boot_Parameter"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_Guest_Boot_Parameter]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Boot_Parameter/createObject'
```
