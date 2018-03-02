---
title: "getInvoice"
description: "Retrieve this is the invoice associated with the upgrade request. For hourly servers or services, an invoice will not be... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Upgrade_Request"
---
# SoftLayer_Product_Upgrade_Request::getInvoice
## Overview 
Retrieve this is the invoice associated with the upgrade request. For hourly servers or services, an invoice will not be available.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Product_Upgrade_RequestInitParameters
* authenticate

### Optional Headers
* SoftLayer_Product_Upgrade_RequestObjectMask
* SoftLayer_Product_Upgrade_RequestObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>

