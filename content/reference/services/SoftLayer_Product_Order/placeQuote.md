---
title: "placeQuote"
description: "Use this method for placing server quotes and additional services quotes. The same applies for this as with verifyOrder.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
---
# SoftLayer_Product_Order::placeQuote
## Overview 
Use this method for placing server quotes and additional services quotes. The same applies for this as with verifyOrder. Send in the SoftLayer_Container_Product_Order_Hardware_Server for server quotes. After placing the quote, you must go to this URL to finish the order process. After going to this URL, it will direct you back to a SoftLayer webpage that tells us you have finished the process. After this, it will go to sales for final approval. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|orderData| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| Details required to order.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Receipt'>SoftLayer_Container_Product_Order_Receipt </a>

