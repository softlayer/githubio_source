---
title: "emailInvoices"
description: "Create a transaction to email PDF and/or Excel invoice links to the requesting user's email address. You must have a PDF reader installed in order to view these files. "
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

# [REST Example](#emailInvoices-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#emailInvoices-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Billing_Invoice_Email]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/emailInvoices'
```
