---
title: "getOccupiedInstances"
description: "The instances already occupied by a guest on this reserved capacity group."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_ReservedCapacityGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_ReservedCapacityGroup"
---

# [REST Example](#getOccupiedInstances-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOccupiedInstances-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_ReservedCapacityGroup/{SoftLayer_Virtual_ReservedCapacityGroupID}/getOccupiedInstances'
```
