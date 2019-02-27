---
title: "getRecalculatedOrderContainer"
description: "Generate an [[SoftLayer_Container_Product_Order|order container]] from the previously-created quote. This will take into... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
aliases:
    - "/reference/services/softlayer_billing_order_quote/getRecalculatedOrderContainer"
---
# [SoftLayer_Billing_Order_Quote](/reference/services/SoftLayer_Billing_Order_Quote)::getRecalculatedOrderContainer

Generate an [[SoftLayer_Container_Product_Order|order container]] from the previously-created quote. 


## Overview 
Generate an [[SoftLayer_Container_Product_Order|order container]] from the previously-created quote. This will take into account promotions, reseller status, estimated taxes and all other standard order verification processes. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|userOrderData| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| User supplied order data|
|orderBeingPlacedFlag| boolean| This flag is set and used internally|


### Required Headers
* authenticate
* SoftLayer_Billing_Order_QuoteInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>




