---
title: "findByPromoCode"
description: "Retrieves a promotion using its code."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Promotion"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Promotion"
---

### [REST Example](#findByPromoCode-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#findByPromoCode-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Promotion/findByPromoCode'
```
