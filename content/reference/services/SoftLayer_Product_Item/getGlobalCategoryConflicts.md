---
title: "getGlobalCategoryConflicts"
description: "An item's category conflicts. For example, 10 Gbps redundant network functionality cannot be ordered with a secondary GPU and as such is a conflict."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item/{SoftLayer_Product_ItemID}/getGlobalCategoryConflicts'
```
