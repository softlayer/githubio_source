---
title: "getPdf"
description: "Retrieve a PDF record of a SoftLayer quoted order. SoftLayer keeps PDF records of all quoted orders for customer retriev... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
aliases:
    - "/reference/services/softlayer_billing_order_quote/getPdf"
---
# [SoftLayer_Billing_Order_Quote](/reference/services/SoftLayer_Billing_Order_Quote)::getPdf

Retrieve a PDF copy of a quote.


## Overview 
Retrieve a PDF record of a SoftLayer quoted order. SoftLayer keeps PDF records of all quoted orders for customer retrieval from the portal and API. You must have a PDF reader installed in order to view these quoted order files. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Billing_Order_QuoteInitParameters


### Return Values
* binary data



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'PDF does not exist: Order has not yet been created.' 

* SoftLayer_Exception_Public 

> Throws the exception 'PDF does not exist: file not found.' 

* SoftLayer_Exception_Public 

> Throws the exception 'PDF does not exist: Unable to load the quote PDF.' 



