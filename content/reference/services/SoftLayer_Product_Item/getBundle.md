---
title: "getBundle"
description: "An item's included product item references. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item_Bundles objects. See the SoftLayer_Product_Item::bundleItems property for bundle of SoftLayer_Product_Item of objects."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Item/{SoftLayer_Product_ItemID}/getBundle'
```
