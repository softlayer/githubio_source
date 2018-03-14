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
aliases:
    - "/reference/services/softlayer_ticket/getInvoiceItems"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::getInvoiceItems

Retrieve the invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee that has been invoiced.


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

