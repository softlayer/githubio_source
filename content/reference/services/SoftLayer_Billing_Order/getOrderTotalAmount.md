---
title: "getOrderTotalAmount"
description: "This amount represents the order's initial charge including set up fee and taxes."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order"
---

# [REST Example](#getOrderTotalAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrderTotalAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getOrderTotalAmount'
```
