---
title: "getDriveRetentionItemPrice"
description: "Return a drive retention SoftLayer_Item_Price object for a guest."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getDriveRetentionItemPrice"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getDriveRetentionItemPrice

Return a drive retention SoftLayer_Item_Price object for a guest.


## Overview 
Return a drive retention SoftLayer_Item_Price object for a guest.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Unable to locate billing item.' when the billing item cannot be determined. 



