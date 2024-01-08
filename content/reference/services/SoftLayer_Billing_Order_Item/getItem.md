---
title: "getItem"
description: "The SoftLayer_Product_Item tied to an order item. The item is the actual definition of the product being sold."
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

### [REST Example](#getItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getItem'
```
