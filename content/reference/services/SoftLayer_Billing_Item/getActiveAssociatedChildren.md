---
title: "getActiveAssociatedChildren"
description: "A billing item's active associated child billing items. This includes 'floating' items that are not necessarily child items of this billing item."
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

# [REST Example](#getActiveAssociatedChildren-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getActiveAssociatedChildren-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getActiveAssociatedChildren'
```
