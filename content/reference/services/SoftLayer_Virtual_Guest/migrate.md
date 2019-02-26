---
title: "migrate"
description: "Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if SoftLayer_Virtual_Guest prope... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/migrate"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::migrate

Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if SoftLayer_Virtual_Guest property pendingMigrationFlag = true 


## Overview 
Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if SoftLayer_Virtual_Guest property pendingMigrationFlag = true

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>




