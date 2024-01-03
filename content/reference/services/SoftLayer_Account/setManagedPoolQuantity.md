---
title: "setManagedPoolQuantity"
description: "Set the total number of servers that are to be maintained in the given pool. When a server is ordered a new server will be put in the pool to replace the server that was removed to fill an order to maintain the desired pool availability quantity. "
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

# [REST Example](#setManagedPoolQuantity-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setManagedPoolQuantity-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/setManagedPoolQuantity'
```
