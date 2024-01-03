---
title: "checkItemConflicts"
description: "Check order items for conflicts"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Order"
---

# [REST Example](#checkItemConflicts-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#checkItemConflicts-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Product_Item_Price]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/checkItemConflicts'
```
