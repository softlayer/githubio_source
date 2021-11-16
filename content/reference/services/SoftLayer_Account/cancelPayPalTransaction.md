---
title: "cancelPayPalTransaction"
description: "Cancel the PayPal Payment Request process. During the process of submitting a PayPal payment request, the customer is re... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/cancelPayPalTransaction"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::cancelPayPalTransaction


Cancel the PayPal Payment Request process.


## Overview 
Cancel the PayPal Payment Request process. During the process of submitting a PayPal payment request, the customer is redirected to PayPal to confirm the request.  If the customer elects to cancel the payment from PayPal, they are returned to SoftLayer where the manual payment record is updated to a status of canceled. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|token| string| Value provided by PayPal to access paypal information and complete the transaction.|
|payerId| string| Paypal user identifier.|


### Required Headers
* authenticate


### Return Values
* boolean




