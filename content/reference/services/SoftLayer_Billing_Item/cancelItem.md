---
title: "cancelItem"
description: "Cancel the resource or service for a billing Item. By default the billing item will be canceled on the next bill date an... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
aliases:
    - "/reference/services/softlayer_billing_item/cancelItem"
---
# [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item)::cancelItem


Cancel a service or resource.


## Overview 
Cancel the resource or service for a billing Item. By default the billing item will be canceled on the next bill date and reclaim of the resource will begin shortly after the cancellation. Setting the "cancelImmediately" property to true will start the cancellation immediately if the item is eligible to be canceled immediately. 

The reason parameter could be from the list below: 
* "No longer needed"
* "Business closing down"
* "Server / Upgrade Costs"
* "Migrating to larger server"
* "Migrating to smaller server"
* "Migrating to a different SoftLayer datacenter"
* "Network performance / latency"
* "Support response / timing"
* "Sales process / upgrades"
* "Moving to competitor"

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|cancelImmediately| boolean| This will trigger an immediate cancellation with a reclaim of the resource|
|cancelAssociatedBillingItems| boolean| This only applies to servers and virtual servers and will|
|reason| string| The cancellation reason. See the documentation overview to see some possible values.|
|customerNote| string| Tracks any additional information that the customer wanted to provide.|


### Required Headers
* authenticate
* SoftLayer_Billing_ItemInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "This type of service cannot be cancelled through the API.  Please submit a cancellation ticket" If a billing items service type cannot be cancelled through the API. 



