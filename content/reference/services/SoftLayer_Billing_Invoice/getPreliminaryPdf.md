---
title: "getPreliminaryPdf"
description: "Retrieve a PDF record of a SoftLayer invoice. SoftLayer keeps PDF records of all closed invoices for customer retrieval from the portal and API. You must have a PDF reader installed in order to view these invoice files. "
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

### [REST Example](#getPreliminaryPdf-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPreliminaryPdf-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/{SoftLayer_Billing_InvoiceID}/getPreliminaryPdf'
```
