---
title: "getTicketsClosedSinceDate"
description: "Retrieve all tickets closed since a given date."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/getTicketsClosedSinceDate"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::getTicketsClosedSinceDate

Retrieve tickets closed since a given date. 


## Overview 
Retrieve all tickets closed since a given date. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|closeDate| dateTime| Retrieve all ticket closed since this date.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>

