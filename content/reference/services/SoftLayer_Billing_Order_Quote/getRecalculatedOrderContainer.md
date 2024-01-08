---
title: "getRecalculatedOrderContainer"
description: "Generate an [SoftLayer_Container_Product_Order](/reference/datatypes/SoftLayer_Container_Product_Order) from the previously-created quote. This will take into account promotions, reseller status, estimated taxes and all other standard order verification processes. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Quote"
---

### [REST Example](#getRecalculatedOrderContainer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRecalculatedOrderContainer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Product_Order, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Quote/{SoftLayer_Billing_Order_QuoteID}/getRecalculatedOrderContainer'
```
