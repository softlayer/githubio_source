---
title: "getDowngradeItems"
description: "For product items which have a downgrade path defined, this will return those product items."
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

### [REST Example](#getDowngradeItems-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDowngradeItems-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getDowngradeItems'
```
