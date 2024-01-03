---
title: "getTotalRecurringAmount"
description: "The recurring fee of an ordered item. This amount represents the fees that will be charged on a recurring (usually monthly) basis."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Item"
---

# [REST Example](#getTotalRecurringAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTotalRecurringAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getTotalRecurringAmount'
```
