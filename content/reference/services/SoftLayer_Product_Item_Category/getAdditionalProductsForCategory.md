---
title: "getAdditionalProductsForCategory"
description: "Returns a list of of active Items in the 'Additional Services' package with their active prices for a given product item category and sorts them by price."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Category"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Item_Category"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Category/{SoftLayer_Product_Item_CategoryID}/getAdditionalProductsForCategory'
```
