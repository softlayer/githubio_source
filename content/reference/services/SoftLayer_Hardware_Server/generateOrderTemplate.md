---
title: "generateOrderTemplate"
description: "Obtain an [SoftLayer_Container_Product_Order_Hardware_Server]({{<ref 'reference/datatypes/SoftLayer_Container_Product_Or... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/generateOrderTemplate"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::generateOrderTemplate


Obtain an order container for a given template object


## Overview 

Obtain an [SoftLayer_Container_Product_Order_Hardware_Server]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server">}}). 


This is primarily useful when there is a necessity to confirm the price which will be charged for an order. 


See [SoftLayer_Hardware::createObject]({{<ref "reference/services/SoftLayer_Hardware/createObject">}}) for specifics on the requirements of the template object parameter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>


### Associated Methods

*  [SoftLayer_Hardware::createObject](/reference/services/SoftLayer_Hardware/createObject )
*  [SoftLayer_Hardware::getCreateObjectOptions](/reference/services/SoftLayer_Hardware/getCreateObjectOptions )




