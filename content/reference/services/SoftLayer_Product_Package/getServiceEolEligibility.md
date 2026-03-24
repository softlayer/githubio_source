---
title: "getServiceEolEligibility"
description: "See [SoftLayer_Product_Package::getServiceEolEligibilityOrderTypes](/reference/services/SoftLayer_Product_Package/getServiceEolEligibilityOrderTypes) for the order type values available. 

Some packages may also require a resource type. See [SoftLayer_Product_Package::getServiceEolEligibilityResourceTypes](/reference/services/SoftLayer_Product_Package/getServiceEolEligibilityResourceTypes) for the values available. "
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

### [REST Example](#getServiceEolEligibility-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServiceEolEligibility-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getServiceEolEligibility'
```
