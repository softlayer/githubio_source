---
title: "getParentVirtualGuestBillingItem"
description: "A billing item's parent item. If a billing item has no parent item then this value is null."
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

### [REST Example](#getParentVirtualGuestBillingItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getParentVirtualGuestBillingItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getParentVirtualGuestBillingItem'
```
