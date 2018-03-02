---
title: "addUpdate"
description: "Add an update to a ticket. A ticket update's entry has a maximum length of 4000 characters, so ''addUpdate()'' splits th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::addUpdate
## Overview 
Add an update to a ticket. A ticket update's entry has a maximum length of 4000 characters, so ''addUpdate()'' splits the ''entry'' property in the ''templateObject'' parameter into 3900 character blocks and creates one entry per 3900 character block. Once complete ''addUpdate()'' emails the ticket's owner and additional email addresses with an update message if the ticket's ''notifyUserOnUpdateFlag'' is set. If the ticket is a Legal or Abuse ticket, then the account's abuse emails are also notified when the updates are processed. Finally, ''addUpdate()'' returns an array of the newly created ticket updates. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update </a>| The update to add to the ticket|
|attachedFiles| <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Attachment'>SoftLayer_Container_Utility_File_Attachment[] </a>| An array of no more than two files to attach to your ticket.|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update[] </a>

