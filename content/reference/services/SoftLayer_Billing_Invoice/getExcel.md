---
title: "getExcel"
description: "Retrieve a Microsoft Excel spreadsheet of a SoftLayer invoice. You must have a Microsoft Excel reader installed in order to view these invoice files. "
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

### [REST Example](#getExcel-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getExcel-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/{SoftLayer_Billing_InvoiceID}/getExcel'
```
