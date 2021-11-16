---
title: "saveQuote"
description: "Account master users and sub-users in the SoftLayer customer portal can save the quote of an order to avoid its deletion... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
aliases:
    - "/reference/services/softlayer_billing_order_quote/saveQuote"
---
# [SoftLayer_Billing_Order_Quote](/reference/services/SoftLayer_Billing_Order_Quote)::saveQuote


Save the quote of an order


## Overview 
Account master users and sub-users in the SoftLayer customer portal can save the quote of an order to avoid its deletion after 5 days or its expiration after 2 days. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Billing_Order_QuoteInitParameters


### Optional Headers
* SoftLayer_Billing_Order_QuoteObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote </a>


### Associated Methods

*  [SoftLayer_Billing_Order_Quote::saveQuote](/reference/services/SoftLayer_Billing_Order_Quote/saveQuote )
*  [SoftLayer_Billing_Order_Quote::deleteQuote](/reference/services/SoftLayer_Billing_Order_Quote/deleteQuote )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'You cannot save a saved quote.' 

* SoftLayer_Exception_Public 

> Throws the exception 'You cannot save a deleted quote.' 

* SoftLayer_Exception_Public 

> Throws the exception 'You cannot save an invalid quote.' 



