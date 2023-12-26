---
title: "getAssociatedChildren"
description: "A Billing Item's associated child billing items. This includes 'floating' items that are not necessarily child billing items of this billing item."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Chronicle"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Chronicle"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Chronicle/{SoftLayer_Billing_Item_ChronicleID}/getAssociatedChildren'
```
