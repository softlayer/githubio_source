---
title: "getQuoteByQuoteKey"
description: "This method will return a [[SoftLayer_Billing_Order_Quote]] that is identified by the quote key specified. If you do not... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
---
# SoftLayer_Billing_Order_Cart::getQuoteByQuoteKey
## Overview 
This method will return a [[SoftLayer_Billing_Order_Quote]] that is identified by the quote key specified. If you do not have access to the quote or it does not exist, an exception will be thrown indicating so. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|quoteKey| string| Key required to retrieve a quote.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Billing_Order_CartObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Order_Cart'>SoftLayer_Billing_Order_Cart </a>

