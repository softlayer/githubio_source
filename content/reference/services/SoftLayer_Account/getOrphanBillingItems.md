---
title: "getOrphanBillingItems"
description: "Retrieve the billing items that have no parent billing item. These are items that don't necessarily belong to a single s... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getOrphanBillingItems"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getOrphanBillingItems

Retrieve the billing items that have no parent billing item. These are items that don't necessarily belong to a single server.


## Overview 
Retrieve the billing items that have no parent billing item. These are items that don't necessarily belong to a single server.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_AccountObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>

