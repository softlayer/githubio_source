---
title: "placeOrder"
description: "Use this method for placing server orders and additional services orders. The same applies for this as with verifyOrder.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
---
# [SoftLayer_Billing_Order_Cart](/reference/services/SoftLayer_Billing_Order_Cart)::placeOrder

Place an order


## Overview 
Use this method for placing server orders and additional services orders. The same applies for this as with verifyOrder. Send in the SoftLayer_Container_Product_Order_Hardware_Server for server orders. In addition to verifying the order, placeOrder() also makes an initial authorization on the SoftLayer_Account tied to this order, if a credit card is on file. If the account tied to this order is a paypal customer, an URL will also be returned to the customer. After placing the order, you must go to this URL to finish the authorization process. This tells paypal that you indeed want to place the order. After going to this URL, it will direct you back to a SoftLayer webpage that tells us you have finished the process. After this, it will go to sales for final approval. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|orderData| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| Details required to order.|


### Required Headers
* authenticate
* SoftLayer_Billing_Order_CartInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Receipt'>SoftLayer_Container_Product_Order_Receipt </a>

