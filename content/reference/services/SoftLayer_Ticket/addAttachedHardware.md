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

-----

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
* <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Hardware'>SoftLayer_Ticket_Attachment_Hardware </a>


### Associated Methods

*  [SoftLayer_Ticket::removeAttachedHardware](/reference/services/SoftLayer_Ticket/removeAttachedHardware )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to attach null hardware to this ticket." if no hardware identifier is provided. 

* SoftLayer_Exception 

> Throw the exception "This hardware is already attached to this ticket." if the given hardware is already attached to this ticket. 

* SoftLayer_Exception 

> Throw the exception "You may not attach this hardware to this ticket." if the user making the API call does not have permission to use the given hardware. 

* SoftLayer_Exception 

> Throw the exception "Unable to attach hardware to this ticket." if the API is unable to attach the given hardware to this ticket. 



