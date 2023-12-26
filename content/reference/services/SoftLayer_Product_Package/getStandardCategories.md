---
title: "getStandardCategories"
description: "This call is similar to [SoftLayer_Product_Package::getCategories](/reference/services/SoftLayer_Product_Package/getCategories), except that it does not include account-restricted pricing. Not all accounts have restricted pricing. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getStandardCategories'
```
