---
title: "getAssociatedChildren"
description: "A Billing Item's associated child billing items. This includes 'floating' items that are not necessarily child billing items of this billing item."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---

### [REST Example](#getAssociatedChildren-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAssociatedChildren-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Virtual_DedicatedHost/{SoftLayer_Billing_Item_Virtual_DedicatedHostID}/getAssociatedChildren'
```
