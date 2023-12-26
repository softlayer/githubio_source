---
title: "getRecalculatedOrderContainer"
description: "Generate an [SoftLayer_Container_Product_Order](/reference/datatypes/SoftLayer_Container_Product_Order) from a billing order. This will take into account promotions, reseller status, estimated taxes and all other standard order verification processes. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getRecalculatedOrderContainer'
```
