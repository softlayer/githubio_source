---
title: "getPricingLocationGroup"
description: "The pricing location group that this price is applicable for. Prices that have a pricing location group will only be available for ordering with the locations specified on the location group."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Price"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Item_Price"
---

### [REST Example](#getPricingLocationGroup-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPricingLocationGroup-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Price/{SoftLayer_Product_Item_PriceID}/getPricingLocationGroup'
```
