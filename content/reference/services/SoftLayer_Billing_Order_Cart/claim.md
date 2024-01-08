---
title: "claim"
description: "This method is used to transfer an anonymous quote to the active user and associated account. An anonymous quote is one that was created by a user without being authenticated. If a quote was created anonymously and then the customer attempts to access that anonymous quote via the API (which requires authentication), the customer will be unable to retrieve the quote due to the security restrictions in place. By providing the ability for a customer to claim a quote, s/he will be able to pull the anonymous quote onto his/her account and successfully view the quote. 

To claim a quote, both the quote id and the quote key (the 32-character random string) must be provided. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Cart"
---

### [REST Example](#claim-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#claim-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Cart/claim'
```
