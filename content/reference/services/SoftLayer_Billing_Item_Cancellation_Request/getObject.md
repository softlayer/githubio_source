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
aliases:
    - "/reference/services/softlayer_billing_item_cancellation_request/getObject"
---
# [SoftLayer_Billing_Item_Cancellation_Request](/reference/services/SoftLayer_Billing_Item_Cancellation_Request)::getObject


Retrieve a SoftLayer_Billing_Item_Cancellation_Request record.


## Overview 
getObject retrieves the SoftLayer_Billing_Item_Cancellation_Request object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Item_Cancellation_Request service. You can only retrieve cancellation request records that are assigned to your SoftLayer account. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



