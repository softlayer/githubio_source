---
title: "getInvoiceTotalOneTimeTaxAmount"
description: "A sum of all the taxes related to one time charges for this invoice."
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

# [REST Example](#getInvoiceTotalOneTimeTaxAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getInvoiceTotalOneTimeTaxAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/{SoftLayer_Billing_InvoiceID}/getInvoiceTotalOneTimeTaxAmount'
```
