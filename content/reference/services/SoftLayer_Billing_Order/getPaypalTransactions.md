---
title: "getPaypalTransactions"
description: "All PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty."
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

### [REST Example](#getPaypalTransactions-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPaypalTransactions-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getPaypalTransactions'
```
