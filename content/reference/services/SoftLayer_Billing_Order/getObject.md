---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Order object whose ID number corresponds to the ID number of the init paramete... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
aliases:
    - "/reference/services/softlayer_billing_order/getObject"
---
# [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order)::getObject

Retrieve a SoftLayer_Billing_Order record.


## Overview 
getObject retrieves the SoftLayer_Billing_Order object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Order service. You can only retrieve orders that are assigned to your portal user's account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_OrderInitParameters
* authenticate


### Optional Headers
* SoftLayer_Billing_OrderObjectMask
* SoftLayer_Billing_OrderObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>


### Associated Methods

*  [SoftLayer_Account::getInvoices](/reference/services/SoftLayer_Account/getInvoices )



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 



