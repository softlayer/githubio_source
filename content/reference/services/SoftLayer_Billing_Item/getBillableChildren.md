---
title: "getBillableChildren"
description: "A billing item's recurring child items that have once been billed and are scheduled to be billed in the future."
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

# [REST Example](#getBillableChildren-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBillableChildren-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getBillableChildren'
```
