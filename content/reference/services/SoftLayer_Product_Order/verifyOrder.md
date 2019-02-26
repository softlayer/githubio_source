---
title: "verifyOrder"
description: "This service is used to verify that an order meets all the necessary requirements to purchase a server, virtual server o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
aliases:
    - "/reference/services/softlayer_product_order/verifyOrder"
---
# [SoftLayer_Product_Order](/reference/services/SoftLayer_Product_Order)::verifyOrder

Verify that an order may be successfully placed with the details provided.


## Overview 
This service is used to verify that an order meets all the necessary requirements to purchase a server, virtual server or service from SoftLayer. It will verify that the products requested do not conflict. For example, you cannot order a Windows firewall with a Linux operating system. It will also check to make sure you have provided all the products that are required for the [[SoftLayer_Product_Package_Order_Configuration (type)|package configuration]] associated with the [[SoftLayer_Product_Package|package id]] on each of the [[SoftLayer_Container_Product_Order (type)|order containers]] specified.<br/><br/> 

This service returns the same container that was provided, but with additional information that can be used for debugging or validation. It will also contain pricing information (prorated if applicable) for each of the products on the order. If an exception occurs during verification, a container with the <code>SoftLayer_Exception_Order</code> exception type will be specified in the result.<br/><br/> 

<code>verifyOrder</code> accepts the same [[SoftLayer_Container_Product_Order (type)|container types]] as <code>placeOrder</code>, so see [[SoftLayer_Product_Order/placeOrder|placeOrder]] for more details. 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|orderData| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| Details required to order.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>


### Associated Methods

*  [SoftLayer_Product_Order::placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder )
*  [SoftLayer_Product_Order::placeQuote](/reference/services/SoftLayer_Product_Order/placeQuote )
*  [SoftLayer_Product_Order::getVlans](/reference/services/SoftLayer_Product_Order/getVlans )




