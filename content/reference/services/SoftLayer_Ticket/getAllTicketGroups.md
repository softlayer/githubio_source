---
title: "getAllTicketGroups"
description: "getAllTicketGroups() retrieves a list of all groups that a ticket may be assigned to. Ticket groups represent the intern... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/getAllTicketGroups"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::getAllTicketGroups

Retrieve all available ticket groups. 


## Overview 
getAllTicketGroups() retrieves a list of all groups that a ticket may be assigned to. Ticket groups represent the internal department at SoftLayer who a ticket is assigned to. 

Every SoftLayer ticket has groupId and ticketGroup properties that correspond to one of the groups returned by getAllTicketGroups(). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Ticket_Group'>SoftLayer_Ticket_Group[] </a>




