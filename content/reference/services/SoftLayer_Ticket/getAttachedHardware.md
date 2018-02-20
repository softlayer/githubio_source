---
title: "getAttachedHardware"
description: "Retrieve the hardware associated with a ticket. This is used in cases where a ticket is directly associated with one or... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::getAttachedHardware
## Overview 
Retrieve the hardware associated with a ticket. This is used in cases where a ticket is directly associated with one or more pieces of hardware.

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
<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>
