---
title: "addAttachedDedicatedHost"
description: "Attach the given Dedicated Host to a SoftLayer ticket. An attachment provides an easy way for SoftLayer's employees to q... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/addAttachedDedicatedHost"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::addAttachedDedicatedHost


Attach a Dedicated Host to a ticket.


## Overview 
Attach the given Dedicated Host to a SoftLayer ticket. An attachment provides an easy way for SoftLayer's employees to quickly look up your records in the case of specific issues. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHostId| integer| The internal identifier of the dedicated host record to attach.|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Dedicated_Host'>SoftLayer_Ticket_Attachment_Dedicated_Host </a>


### Associated Methods

*  [SoftLayer_Ticket::removeAttachedDedicatedHost](/reference/services/SoftLayer_Ticket/removeAttachedDedicatedHost )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to attach a null dedicated host to this ticket." if no dedicated host identifier is provided. 

* SoftLayer_Exception 

> Throw the exception "This dedicated host is already attached to this ticket." if the given dedicated host is already attached to this ticket. 

* SoftLayer_Exception 

> Throw the exception "You may not attach this dedicated host to this ticket." if the user making the API call does not have permission to use the given dedicated host. 

* SoftLayer_Exception 

> Throw the exception "Unable to attach dedicated host to this ticket." if the API is unable to attach the given dedicated host to this ticket. 



