---
title: "migrateDedicatedHost"
description: "Create a transaction to migrate an instance from one dedicated host to another dedicated host "
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

### [REST Example](#migrateDedicatedHost-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#migrateDedicatedHost-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/migrateDedicatedHost'
```
