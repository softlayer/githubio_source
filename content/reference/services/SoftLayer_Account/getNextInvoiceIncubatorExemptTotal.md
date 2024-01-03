---
title: "getNextInvoiceIncubatorExemptTotal"
description: "The pre-tax total amount exempt from incubator credit for the account's next invoice. This field is now deprecated and will soon be removed. Please update all references to instead use nextInvoiceTotalAmount"
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

# [REST Example](#getNextInvoiceIncubatorExemptTotal-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNextInvoiceIncubatorExemptTotal-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getNextInvoiceIncubatorExemptTotal'
```
