---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Invoice object whose ID number corresponds to the ID number of the init parame... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
---
# [SoftLayer_Billing_Invoice](/reference/services/SoftLayer_Billing_Invoice)::getObject

Retrieve a SoftLayer_Billing_Invoice record.


## Overview 
getObject retrieves the SoftLayer_Billing_Invoice object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Invoice service. You can only retrieve invoices that are assigned to your portal user's account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_InvoiceInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_InvoiceObjectMask
* SoftLayer_Billing_InvoiceObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>


### associatedMethods

*  [SoftLayer_Account::getInvoices](/reference/services/SoftLayer_Account/getInvoices )

