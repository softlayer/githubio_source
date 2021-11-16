---
title: "getPostProvisioningHooks"
description: "Retrieve customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent ove... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getPostProvisioningHooks"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getPostProvisioningHooks


Retrieve customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.


## Overview 
Retrieve customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.

-----

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
* <a href='/reference/datatypes/SoftLayer_Provisioning_Hook'>SoftLayer_Provisioning_Hook[] </a>




