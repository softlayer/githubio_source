---
title: "deleteQuote"
description: "Account master users and sub-users in the SoftLayer customer portal can delete the quote of an order. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Quote"
---

### [REST Example](#deleteQuote-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteQuote-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Quote/{SoftLayer_Billing_Order_QuoteID}/deleteQuote'
```
