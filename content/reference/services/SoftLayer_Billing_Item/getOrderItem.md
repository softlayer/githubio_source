---
title: "getOrderItem"
description: "A billing item's original order item. Simply a reference to the original order from which this billing item was created."
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

### [REST Example](#getOrderItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrderItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getOrderItem'
```
