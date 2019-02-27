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
aliases:
    - "/reference/services/softlayer_ticket/removeAttachedVirtualGuest"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::removeAttachedVirtualGuest

Detach a CloudLayer Computing Instance from a ticket.


## Overview 
Detach the given CloudLayer Computing Instance from a SoftLayer ticket. Removing an attachment may delay ticket processing time if the instance removed is relevant to the ticket's issue. Return a boolean true upon successful detachment. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|guestId| integer| The internal identifier of the virtual guest record to detach|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Ticket::addAttachedVirtualGuest](/reference/services/SoftLayer_Ticket/addAttachedVirtualGuest )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to detach null virtual guest from this ticket." if no virtual guest identifier is provided. 

* SoftLayer_Exception 

> Throw the exception "This virtual guest is not attached to this ticket." if the given virtual guest is not attached to this ticket. 

* SoftLayer_Exception 

> Throw the exception "You may not detach this virtual guest from this ticket." if the user making the API call does not have permission to use the given virtual guest. 

* SoftLayer_Exception 

> Throw the exception "Unable to detach virtual guest from this ticket." if the API is unable to detach the given virtual guest from this ticket. 



