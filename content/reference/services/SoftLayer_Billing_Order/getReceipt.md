---
title: "getReceipt"
description: "Generate a [SoftLayer_Container_Product_Order_Receipt](/reference/datatypes/SoftLayer_Container_Product_Order_Receipt) object with all the order information. "
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

### [REST Example](#getReceipt-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getReceipt-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getReceipt'
```
