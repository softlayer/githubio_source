---
title: "getCreditCardTransactions"
description: "All credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty."
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

# [REST Example](#getCreditCardTransactions-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCreditCardTransactions-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getCreditCardTransactions'
```
