---
title: "getCoreRestrictedItemFlag"
description: "This flag indicates that this product is restricted by the number of cores on the compute instance. This is deprecated. Use [SoftLayer_Product_Item::getCapacityRestrictedProductFlag](/reference/services/SoftLayer_Product_Item/getCapacityRestrictedProductFlag)"
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

### [REST Example](#getCoreRestrictedItemFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCoreRestrictedItemFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item/{SoftLayer_Product_ItemID}/getCoreRestrictedItemFlag'
```
