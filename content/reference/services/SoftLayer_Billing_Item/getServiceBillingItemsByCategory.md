---
title: "getServiceBillingItemsByCategory"
description: "This service returns billing items of a specified category code. This service should be used to retrieve billing items t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
aliases:
    - "/reference/services/softlayer_billing_item/getServiceBillingItemsByCategory"
---
# [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item)::getServiceBillingItemsByCategory

Returns billing item in a given category code. Use this method to retrieve service billing items that you wish to cancel.


## Overview 
This service returns billing items of a specified category code. This service should be used to retrieve billing items that you wish to cancel. Some billing items can be canceled via [SoftLayer_Security_Certificate_Request]({{<ref "reference/datatypes/SoftLayer_Security_Certificate_Request">}}) service. 

In order to find billing items for cancellation, use [SoftLayer_Product_Item_Category::getValidCancelableServiceItemCategories]({{<ref "reference/services/SoftLayer_Product_Item_Category/getValidCancelableServiceItemCategories">}}) service to retrieve category codes that are eligible for cancellation. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|categoryCode| string| The category code of billing items you wish to retrieve.|
|includeZeroRecurringFee| boolean| Indicates whether billing item with $0 recurring fee should be included or not|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Billing_ItemObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>




