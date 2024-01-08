---
title: "getDisallowedComputeGroupUpgradeFlag"
description: "When true this preset is only allowed to upgrade/downgrade to other presets in the same compute family."
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

### [REST Example](#getDisallowedComputeGroupUpgradeFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDisallowedComputeGroupUpgradeFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package_Preset/{SoftLayer_Product_Package_PresetID}/getDisallowedComputeGroupUpgradeFlag'
```
