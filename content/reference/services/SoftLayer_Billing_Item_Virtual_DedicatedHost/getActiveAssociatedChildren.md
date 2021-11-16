---
title: "getActiveAssociatedChildren"
description: "Retrieve a billing item's active associated child billing items. This includes 'floating' items that are not necessarily... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
aliases:
    - "/reference/services/softlayer_billing_item_virtual_dedicatedhost/getActiveAssociatedChildren"
---
# [SoftLayer_Billing_Item_Virtual_DedicatedHost](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost)::getActiveAssociatedChildren


Retrieve a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.


## Overview 
Retrieve a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_Item_Virtual_DedicatedHostInitParameters
* authenticate


### Optional Headers
* SoftLayer_Billing_Item_Virtual_DedicatedHostObjectMask
* SoftLayer_Billing_Item_Virtual_DedicatedHostObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>




