---
title: "checkItemAvailability"
description: ""
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

### [REST Example](#checkItemAvailability-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#checkItemAvailability-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Product_Item_Price, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/checkItemAvailability'
```
