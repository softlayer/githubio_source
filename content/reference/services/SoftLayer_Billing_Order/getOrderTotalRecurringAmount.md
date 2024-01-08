---
title: "getOrderTotalRecurringAmount"
description: "An order's total recurring amount. This amount represents the fees that will be charged on a recurring (usually monthly) basis."
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

### [REST Example](#getOrderTotalRecurringAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrderTotalRecurringAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getOrderTotalRecurringAmount'
```
