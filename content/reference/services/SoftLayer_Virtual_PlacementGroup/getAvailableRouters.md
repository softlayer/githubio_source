---
title: "getAvailableRouters"
description: "Returns all routers available for use with placement groups. If a datacenter location ID is provided, this method will further restrict the list of routers to ones contained within that datacenter. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_PlacementGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_PlacementGroup"
---

# [REST Example](#getAvailableRouters-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAvailableRouters-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_PlacementGroup/getAvailableRouters'
```
