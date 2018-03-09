---
title: "generateOrderTemplate"
description: "Obtain an [[SoftLayer_Container_Product_Order_Hardware_Server (type)|order container]] that can be sent to [[SoftLayer_P... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::generateOrderTemplate

Obtain an order container for a given template object


## Overview 

Obtain an [[SoftLayer_Container_Product_Order_Hardware_Server (type)|order container]] that can be sent to [[SoftLayer_Product_Order/verifyOrder|verifyOrder]] or [[SoftLayer_Product_Order/placeOrder|placeOrder]]. 


This is primarily useful when there is a necessity to confirm the price which will be charged for an order. 


See [[SoftLayer_Hardware/createObject|createObject]] for specifics on the requirements of the template object parameter. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>


### associatedMethods

*  [SoftLayer_Hardware::createObject](/reference/services/SoftLayer_Hardware/createObject )
*  [SoftLayer_Hardware::getCreateObjectOptions](/reference/services/SoftLayer_Hardware/getCreateObjectOptions )

