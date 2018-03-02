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
---
# SoftLayer_Ticket::addAttachedFile
## Overview 
Attach the given file to a SoftLayer ticket. A file attachment is a convenient way to submit non-textual error reports to SoftLayer employees in a ticket. File attachments to tickets must have a unique name. 

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
<a href='/reference/datatypes/SoftLayer_Ticket_Attachment_File'>SoftLayer_Ticket_Attachment_File </a>


### associatedMethods

*  [SoftLayer_Ticket::getAttachedFile](/reference/services/SoftLayer_Ticket/getAttachedFile )
*  [SoftLayer_Ticket::getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles )

