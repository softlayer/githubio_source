---
title: "approveModifiedOrder"
description: "When an order has been modified, the customer will need to approve the changes. This method will allow the customer to approve the changes. "
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

### [REST Example](#approveModifiedOrder-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#approveModifiedOrder-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/approveModifiedOrder'
```
