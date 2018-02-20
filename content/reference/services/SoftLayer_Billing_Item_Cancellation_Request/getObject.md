---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Item_Cancellation_Request object whose ID number corresponds to the ID number... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
---
# SoftLayer_Billing_Item_Cancellation_Request::getObject
## Overview 
getObject retrieves the SoftLayer_Billing_Item_Cancellation_Request object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Item_Cancellation_Request service. You can only retrieve cancellation request records that are assigned to your SoftLayer account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_Item_Cancellation_RequestInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_Item_Cancellation_RequestObjectMask
* SoftLayer_Billing_Item_Cancellation_RequestObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request </a>
