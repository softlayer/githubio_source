---
title: "setAssociationId"
description: "Set an associated billing item to an orphan billing item. Associations allow you to tie an 'orphaned' billing item, any... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
aliases:
    - "/reference/services/softlayer_billing_item/setAssociationId"
---
# [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item)::setAssociationId

Set the associated billing item for an orphan billing item.


## Overview 
Set an associated billing item to an orphan billing item. Associations allow you to tie an "orphaned" billing item, any non-server billing item that doesn't have a parent item such as secondary IP subnets or StorageLayer accounts, to a server billing item. You may only set an association for an orphan to a server. You cannot associate a server to an orphan if the either the server or orphan billing items have a cancellation date set. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|associatedId| integer| the billing item to associate to this item|


### Required Headers
* authenticate
* SoftLayer_Billing_ItemInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Billing_Item::removeAssociationId](/reference/services/SoftLayer_Billing_Item/removeAssociationId )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "This billing item is not an orphan billing item." if the current billing item has a parent item or already has an association defined. 

* SoftLayer_Exception_Public 

> Throw the exception "There was a problem fetching data for the associated billing Item ([associatedId])" if the SoftLayer API is unable to locate the billing item you wish to associate. 

* SoftLayer_Exception_Public 

> Throw the exception "You may only associate orphan billing items to server billing items. You chose a [categoryCode] billing item." if the billing item you're attempting to associate is not a server billing item. 

* SoftLayer_Exception_Public 

> Throw the exception "You may not associate to this billing item ($associatedId) as it is scheduled for cancellation." if the associated billing item has a cancellationDate set. 



