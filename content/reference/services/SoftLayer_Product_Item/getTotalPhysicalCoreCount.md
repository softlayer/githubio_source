---
title: "getTotalPhysicalCoreCount"
description: "Shows the total number of cores. This is deprecated. Use [SoftLayer_Product_Item::getCapacity](/reference/services/SoftLayer_Product_Item/getCapacity) for guest_core products and [SoftLayer_Product_Item::getTotalPhysicalCoreCapacity](/reference/services/SoftLayer_Product_Item/getTotalPhysicalCoreCapacity) for server products"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Item"
---

# [REST Example](#getTotalPhysicalCoreCount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTotalPhysicalCoreCount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item/{SoftLayer_Product_ItemID}/getTotalPhysicalCoreCount'
```
