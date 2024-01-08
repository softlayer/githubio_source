---
title: "cancelService"
description: "Cancel the resource or service (excluding bare metal servers) for a billing Item. The billing item will be cancelled immediately and reclaim of the resource will begin shortly. "
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

### [REST Example](#cancelService-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#cancelService-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/cancelService'
```
