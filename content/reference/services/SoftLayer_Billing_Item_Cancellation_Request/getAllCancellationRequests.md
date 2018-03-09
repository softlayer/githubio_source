---
title: "getAllCancellationRequests"
description: "This method returns all service cancellation requests. 

Make sure to include the 'resultLimit' in the SOAP request head... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
---
# [SoftLayer_Billing_Item_Cancellation_Request](/reference/services/SoftLayer_Billing_Item_Cancellation_Request)::getAllCancellationRequests

Returns all service cancellation requests


## Overview 
This method returns all service cancellation requests. 

Make sure to include the "resultLimit" in the SOAP request header for quicker response. If there is no result limit header is passed, it will return the latest 25 results by default. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Billing_Item_Cancellation_RequestObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Billing_Item_Cancellation_RequestObjectFilter
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request[] </a>

