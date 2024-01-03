---
title: "getRecalculatedOrderContainer"
description: "This method allows the customer to retrieve a saved cart and put it in a format that's suitable to be sent to SoftLayer_Billing_Order_Cart::createCart to create a new cart or to SoftLayer_Billing_Order_Cart::updateCart to update an existing cart. "
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

# [REST Example](#getRecalculatedOrderContainer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRecalculatedOrderContainer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Product_Order, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Cart/{SoftLayer_Billing_Order_CartID}/getRecalculatedOrderContainer'
```
