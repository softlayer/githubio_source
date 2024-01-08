---
title: "editObject"
description: "Update a placement group. "
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

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_PlacementGroup]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_PlacementGroup/{SoftLayer_Virtual_PlacementGroupID}/editObject'
```
