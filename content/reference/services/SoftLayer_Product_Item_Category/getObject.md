---
title: "getObject"
description: "Each product item price must be tied to a category for it to be sold. These categories describe how a particular product item is sold. For example, the 250GB hard drive can be sold as disk0, disk1, ... disk11. There are different prices for this product item depending on which category it is. This keeps down the number of products in total. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Category/{SoftLayer_Product_Item_CategoryID}/getObject'
```
