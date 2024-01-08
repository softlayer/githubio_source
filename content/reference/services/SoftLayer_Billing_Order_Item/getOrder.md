---
title: "getOrder"
description: "The order to which this item belongs. The order contains all the information related to the items included in an order"
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

### [REST Example](#getOrder-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrder-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getOrder'
```
