---
title: "getNextInvoiceTotalRecurringTaxAmount"
description: "The total recurring tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getNextInvoiceTotalRecurringTaxAmount'
```
