---
title: "getChildren"
description: "The child order items for an order item. All server order items should have children. These children are considered a part of the server."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Item"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getChildren'
```
