---
title: "getResellerOrder"
description: "When the account is on an external reseller brand, this service will provide a SoftLayer_Product_Order with the the pric... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
aliases:
    - "/reference/services/softlayer_product_order/getResellerOrder"
---
# [SoftLayer_Product_Order](/reference/services/SoftLayer_Product_Order)::getResellerOrder

Get External Reseller pricing where applicable


## Overview 
When the account is on an external reseller brand, this service will provide a SoftLayer_Product_Order with the the pricing adjusted by the external reseller. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|orderContainer| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Reseller pricing not supported" This account is not under a supported reseller. 

* SoftLayer_Exception_Public 

> Throw the exception "There was an issue getting the reseller pricing." The reseller partner was unable to provide pricing. 



