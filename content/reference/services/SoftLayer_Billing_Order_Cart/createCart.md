---
title: "createCart"
description: "When creating a new cart, the order data is sent through SoftLayer_Product_Order::verifyOrder to make sure that the cart contains valid data. If an issue is found with the order, an exception will be thrown and you will receive the same response as if SoftLayer_Product_Order::verifyOrder were called directly. Once the order verification is complete, the cart will be created. 

The response is the new cart id. "
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
