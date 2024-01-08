---
title: "getHourlyFlag"
description: "A flag that will reflect whether this billing item is billed on an hourly basis or not."
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

### [REST Example](#getHourlyFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getHourlyFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getHourlyFlag'
```
