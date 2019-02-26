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
aliases:
    - "/reference/services/softlayer_account_shipment/getAllCouriersByType"
---
# [SoftLayer_Account_Shipment](/reference/services/SoftLayer_Account_Shipment)::getAllCouriersByType

Retrieve a list of couriers for a given courier type


## Overview 
Retrieve a list of available shipping couriers.

-----

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
* <a href='/reference/datatypes/SoftLayer_Auxiliary_Shipping_Courier'>SoftLayer_Auxiliary_Shipping_Courier[] </a>




