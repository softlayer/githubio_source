---
title: "getItemPrice"
description: "The SoftLayer_Product_Item_Price tied to an order item. The item price object describes the cost of an item."
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

### [REST Example](#getItemPrice-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getItemPrice-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getItemPrice'
```
