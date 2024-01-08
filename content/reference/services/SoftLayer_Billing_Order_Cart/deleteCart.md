---
title: "deleteCart"
description: "If a cart is no longer needed, it can be deleted using this service. Once a cart has been deleted, it cannot be retrieved again. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Cart"
---

### [REST Example](#deleteCart-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteCart-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Cart/{SoftLayer_Billing_Order_CartID}/deleteCart'
```
