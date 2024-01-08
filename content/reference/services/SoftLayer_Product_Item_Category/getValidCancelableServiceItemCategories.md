---
title: "getValidCancelableServiceItemCategories"
description: "This method returns service product categories that can be canceled via API.  You can use these categories to find the billing items you wish to cancel. "
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

### [REST Example](#getValidCancelableServiceItemCategories-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getValidCancelableServiceItemCategories-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Category/getValidCancelableServiceItemCategories'
```
