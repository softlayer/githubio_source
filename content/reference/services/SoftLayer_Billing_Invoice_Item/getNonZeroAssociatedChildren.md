---
title: "getNonZeroAssociatedChildren"
description: "Retrieve an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent i... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item"
aliases:
    - "/reference/services/softlayer_billing_invoice_item/getNonZeroAssociatedChildren"
---
# [SoftLayer_Billing_Invoice_Item](/reference/services/SoftLayer_Billing_Invoice_Item)::getNonZeroAssociatedChildren


Retrieve an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.


## Overview 
Retrieve an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.

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
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>




