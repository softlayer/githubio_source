---
title: "getFilteredNextInvoiceChildren"
description: "Retrieve a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
aliases:
    - "/reference/services/softlayer_billing_item_virtual_dedicatedhost/getFilteredNextInvoiceChildren"
---
# [SoftLayer_Billing_Item_Virtual_DedicatedHost](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost)::getFilteredNextInvoiceChildren

Retrieve a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee.


## Overview 
Retrieve a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_Item_Virtual_DedicatedHostInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_Item_Virtual_DedicatedHostObjectMask
* SoftLayer_Billing_Item_Virtual_DedicatedHostObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>

