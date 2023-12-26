---
title: "getTaxInfoHistory"
description: "This is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information."
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/{SoftLayer_Billing_InvoiceID}/getTaxInfoHistory'
```
