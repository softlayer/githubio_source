---
title: "getAssociatedChildren"
description: "An Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice_Item/{SoftLayer_Billing_Invoice_ItemID}/getAssociatedChildren'
```
