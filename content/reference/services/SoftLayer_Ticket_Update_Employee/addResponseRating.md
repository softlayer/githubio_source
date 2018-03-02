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
---
# SoftLayer_Ticket_Update_Employee::addResponseRating
## Overview 
As part of the customer service process SoftLayer has provided a quick feedback mechanism for its customers to rate the responses that its employees give on tickets. addResponseRating() sets the rating for a single ticket update made by a SoftLayer employee. Ticket ratings have the integer values 1 through 5, with 1 being the worst and 5 being the best. Once the rating is set ''addResponseRating()'' returns a boolean true. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|responseRating| integer| An integer value from 1 to 5, worst to best, that rates a SoftLayer employee's ticket response.|


### Required Headers
* authenticate
* SoftLayer_Ticket_Update_EmployeeInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Ticket::addFinalComments](/reference/services/SoftLayer_Ticket/addFinalComments )

