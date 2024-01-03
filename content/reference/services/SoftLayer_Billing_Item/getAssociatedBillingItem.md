---
title: "getAssociatedBillingItem"
description: "A billing item's associated parent. This is to be used for billing items that are 'floating', and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item"
---

# [REST Example](#getAssociatedBillingItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAssociatedBillingItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getAssociatedBillingItem'
```
