---
title: "getTaxInfoHistory"
description: "Retrieve this is the set of tax information for any tax calculation for this invoice. Note that not all of these are nec... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
aliases:
    - "/reference/services/softlayer_billing_invoice/getTaxInfoHistory"
---
# [SoftLayer_Billing_Invoice](/reference/services/SoftLayer_Billing_Invoice)::getTaxInfoHistory


Retrieve this is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information.


## Overview 
Retrieve this is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_InvoiceInitParameters
* authenticate


### Optional Headers
* SoftLayer_Billing_InvoiceObjectMask
* SoftLayer_Billing_InvoiceObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info'>SoftLayer_Billing_Invoice_Tax_Info[] </a>




