---
title: "getTopLevelCategories"
description: "This method returns a collection of computing categories. These categories are also top level items in a service offering. "
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

# [REST Example](#getTopLevelCategories-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTopLevelCategories-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Category/getTopLevelCategories'
```
