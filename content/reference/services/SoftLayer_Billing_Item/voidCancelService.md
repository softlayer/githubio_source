---
title: "voidCancelService"
description: "Void a previously made cancellation for a service"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
aliases:
    - "/reference/services/softlayer_billing_item/voidCancelService"
---
# [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item)::voidCancelService


Void a service cancellation that was previously made.


## Overview 
Void a previously made cancellation for a service 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Billing_ItemInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Cannot void cancellation for this service through the API." If a billing items service type cannot have a cancellation voided through the API. 

* SoftLayer_Exception_Public 

> Throw the exception "Cannot void cancellation.  This billing item is not set to cancel." If a service is not cancelled. 

* SoftLayer_Exception_Public 

> Throw the exception "Cannot void cancellation.  The void cnacellation period has expired." If the void cancellation period has expired 



