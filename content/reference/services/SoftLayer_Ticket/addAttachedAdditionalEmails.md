---
title: "addAttachedAdditionalEmails"
description: "Creates new additional emails for assigned user if new emails are provided. Attaches any newly created additional emails... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/addAttachedAdditionalEmails"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::addAttachedAdditionalEmails


Add non-user email addresses to a ticket's email notify list.


## Overview 
Creates new additional emails for assigned user if new emails are provided. Attaches any newly created additional emails to ticket. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|emails| array of strings| A list of email addresses to notify when a ticket is updated|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Ticket::removeAttachedAdditionalEmails](/reference/services/SoftLayer_Ticket/removeAttachedAdditionalEmails )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "This ticket does not have an assigned user. Could not add additional emails." if the given ticket is not assigned to a user. 

* SoftLayer_Exception_Public 

> Throw the exception "Invalid email address(es) found: {list of invalid email addreses}" if one or more email addresses are invalid. 



