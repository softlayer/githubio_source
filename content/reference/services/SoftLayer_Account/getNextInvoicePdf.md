---
title: "getNextInvoicePdf"
description: "Return an account's next invoice in PDF format. The 'next invoice' is what a customer will be billed on their next invoice, assuming no changes are made. Currently this does not include Bandwidth Pooling charges."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

# [REST Example](#getNextInvoicePdf-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNextInvoicePdf-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getNextInvoicePdf'
```
