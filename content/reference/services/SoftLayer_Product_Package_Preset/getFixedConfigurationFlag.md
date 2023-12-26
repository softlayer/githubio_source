---
title: "getFixedConfigurationFlag"
description: "A package preset with this flag set will not allow the price's defined in the preset configuration to be overriden during order placement."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Preset"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Package_Preset"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package_Preset/{SoftLayer_Product_Package_PresetID}/getFixedConfigurationFlag'
```
