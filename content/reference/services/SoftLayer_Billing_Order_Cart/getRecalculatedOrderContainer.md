---
title: "getRecalculatedOrderContainer"
description: "This method allows the customer to retrieve a saved cart and put it in a format that's suitable to be sent to SoftLayer_... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
aliases:
    - "/reference/services/softlayer_billing_order_cart/getRecalculatedOrderContainer"
---
# [SoftLayer_Billing_Order_Cart](/reference/services/SoftLayer_Billing_Order_Cart)::getRecalculatedOrderContainer


Retrieve order container from a saved cart


## Overview 
This method allows the customer to retrieve a saved cart and put it in a format that's suitable to be sent to SoftLayer_Billing_Order_Cart::createCart to create a new cart or to SoftLayer_Billing_Order_Cart::updateCart to update an existing cart. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|orderData| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| Details for an order|
|orderBeingPlacedFlag| boolean| Determines if an order is actually being placed|


### Required Headers
* authenticate
* SoftLayer_Billing_Order_CartInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>




