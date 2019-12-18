---
title: "generateOrderTemplate"
description: "Obtain an [SoftLayer_Container_Product_Order_Virtual_Guest]({{<ref 'reference/datatypes/SoftLayer_Container_Product_Orde... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/generateOrderTemplate"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::generateOrderTemplate

Obtain an order container for a given template object


## Overview 

Obtain an [SoftLayer_Container_Product_Order_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest">}}). 


This is primarily useful when there is a necessity to confirm the price which will be charged for an order. 


See [SoftLayer_Virtual_Guest::createObject]({{<ref "reference/services/SoftLayer_Virtual_Guest/createObject">}}) for specifics on the requirements of the template object parameter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>


### Associated Methods

*  [SoftLayer_Virtual_Guest::createObject](/reference/services/SoftLayer_Virtual_Guest/createObject )
*  [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions )




