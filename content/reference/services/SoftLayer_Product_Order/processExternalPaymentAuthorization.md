---
title: "processExternalPaymentAuthorization"
description: "This method simply finalizes an authorization from PayPal. It tells SoftLayer that the customer has completed the PayPal... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
---
# SoftLayer_Product_Order::processExternalPaymentAuthorization
## Overview 
This method simply finalizes an authorization from PayPal. It tells SoftLayer that the customer has completed the PayPal process. This is ONLY needed if you, the customer, have your own API into PayPal and wish to automate authorizations from PayPal and our system. For most, this method will not be needed. Once an order is placed using placeOrder() for PayPal customers, a URL is given back to the customer. In it is the token and PayerID. If you want to systematically pay with PayPal, do so then call this method with the token and PayerID. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|token| string| The token from PayPal|
|payerId| string| The PayerID from PayPal|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>

