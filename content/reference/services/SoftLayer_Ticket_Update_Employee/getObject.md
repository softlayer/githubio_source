---
title: "getObject"
description: "getObject retrieves the SoftLayer_Ticket_Update_Employee object whose ID number corresponds to the ID number of the init... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Update_Employee"
aliases:
    - "/reference/services/softlayer_ticket_update_employee/getObject"
---
# [SoftLayer_Ticket_Update_Employee](/reference/services/SoftLayer_Ticket_Update_Employee)::getObject


Retrieve a SoftLayer_Ticket_Update_Employee record.


## Overview 
getObject retrieves the SoftLayer_Ticket_Update_Employee object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Ticket_Update_Employee service. You can only retrieve employee updates to tickets that your API account has access to. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Ticket_Update_EmployeeInitParameters
* authenticate


### Optional Headers
* SoftLayer_Ticket_Update_EmployeeObjectMask
* SoftLayer_Ticket_Update_EmployeeObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Ticket_Update_Employee'>SoftLayer_Ticket_Update_Employee </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



