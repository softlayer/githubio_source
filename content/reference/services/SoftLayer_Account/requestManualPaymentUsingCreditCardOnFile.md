---
title: "requestManualPaymentUsingCreditCardOnFile"
description: "Retrieve the record data associated with the submission of a Manual Payment Request for a manual payment using a credit card which is on file and does not require an approval process.  Softlayer customers are permitted to request a manual one-time payment at a minimum amount of $2.00.  Customers may use an existing Credit Card on file (Mastercard, Visa, American Express).  SoftLayer engages the credit card financial institution to submit the payment request.  The financial institution's response and other data associated with the transaction are returned to the calling function.  The applicable data generated during the request is returned to the calling function. "
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

# [REST Example](#requestManualPaymentUsingCreditCardOnFile-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#requestManualPaymentUsingCreditCardOnFile-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/requestManualPaymentUsingCreditCardOnFile'
```
