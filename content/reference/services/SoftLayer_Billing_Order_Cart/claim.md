---
title: "claim"
description: "This method is used to transfer an anonymous quote to the active user and associated account. An anonymous quote is one... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
---
# SoftLayer_Billing_Order_Cart::claim
## Overview 
This method is used to transfer an anonymous quote to the active user and associated account. An anonymous quote is one that was created by a user without being authenticated. If a quote was created anonymously and then the customer attempts to access that anonymous quote via the API (which requires authentication), the customer will be unable to retrieve the quote due to the security restrictions in place. By providing the ability for a customer to claim a quote, s/he will be able to pull the anonymous quote onto his/her account and successfully view the quote. 

To claim a quote, both the quote id and the quote key (the 32-character random string) must be provided. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|quoteKey| string| The 32-character random string generated when the quote was created|
|quoteId| integer| The quote's unique identifier (id) property|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Billing_Order_CartObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Order_Cart'>SoftLayer_Billing_Order_Cart </a>
