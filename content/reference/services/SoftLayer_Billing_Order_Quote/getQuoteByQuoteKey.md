---
title: "getQuoteByQuoteKey"
description: "This method will return a [SoftLayer_Billing_Order_Quote]({{<ref 'reference/datatypes/SoftLayer_Billing_Order_Quote'>}})... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
aliases:
    - "/reference/services/softlayer_billing_order_quote/getQuoteByQuoteKey"
---
# [SoftLayer_Billing_Order_Quote](/reference/services/SoftLayer_Billing_Order_Quote)::getQuoteByQuoteKey

Retrieve a [SoftLayer_Billing_Order_Quote]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Quote">}}) by the quote key specified.


## Overview 
This method will return a [SoftLayer_Billing_Order_Quote]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Quote">}}) that is identified by the quote key specified. If you do not have access to the quote or it does not exist, an exception will be thrown indicating so. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|quoteKey| string| Key required to retrieve a quote.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Billing_Order_QuoteObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "No quote found" 

* SoftLayer_Exception_Public 

> Throws the exception "Quote is no longer valid." 

* SoftLayer_Exception_Public 

> Throws the exception "Quote expired." 

* SoftLayer_Exception_Public 

> Throws the exception "Quote has been removed from the system." 

* SoftLayer_Exception_Public 

> Throws the exception "Quote is unavailable." 

* SoftLayer_Exception_Public 

> Throws the exception "Could not authenticate quote." 



