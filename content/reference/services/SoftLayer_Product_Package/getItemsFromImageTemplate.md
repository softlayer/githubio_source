---
title: "getItemsFromImageTemplate"
description: "Return a collection of [SoftLayer_Product_Item](/reference/datatypes/SoftLayer_Product_Item) objects from a [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group) object"
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

### [REST Example](#getItemsFromImageTemplate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getItemsFromImageTemplate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_Guest_Block_Device_Template_Group]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getItemsFromImageTemplate'
```
