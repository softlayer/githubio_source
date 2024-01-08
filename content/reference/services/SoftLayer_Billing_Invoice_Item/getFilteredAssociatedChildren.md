---
title: "getFilteredAssociatedChildren"
description: "An Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Invoice_Item"
---

### [REST Example](#getFilteredAssociatedChildren-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFilteredAssociatedChildren-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice_Item/{SoftLayer_Billing_Invoice_ItemID}/getFilteredAssociatedChildren'
```
