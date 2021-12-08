---
title: "setManagedPoolQuantity"
description: "Set the total number of servers that are to be maintained in the given pool. When a server is ordered a new server will... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/setManagedPoolQuantity"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::setManagedPoolQuantity


Set the number of desired servers in the pool


## Overview 
Set the total number of servers that are to be maintained in the given pool. When a server is ordered a new server will be put in the pool to replace the server that was removed to fill an order to maintain the desired pool availability quantity. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|poolKeyName| string| $poolKeyName|
|backendRouter| string| $backendRouter|
|quantity| integer| $quantity|


### Required Headers
* authenticate


### Return Values
* integer




