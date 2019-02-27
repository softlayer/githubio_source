---
title: "checkItemConflicts"
description: "Check order items for conflicts"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
aliases:
    - "/reference/services/softlayer_product_order/checkItemConflicts"
---
# [SoftLayer_Product_Order](/reference/services/SoftLayer_Product_Order)::checkItemConflicts

Check order items for conflicts


## Overview 
Check order items for conflicts

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|itemPrices| <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>| Item prices to be ordered.|


### Required Headers
* authenticate


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Order_Item_Conflict 

> Throws the exception 'You cannot order (item description) with (item description)'. 



