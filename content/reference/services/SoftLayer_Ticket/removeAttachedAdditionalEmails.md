---
title: "removeAttachedAdditionalEmails"
description: "removeAttachedAdditionalEmails() removes the specified email addresses from a ticket's notification list. If one of the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/removeAttachedAdditionalEmails"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::removeAttachedAdditionalEmails

Detaches non-user additional email addresses from a ticket.


## Overview 
removeAttachedAdditionalEmails() removes the specified email addresses from a ticket's notification list. If one of the provided email addresses is not attached to the ticket then ''removeAttachedAdditiaonalEmails()'' ignores it and continues to the next one. Once the email addresses are removed ''removeAttachedAdditiaonalEmails()'' returns a boolean true. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|emails| array of strings| A list of email addresses to remove from a ticket's notification list|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Ticket::addAttachedAdditionalEmails](/reference/services/SoftLayer_Ticket/addAttachedAdditionalEmails )

