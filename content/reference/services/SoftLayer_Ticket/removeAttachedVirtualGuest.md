---
title: "removeAttachedVirtualGuest"
description: "Detach the given CloudLayer Computing Instance from a SoftLayer ticket. Removing an attachment may delay ticket processi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::removeAttachedVirtualGuest
## Overview 
Detach the given CloudLayer Computing Instance from a SoftLayer ticket. Removing an attachment may delay ticket processing time if the instance removed is relevant to the ticket's issue. Return a boolean true upon successful detachment. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|guestId| integer| The internal identifier of the virtual guest record to detach|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Ticket::addAttachedVirtualGuest](/reference/services/SoftLayer_Ticket/addAttachedVirtualGuest )

