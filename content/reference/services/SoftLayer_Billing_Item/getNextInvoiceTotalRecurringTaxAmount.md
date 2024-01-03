---
title: "getNextInvoiceTotalRecurringTaxAmount"
description: "This is deprecated and will always be zero. Because tax is calculated in real-time, previewing the next recurring invoice is pre-tax only."
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

# [REST Example](#getNextInvoiceTotalRecurringTaxAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNextInvoiceTotalRecurringTaxAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item/{SoftLayer_Billing_ItemID}/getNextInvoiceTotalRecurringTaxAmount'
```
