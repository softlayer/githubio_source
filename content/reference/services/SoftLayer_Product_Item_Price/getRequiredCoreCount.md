---
title: "getRequiredCoreCount"
description: "The number of server cores required to order this item. This is deprecated. Use [SoftLayer_Product_Item_Price::getCapacityRestrictionMinimum](/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMinimum) and [SoftLayer_Product_Item_Price::getCapacityRestrictionMaximum](/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMaximum)"
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

# [REST Example](#getRequiredCoreCount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRequiredCoreCount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Price/{SoftLayer_Product_Item_PriceID}/getRequiredCoreCount'
```
