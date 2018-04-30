---
title: "getChildren"
description: "Retrieve an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item"
aliases:
    - "/reference/services/softlayer_billing_invoice_item/getChildren"
---
# [SoftLayer_Billing_Invoice_Item](/reference/services/SoftLayer_Billing_Invoice_Item)::getChildren

Retrieve an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children.


## Overview 
Retrieve an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_Invoice_ItemInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_Invoice_ItemObjectMask
* SoftLayer_Billing_Invoice_ItemObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>

