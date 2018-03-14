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
<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>

