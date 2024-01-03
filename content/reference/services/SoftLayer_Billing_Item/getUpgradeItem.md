---
title: "getUpgradeItem"
description: "Billing items whose product item has an upgrade path defined in our system will return the next product item in the upgrade path."
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

# [REST Example](#getUpgradeItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUpgradeItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getUpgradeItem'
```
