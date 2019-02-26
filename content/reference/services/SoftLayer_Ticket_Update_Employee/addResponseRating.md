---
title: "addResponseRating"
description: "As part of the customer service process SoftLayer has provided a quick feedback mechanism for its customers to rate the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Update_Employee"
aliases:
    - "/reference/services/softlayer_ticket_update_employee/addResponseRating"
---
# [SoftLayer_Ticket_Update_Employee](/reference/services/SoftLayer_Ticket_Update_Employee)::addResponseRating

Set an update's response rating.


## Overview 
As part of the customer service process SoftLayer has provided a quick feedback mechanism for its customers to rate the responses that its employees give on tickets. addResponseRating() sets the rating for a single ticket update made by a SoftLayer employee. Ticket ratings have the integer values 1 through 5, with 1 being the worst and 5 being the best. Once the rating is set ''addResponseRating()'' returns a boolean true. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|responseRating| integer| An integer value from 1 to 5, worst to best, that rates a SoftLayer employee's ticket response.|
|responseIndex| integer| An integer value, that refers to the unique update Number.|


### Required Headers
* authenticate
* SoftLayer_Ticket_Update_EmployeeInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Ticket::addFinalComments](/reference/services/SoftLayer_Ticket/addFinalComments )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Please set a response rating between 1 and 5." if ''responseRating'' is anything other than an integer from 1 to 5. 

* SoftLayer_Exception_Public 

> Throw the exception "Ratings cannot be edited on a closed ticket." if ''ticketStatus'' is 1002 (closed) 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to set response rating." if the API was unable to set the update's response rating. 



