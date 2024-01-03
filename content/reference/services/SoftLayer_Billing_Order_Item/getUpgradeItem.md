---
title: "getUpgradeItem"
description: "The next SoftLayer_Product_Item in the upgrade path for this order item."
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

# [REST Example](#getUpgradeItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUpgradeItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getUpgradeItem'
```
