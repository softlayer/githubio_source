---
title: "getAllCouriersByType"
description: "Retrieve a list of available shipping couriers."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Shipment"
---
# SoftLayer_Account_Shipment::getAllCouriersByType
## Overview 
Retrieve a list of available shipping couriers.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|courierTypeKeyName| string| The keyName for the courier type.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Account_ShipmentObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Auxiliary_Shipping_Courier'>SoftLayer_Auxiliary_Shipping_Courier[] </a>

