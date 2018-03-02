---
title: "getBillingItem"
description: "Retrieve an associated parent billing item which is active. Includes billing items which are scheduled to be cancelled i... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_MassDataMigration_Request"
---
# SoftLayer_Network_Storage_MassDataMigration_Request::getBillingItem
## Overview 
Retrieve an associated parent billing item which is active. Includes billing items which are scheduled to be cancelled in the future.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_MassDataMigration_RequestInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_MassDataMigration_RequestObjectMask
* SoftLayer_Network_Storage_MassDataMigration_RequestObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>

