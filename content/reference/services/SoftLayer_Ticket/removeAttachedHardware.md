---
title: "removeAttachedHardware"
description: "detach the given hardware from a SoftLayer ticket. Removing a hardware attachment may delay ticket processing time if th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::removeAttachedHardware

detach hardware from a ticket.


## Overview 
detach the given hardware from a SoftLayer ticket. Removing a hardware attachment may delay ticket processing time if the hardware removed is relevant to the ticket's issue. Return a boolean true upon successful hardware detachment. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The internal identifier of the hardware record to detach|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Ticket::addAttachedHardware](/reference/services/SoftLayer_Ticket/addAttachedHardware )

