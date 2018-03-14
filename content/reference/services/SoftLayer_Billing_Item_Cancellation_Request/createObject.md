---
title: "createObject"
description: "This method creates a service cancellation request. 

You need to have 'Cancel Services' privilege to create a cancellat... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
aliases:
    - "/reference/services/softlayer_billing_item_cancellation_request/createObject"
---
# [SoftLayer_Billing_Item_Cancellation_Request](/reference/services/SoftLayer_Billing_Item_Cancellation_Request)::createObject

Creates a cancellation request.


## Overview 
This method creates a service cancellation request. 

You need to have "Cancel Services" privilege to create a cancellation request. You have to provide at least one SoftLayer_Billing_Item_Cancellation_Request_Item in the "items" property. Make sure billing item's category code belongs to the cancelable product codes. You can retrieve the cancelable product category by the [[SoftLayer_Product_Item_Category::getValidCancelableServiceItemCategories|product category]] service. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request </a>| The SoftLayer_Billing_Item_Cancellation_Request object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Billing_Item_Cancellation_RequestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request </a>

