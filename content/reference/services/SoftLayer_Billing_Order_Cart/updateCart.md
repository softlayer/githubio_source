---
title: "updateCart"
description: "Like SoftLayer_Billing_Order_Cart::createCart, the order data will be sent through SoftLayer_Product_Order::verifyOrder to make sure that the updated cart information is valid. Once it has been verified, the new order data will be saved. 

This will return the cart id. "
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

# [REST Example](#updateCart-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateCart-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Product_Order]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Cart/{SoftLayer_Billing_Order_CartID}/updateCart'
```
