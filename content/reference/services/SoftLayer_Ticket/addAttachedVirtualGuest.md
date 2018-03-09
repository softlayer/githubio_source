---
title: "addAttachedVirtualGuest"
description: "Attach the given CloudLayer Computing Instance to a SoftLayer ticket. An attachment provides an easy way for SoftLayer's... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::addAttachedVirtualGuest

Attach a CloudLayer Computing Instance to a ticket.


## Overview 
Attach the given CloudLayer Computing Instance to a SoftLayer ticket. An attachment provides an easy way for SoftLayer's employees to quickly look up your records in the case of specific issues. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|guestId| integer| The internal identifier of the virtual guest record to attach.|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Virtual_Guest'>SoftLayer_Ticket_Attachment_Virtual_Guest </a>


### associatedMethods

*  [SoftLayer_Ticket::removeAttachedVirtualGuest](/reference/services/SoftLayer_Ticket/removeAttachedVirtualGuest )

