---
title: "addFinalComments"
description: "As part of the customer service process SoftLayer has provided a quick feedback mechanism for its customers to rate thei... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::addFinalComments
## Overview 
As part of the customer service process SoftLayer has provided a quick feedback mechanism for its customers to rate their overall experience with SoftLayer after a ticket is closed. addFinalComments() sets these comments for a ticket update made by a SoftLayer employee. Final comments may only be set on closed tickets, can only be set once, and may not exceed 4000 characters in length. Once the comments are set ''addFinalComments()'' returns a boolean true. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|finalComments| string| Feedback to leave on a closed ticket.|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers

### Return Values
boolean
