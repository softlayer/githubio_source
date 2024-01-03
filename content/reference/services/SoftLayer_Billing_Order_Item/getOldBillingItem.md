---
title: "getOldBillingItem"
description: "This is only populated when an upgrade order is placed. The old billing item represents what the billing was before the upgrade happened."
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

# [REST Example](#getOldBillingItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOldBillingItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getOldBillingItem'
```
