---
title: "addAttachedFile"
description: "Attach the given file to a SoftLayer ticket. A file attachment is a convenient way to submit non-textual error reports t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/addAttachedFile"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::addAttachedFile


Attach a file to a ticket.


## Overview 
Attach the given file to a SoftLayer ticket. A file attachment is a convenient way to submit non-textual error reports to SoftLayer employees in a ticket. File attachments to tickets must have a unique name. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileAttachment| <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Attachment'>SoftLayer_Container_Utility_File_Attachment </a>| The file to attach|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_File'>SoftLayer_Ticket_Attachment_File </a>


### Associated Methods

*  [SoftLayer_Ticket::getAttachedFile](/reference/services/SoftLayer_Ticket/getAttachedFile )
*  [SoftLayer_Ticket::getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to attach a null file to this ticket." if an empty SoftLayer_Container_File_Attachment is provided. 

* SoftLayer_Exception 

> Throw the exception "Unable to attach a file with no file name to this ticket." if the given file attachment has no file name. 

* SoftLayer_Exception 

> Throw the exception "Unable to attach a file with no contents to this ticket." if the given file attachment has no contents. 

* SoftLayer_Exception 

> Throw the exception "A file named {filename} is already attached to this ticket." if the a file with the same name is already attached to this ticket. 

* SoftLayer_Exception 

> Throw the exception "Unable to attach file to this ticket." if the API is unable to attach the given file to this ticket. 



