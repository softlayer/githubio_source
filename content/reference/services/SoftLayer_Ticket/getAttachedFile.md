---
title: "getAttachedFile"
description: "Retrieve the file attached to a SoftLayer ticket by it's given identifier. To retrieve a list of files attached to a tic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::getAttachedFile
## Overview 
Retrieve the file attached to a SoftLayer ticket by it's given identifier. To retrieve a list of files attached to a ticket either call the SoftLayer_Ticket::getAttachedFiles method or call SoftLayer_Ticket::getObject with ''attachedFiles'' defined in an object mask. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|attachmentId| integer| The id of the attachment to retrieve|


### Required Headers
* authenticate
* SoftLayer_TicketInitParameters

### Optional Headers

### Return Values
binary data


### associatedMethods

*  [SoftLayer_Ticket::getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles )
*  [SoftLayer_Ticket::getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles )
*  [SoftLayer_Ticket::addAttachedFile](/reference/services/SoftLayer_Ticket/addAttachedFile )

