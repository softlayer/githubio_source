---
title: "getInvoiceTotalRecurringAmount"
description: "The total Recurring amount of this invoice. This amount does not include taxes or one time charges."
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

### [REST Example](#getInvoiceTotalRecurringAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getInvoiceTotalRecurringAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/{SoftLayer_Billing_InvoiceID}/getInvoiceTotalRecurringAmount'
```
