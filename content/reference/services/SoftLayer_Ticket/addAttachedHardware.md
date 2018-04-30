---
title: "addAttachedHardware"
description: "Attach the given hardware to a SoftLayer ticket. A hardware attachment provides an easy way for SoftLayer's employees to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/addAttachedHardware"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::addAttachedHardware

Attach hardware to a ticket.


## Overview 
Attach the given hardware to a SoftLayer ticket. A hardware attachment provides an easy way for SoftLayer's employees to quickly look up your hardware records in the case of hardware-specific issues. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The internal identifier of the hardware record to attach.|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Hardware'>SoftLayer_Ticket_Attachment_Hardware </a>


### associatedMethods

*  [SoftLayer_Ticket::removeAttachedHardware](/reference/services/SoftLayer_Ticket/removeAttachedHardware )

