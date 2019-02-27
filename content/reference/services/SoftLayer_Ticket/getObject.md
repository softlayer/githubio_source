---
title: "getObject"
description: "getObject retrieves the SoftLayer_Ticket object whose ID number corresponds to the ID number of the init parameter passe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/getObject"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::getObject

Retrieve a SoftLayer_Ticket record.


## Overview 
getObject retrieves the SoftLayer_Ticket object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Ticket service. You can only retrieve tickets that are associated with your SoftLayer customer account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_TicketInitParameters
* authenticate


### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_TicketObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



