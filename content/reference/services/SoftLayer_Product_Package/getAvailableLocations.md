---
title: "getAvailableLocations"
description: "A collection of valid locations for this package. (Deprecated - Use [SoftLayer_Product_Package::getRegions](/reference/services/SoftLayer_Product_Package/getRegions))"
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

### [REST Example](#getAvailableLocations-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAvailableLocations-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getAvailableLocations'
```
