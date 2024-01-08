---
title: "getItemPricesFromSoftwareDescriptions"
description: "Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description "
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

### [REST Example](#getItemPricesFromSoftwareDescriptions-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getItemPricesFromSoftwareDescriptions-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Software_Description, boolean, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getItemPricesFromSoftwareDescriptions'
```
