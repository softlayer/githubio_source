---
title: "edit"
description: "Edit a SoftLayer ticket. The edit method is two-fold. You may either edit a ticket itself, add an update to a ticket, at... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/edit"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::edit

Edit or update a SoftLayer ticket.


## Overview 
Edit a SoftLayer ticket. The edit method is two-fold. You may either edit a ticket itself, add an update to a ticket, attach up to two files to a ticket, or perform all of these tasks. The SoftLayer API ignores changes made to the ''userEditableFlag''  and ''accountId'' properties. You may not assign a ticket to a user that your API account does not have access to. You may not enter a custom title for standard support tickets, buy may do so when editing an administrative ticket. Finally, you may not close a ticket using this method. Please contact SoftLayer if you need a ticket closed. 

If you need to only add an update to a ticket then please use the [[SoftLayer_Ticket::addUpdate|addUpdate]] method in this service. Likewise if you need to only attach a file to a ticket then use the [[SoftLayer_Ticket::addAttachedFile|addAttachedFile]] method. The edit method exists as a convenience if you need to perform all these tasks at once. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>| A skeleton [[SoftLayer_Ticket (type)|SoftLayer_Ticket]] object containing the data of the ticket you wish to submit.|
|contents| string| The contents of the first update of the ticket. This is typically the ticket's problem description.|
|attachedFiles| <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Attachment'>SoftLayer_Container_Utility_File_Attachment[] </a>| An array of no more than two files to attach to your ticket.|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>


### Associated Methods

*  [SoftLayer_Ticket::addUpdate](/reference/services/SoftLayer_Ticket/addUpdate )
*  [SoftLayer_Ticket::addAttachedFile](/reference/services/SoftLayer_Ticket/addAttachedFile )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Please provide a subject when creating a standard support ticket." If the $templateObject parameter does not have a subjectId set. See [[SoftLayer_Ticket_Subject]] for more information. 

* SoftLayer_Exception 

> Throw the exception "Please provide ticket update contents." if no update contents are provided to the method. 

* SoftLayer_Exception 

> Throw the exception "You may not attach more than two files when updating a ticket." If the ''attachedFiles'' parameter contains more than two files. 



