---
title: "getActiveUsageRatePrices"
description: "This method returns a collection of active usage rate [SoftLayer_Product_Item_Price](/reference/datatypes/SoftLayer_Product_Item_Price) objects for the current package and specified datacenter. Optionally you can retrieve the active usage rate prices for a particular [SoftLayer_Product_Item_Category](/reference/datatypes/SoftLayer_Product_Item_Category) by specifying a category code as the first parameter. This information is useful so that you can see 'pay as you go' rates (if any) for the current package, location and optionally category. "
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

### [REST Example](#getActiveUsageRatePrices-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getActiveUsageRatePrices-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getActiveUsageRatePrices'
```
