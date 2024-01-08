---
title: "getInvoiceTopLevelItems"
description: "A list of top-level invoice items that are on the currently pending invoice."
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

### [REST Example](#getInvoiceTopLevelItems-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getInvoiceTopLevelItems-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/{SoftLayer_Billing_InvoiceID}/getInvoiceTopLevelItems'
```
