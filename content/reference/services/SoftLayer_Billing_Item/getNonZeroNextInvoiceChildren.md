---
title: "getNonZeroNextInvoiceChildren"
description: "A Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee."
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

### [REST Example](#getNonZeroNextInvoiceChildren-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNonZeroNextInvoiceChildren-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getNonZeroNextInvoiceChildren'
```
