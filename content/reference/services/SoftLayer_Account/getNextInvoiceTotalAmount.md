---
title: "getNextInvoiceTotalAmount"
description: "The pre-tax total amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing."
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

### [REST Example](#getNextInvoiceTotalAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNextInvoiceTotalAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getNextInvoiceTotalAmount'
```
