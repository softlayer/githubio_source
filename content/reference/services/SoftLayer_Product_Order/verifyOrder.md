---
title: "verifyOrder"
description: "This service is used to verify that an order meets all the necessary requirements to purchase a server, virtual server or service from SoftLayer. It will verify that the products requested do not conflict. For example, you cannot order a Windows firewall with a Linux operating system. It will also check to make sure you have provided all the products that are required for the [SoftLayer_Product_Package_Order_Configuration](/reference/datatypes/SoftLayer_Product_Package_Order_Configuration) associated with the [SoftLayer_Product_Package](/reference/datatypes/SoftLayer_Product_Package) on each of the [SoftLayer_Container_Product_Order](/reference/datatypes/SoftLayer_Container_Product_Order) specified.<br/><br/> 

This service returns the same container that was provided, but with additional information that can be used for debugging or validation. It will also contain pricing information (prorated if applicable) for each of the products on the order. If an exception occurs during verification, a container with the <code>SoftLayer_Exception_Order</code> exception type will be specified in the result.<br/><br/> 

<code>verifyOrder</code> accepts the same [SoftLayer_Container_Product_Order](/reference/datatypes/SoftLayer_Container_Product_Order) as <code>placeOrder</code>, so see [SoftLayer_Product_Order::placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder) for more details. 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Order"
---
