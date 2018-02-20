---
title: "completePayPalTransaction"
description: "Complete the PayPal Payment Request process and receive confirmation message. During the process of submitting a PayPal... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::completePayPalTransaction
## Overview 
Complete the PayPal Payment Request process and receive confirmation message. During the process of submitting a PayPal payment request, the customer is redirected to PayPal to confirm the request.  Once confirmed, PayPal returns the customer to SoftLayer where an attempt is made to finalize the transaction.  A status message regarding the attempt is returned to the calling function. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|token| string| Value provided by PayPal to access paypal information and complete the transaction.|
|payerId| string| Paypal user identifier.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
string
