---
title: "getAllTicketStatuses"
description: "getAllTicketStatuses() retrieves a list of all statuses that a ticket may exist in. Ticket status represent the current... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/getAllTicketStatuses"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::getAllTicketStatuses

Retrieve all available ticket statuses. 


## Overview 
getAllTicketStatuses() retrieves a list of all statuses that a ticket may exist in. Ticket status represent the current state of a ticket, usually "open", "assigned", and "closed". 

Every SoftLayer ticket has statusId and status properties that correspond to one of the statuses returned by getAllTicketStatuses(). 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket_Status'>SoftLayer_Ticket_Status[] </a>

