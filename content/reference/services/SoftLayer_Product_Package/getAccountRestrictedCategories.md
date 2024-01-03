---
title: "getAccountRestrictedCategories"
description: "The results from this call are similar to [SoftLayer_Product_Package::getCategories](/reference/services/SoftLayer_Product_Package/getCategories), but these ONLY include account-restricted prices. Not all accounts have restricted pricing."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Package"
---

# [REST Example](#getAccountRestrictedCategories-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAccountRestrictedCategories-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getAccountRestrictedCategories'
```
