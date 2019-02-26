---
title: "getAssociatedInvoiceItem"
description: "Retrieve an Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item"
aliases:
    - "/reference/services/softlayer_billing_invoice_item/getAssociatedInvoiceItem"
---
# [SoftLayer_Billing_Invoice_Item](/reference/services/SoftLayer_Billing_Invoice_Item)::getAssociatedInvoiceItem

Retrieve an Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but logically belongs to the associated invoice item.


## Overview 
Retrieve an Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but logically belongs to the associated invoice item.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_Invoice_ItemInitParameters
* authenticate


### Optional Headers
* SoftLayer_Billing_Invoice_ItemObjectMask
* SoftLayer_Billing_Invoice_ItemObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a>




