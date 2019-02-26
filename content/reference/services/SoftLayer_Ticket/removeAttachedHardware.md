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
aliases:
    - "/reference/services/softlayer_ticket/removeAttachedHardware"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::removeAttachedHardware

detach hardware from a ticket.


## Overview 
detach the given hardware from a SoftLayer ticket. Removing a hardware attachment may delay ticket processing time if the hardware removed is relevant to the ticket's issue. Return a boolean true upon successful hardware detachment. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The internal identifier of the hardware record to detach|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Ticket::addAttachedHardware](/reference/services/SoftLayer_Ticket/addAttachedHardware )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to detach null hardware from this ticket." if no hardware identifier is provided. 

* SoftLayer_Exception 

> Throw the exception "This hardware is not attached to this ticket." if the given hardware is not attached to this ticket. 

* SoftLayer_Exception 

> Throw the exception "You may not detach this hardware from this ticket." if the user making the API call does not have permission to use the given hardware. 

* SoftLayer_Exception 

> Throw the exception "Unable to detach hardware from this ticket." if the API is unable to detach the given hardware from this ticket. 



