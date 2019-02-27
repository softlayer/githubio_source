---
title: "cancelServiceOnAnniversaryDate"
description: "Cancel the resource or service for a billing Item"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
aliases:
    - "/reference/services/softlayer_billing_item/cancelServiceOnAnniversaryDate"
---
# [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item)::cancelServiceOnAnniversaryDate

Cancel a service or resource on the next bill date


## Overview 
Cancel the resource or service for a billing Item 

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

> Throw the exception "This type of service cannot be cancelled through the API.  Please submit a cancellation ticket" If a billing items service type cannot be cancelled through the API. 



