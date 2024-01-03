---
title: "getObject"
description: "Each product item category must be tied to a category group. These category groups describe how a particular product item category is categorized. For example, the disk0, disk1, ... disk11 can be categorized as Server and Attached Services. There are different groups for each of this product item category depending on the function of the item product in the subject category. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Category_Group"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Item_Category_Group"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Category_Group/{SoftLayer_Product_Item_Category_GroupID}/getObject'
```
