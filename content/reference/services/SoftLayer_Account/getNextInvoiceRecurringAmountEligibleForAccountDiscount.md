---
title: "getNextInvoiceRecurringAmountEligibleForAccountDiscount"
description: "The total recurring charge amount of an account's next invoice eligible for account discount measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing."
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

# [REST Example](#getNextInvoiceRecurringAmountEligibleForAccountDiscount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNextInvoiceRecurringAmountEligibleForAccountDiscount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getNextInvoiceRecurringAmountEligibleForAccountDiscount'
```
