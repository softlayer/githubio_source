---
title: "getServerAdministrationRefundInvoice"
description: "Retrieve the refund invoice associated with a ticket. Only tickets with a refund applied in them have an associated refu... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::getServerAdministrationRefundInvoice
## Overview 
Retrieve the refund invoice associated with a ticket. Only tickets with a refund applied in them have an associated refund invoice.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_TicketInitParameters
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_TicketObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>
