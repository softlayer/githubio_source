---
title: "getObject"
description: "getObject retrieves the SoftLayer_Ticket_Subject object whose ID number corresponds to the ID number of the init paramet... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Subject"
aliases:
    - "/reference/services/softlayer_ticket_subject/getObject"
---
# [SoftLayer_Ticket_Subject](/reference/services/SoftLayer_Ticket_Subject)::getObject

Retrieve a SoftLayer_Ticket_Subject record.


## Overview 
getObject retrieves the SoftLayer_Ticket_Subject object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Ticket_Subject service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Ticket_SubjectInitParameters
* authenticate


### Optional Headers
* SoftLayer_Ticket_SubjectObjectMask
* SoftLayer_Ticket_SubjectObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Ticket_Subject'>SoftLayer_Ticket_Subject </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 



