---
title: "setAssociationId"
description: "Set an associated billing item to an orphan billing item. Associations allow you to tie an 'orphaned' billing item, any... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---
# [SoftLayer_Billing_Item_Virtual_DedicatedHost](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost)::setAssociationId

Set the associated billing item for an orphan billing item.


## Overview 
Set an associated billing item to an orphan billing item. Associations allow you to tie an "orphaned" billing item, any non-server billing item that doesn't have a parent item such as secondary IP subnets or StorageLayer accounts, to a server billing item. You may only set an association for an orphan to a server. You cannot associate a server to an orphan if the either the server or orphan billing items have a cancellation date set. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|associatedId| integer| the billing item to associate to this item|


### Required Headers
* authenticate
* SoftLayer_Billing_Item_Virtual_DedicatedHostInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Billing_Item::removeAssociationId](/reference/services/SoftLayer_Billing_Item/removeAssociationId )

