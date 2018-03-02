---
title: "generateOrderTemplate"
description: "Obtain an [[SoftLayer_Container_Product_Order_Virtual_Guest (type)|order container]] that can be sent to [[SoftLayer_Pro... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::generateOrderTemplate
## Overview 

Obtain an [[SoftLayer_Container_Product_Order_Virtual_Guest (type)|order container]] that can be sent to [[SoftLayer_Product_Order/verifyOrder|verifyOrder]] or [[SoftLayer_Product_Order/placeOrder|placeOrder]]. 


This is primarily useful when there is a necessity to confirm the price which will be charged for an order. 


See [[SoftLayer_Virtual_Guest/createObject|createObject]] for specifics on the requirements of the template object parameter. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>


### associatedMethods

*  [SoftLayer_Virtual_Guest::createObject](/reference/services/SoftLayer_Virtual_Guest/createObject )
*  [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions )

