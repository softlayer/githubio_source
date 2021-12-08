---
title: "getAttachedFile"
description: "Retrieve the file attached to a SoftLayer ticket by it's given identifier. To retrieve a list of files attached to a tic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/getAttachedFile"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::getAttachedFile


Retrieve a file attached to a ticket.


## Overview 
Retrieve the file attached to a SoftLayer ticket by it's given identifier. To retrieve a list of files attached to a ticket either call the SoftLayer_Ticket::getAttachedFiles method or call SoftLayer_Ticket::getObject with ''attachedFiles'' defined in an object mask. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|attachmentId| integer| The id of the attachment to retrieve|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Return Values
* binary data


### Associated Methods

*  [SoftLayer_Ticket::getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles )
*  [SoftLayer_Ticket::getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles )
*  [SoftLayer_Ticket::addAttachedFile](/reference/services/SoftLayer_Ticket/addAttachedFile )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "File {attachmentId} is not attached to ticket {ticketId}." if the given file is not attached to the given ticket. 

* SoftLayer_Exception 

> Throw the exception "File does not exist: file not found." if the given file is attached to the ticket, but not present in SoftLayer's attachment backend filesystem. 

* SoftLayer_Exception 

> Throw the exception "Unable to load a valid ticket file attachment." exists but is not retrievable by the API. 



