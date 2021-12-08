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
aliases:
    - "/reference/services/softlayer_ticket/addFinalComments"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::addFinalComments


Add final comments to a closed ticket.


## Overview 
As part of the customer service process SoftLayer has provided a quick feedback mechanism for its customers to rate their overall experience with SoftLayer after a ticket is closed. addFinalComments() sets these comments for a ticket update made by a SoftLayer employee. Final comments may only be set on closed tickets, can only be set once, and may not exceed 4000 characters in length. Once the comments are set ''addFinalComments()'' returns a boolean true. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|finalComments| string| Feedback to leave on a closed ticket.|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Ticket_Update_Employee::addResponseRating](/reference/services/SoftLayer_Ticket_Update_Employee/addResponseRating )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "You can only add final comments to a closed ticket." if the given ticket is not closed. 

* SoftLayer_Exception_Public 

> Throw the exception "This ticket already has final comments set." if the given ticket already has final comments set. 

* SoftLayer_Exception_Public 

> Throw the exception "Please provide final comments." if no final comments were passed to ''addFinalComments()''. 

* SoftLayer_Exception_Public 

> Throw the exception "Your final comments may not exceed 4000 characters in length." if the given final comments exceed 4000 characters in length. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to add final comments to this ticket." if the API was unable to add final comments to the given ticket. 



