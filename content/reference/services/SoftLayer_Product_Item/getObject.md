---
title: "getObject"
description: "Product Items are the products SoftLayer sells. Items have many properties that help describe what each is for. Each product items holds within it a description, tax rate information, status, and upgrade downgrade path information. "
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

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item/{SoftLayer_Product_ItemID}/getObject'
```
