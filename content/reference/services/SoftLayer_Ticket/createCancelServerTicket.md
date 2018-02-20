---
title: "createCancelServerTicket"
description: "A cancel server request creates a ticket to cancel the resource on next bill date. The hardware ID parameter is required... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::createCancelServerTicket
## Overview 
A cancel server request creates a ticket to cancel the resource on next bill date. The hardware ID parameter is required to determine which server is to be cancelled. NOTE: Hourly bare metal servers will be cancelled on next bill date. 

The reason parameter could be from the list below: 
* "No longer needed"
* "Business closing down"
* "Server / Upgrade Costs"
* "Migrating to larger server"
* "Migrating to smaller server"
* "Migrating to a different SoftLayer datacenter"
* "Network performance / latency"
* "Support response / timing"
* "Sales process / upgrades"
* "Moving to competitor"


The content parameter describes further the reason for cancelling the server. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|attachmentId| integer| The internal identifier of the server to cancel.|
|reason| string| Cancellation reason.|
|content| string| Cancellation content for ticket. A brief description explaining the cancellation reason.|
|cancelAssociatedItems| boolean| Flag to indicate that associated billing items assigned to the server should be canceled also.|
|attachmentType| string| <ul type="xsd:string"> <li title="HARDWARE">HARDWARE</li> </ul>|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>
