---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Invoice_Item object whose ID number corresponds to the ID number of the init p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item"
aliases:
    - "/reference/services/softlayer_billing_invoice_item/getObject"
---
# [SoftLayer_Billing_Invoice_Item](/reference/services/SoftLayer_Billing_Invoice_Item)::getObject

Retrieve a SoftLayer_Billing_Invoice_Item record.


## Overview 
getObject retrieves the SoftLayer_Billing_Invoice_Item object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Invoice_Item service. You can only retrieve the items tied to the account that your portal user is assigned to. 

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




