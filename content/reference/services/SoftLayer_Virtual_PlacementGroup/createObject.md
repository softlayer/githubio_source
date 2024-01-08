---
title: "createObject"
description: "Add a placement group to your account for use during VSI provisioning. "
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

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_PlacementGroup]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_PlacementGroup/createObject'
```
