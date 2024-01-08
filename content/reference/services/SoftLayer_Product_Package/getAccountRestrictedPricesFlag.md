---
title: "getAccountRestrictedPricesFlag"
description: "The flag to indicate if there are any restricted prices in a package for the currently-active account."
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

### [REST Example](#getAccountRestrictedPricesFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAccountRestrictedPricesFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getAccountRestrictedPricesFlag'
```
