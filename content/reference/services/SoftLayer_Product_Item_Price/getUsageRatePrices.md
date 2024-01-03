---
title: "getUsageRatePrices"
description: "Returns a collection of rate-based [SoftLayer_Product_Item_Price](/reference/datatypes/SoftLayer_Product_Item_Price) objects associated with the [SoftLayer_Product_Item](/reference/datatypes/SoftLayer_Product_Item) objects and the [SoftLayer_Location](/reference/datatypes/SoftLayer_Location) specified. The location is required to get the appropriate rate-based prices because the usage rates may vary from datacenter to datacenter. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Price"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Item_Price"
---

# [REST Example](#getUsageRatePrices-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUsageRatePrices-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Location, SoftLayer_Product_Item]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item_Price/getUsageRatePrices'
```
