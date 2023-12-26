---
title: "getInvoiceTotalOneTimeAmount"
description: "The total one-time charges for this invoice. This is the sum of one-time charges + setup fees + labor fees. This does not include taxes."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Invoice"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/{SoftLayer_Billing_InvoiceID}/getInvoiceTotalOneTimeAmount'
```
