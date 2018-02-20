---
title: "getExternalPaymentAuthorizationReceipt"
description: "This method simply returns a receipt for a previously finalized payment authorization from PayPal. The response matches... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
---
# SoftLayer_Product_Order::getExternalPaymentAuthorizationReceipt
## Overview 
This method simply returns a receipt for a previously finalized payment authorization from PayPal. The response matches the response returned from placeOrder when the order was originally placed with PayPal as the payment type. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|token| string| The token from PayPal|
|payerId| string| The PayerID from PayPal|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Receipt'>SoftLayer_Container_Product_Order_Receipt </a>
