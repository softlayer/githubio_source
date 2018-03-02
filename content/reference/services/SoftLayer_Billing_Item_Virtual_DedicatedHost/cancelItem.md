---
title: "cancelItem"
description: "Cancel the resource or service for a billing Item. By default the billing item will be cancelled immediately and reclaim... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---
# SoftLayer_Billing_Item_Virtual_DedicatedHost::cancelItem
## Overview 
Cancel the resource or service for a billing Item. By default the billing item will be cancelled immediately and reclaim of the resource will begin shortly. Setting the "cancelImmediately" property to false will delay the cancellation until the next bill date. 


* The reason parameter could be from the list below:
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

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|cancelImmediately| boolean| This will trigger an immediate cancellation with a reclaim of the resource|
|cancelAssociatedBillingItems| boolean| This only applies to servers and virtual servers and will|
|reason| string| The cancellation reason. See the documentation overview to see some possible values.|
|customerNote| string| Tracks any additional information that the customer wanted to provide.|


### Required Headers
* authenticate
* SoftLayer_Billing_Item_Virtual_DedicatedHostInitParameters

### Optional Headers

### Return Values
boolean

