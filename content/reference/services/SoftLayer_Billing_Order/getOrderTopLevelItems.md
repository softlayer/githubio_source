---
title: "getOrderTopLevelItems"
description: "An order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI."
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

# [REST Example](#getOrderTopLevelItems-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrderTopLevelItems-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getOrderTopLevelItems'
```
