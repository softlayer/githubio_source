---
title: "getInvoiceItems"
description: "Retrieve the invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::getInvoiceItems
## Overview 
Retrieve the invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee that has been invoiced.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_TicketInitParameters
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_TicketObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>

