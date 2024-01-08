---
title: "completePayPalTransaction"
description: "Complete the PayPal Payment Request process and receive confirmation message. During the process of submitting a PayPal payment request, the customer is redirected to PayPal to confirm the request.  Once confirmed, PayPal returns the customer to SoftLayer where an attempt is made to finalize the transaction.  A status message regarding the attempt is returned to the calling function. "
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

### [REST Example](#completePayPalTransaction-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#completePayPalTransaction-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/completePayPalTransaction'
```
