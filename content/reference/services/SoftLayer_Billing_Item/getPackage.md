---
title: "getPackage"
description: "The package under which this billing item was sold. A Package is the general grouping of products as seen on our order forms."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item"
---

# [REST Example](#getPackage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPackage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getPackage'
```
