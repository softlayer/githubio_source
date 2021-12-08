---
title: "getAdditionalRequiredPricesForOsReload"
description: "Return a collection of SoftLayer_Item_Price objects for an OS reload"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getAdditionalRequiredPricesForOsReload"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getAdditionalRequiredPricesForOsReload


Return a collection of SoftLayer_Item_Price objects for an OS reload


## Overview 
Return a collection of SoftLayer_Item_Price objects for an OS reload

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|config| <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration'>SoftLayer_Container_Hardware_Server_Configuration </a>| The new cloud configuration for the reload.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Unable to locate billing item.' when the billing item cannot be determined. 

* SoftLayer_Exception_Public 

> Throws the exception 'Unable to locate a required price for the primary disk.' when the primary disk requires a larger capacity and a product cannot be determined. 



