---
title: "createStandardTicket"
description: "Create a standard support ticket. Use a standard support ticket if you need to work out a problem related to SoftLayer's... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket::createStandardTicket
## Overview 
Create a standard support ticket. Use a standard support ticket if you need to work out a problem related to SoftLayer's hardware, network, or services. If you require SoftLayer's assistance managing your server or content then please open an administrative ticket. 

Support tickets may only be created in the open state. The SoftLayer API defaults new ticket properties ''userEditableFlag'' to true, ''accountId'' to the id of the account that your API user belongs to, and ''statusId'' to 1001 (or "open"). You may not assign your new to ticket to users that your API user does not have access to. 

Once your ticket is created it is placed in a queue for SoftLayer employees to work. As they update the ticket new [[SoftLayer_Ticket_Update]] entries are added to the ticket object. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>| A skeleton [[SoftLayer_Ticket (type)|SoftLayer_Ticket]] object containing the data of the ticket you wish to submit.|
|contents| string| The contents of the first update of the ticket. This is typically the ticket's problem description.|
|attachmentId| integer| An optional internal identifier of a piece of hardware or CloudLayer Computing Instance you wish to attach to this ticket. If you attach hardware to a ticket then you must also specify a root or admin password.|
|rootPassword| string| The root password of the hardware you wish to attach to this ticket. Providing your administrative password can significantly improve your ticket response time.|
|controlPanelPassword| string| An optional administrative password to a hosting control panel running on your server, if your server has one installed.|
|accessPort| string| The TCP port on your server that SoftLayer must use to access your operating system. This is typically 22 for SSH and 3389 for Remote Desktop.|
|attachedFiles| <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Attachment'>SoftLayer_Container_Utility_File_Attachment[] </a>| An array of files to attach to a ticket upon creation.|
|attachmentType| string| <ul type="xsd:string"> <li title="HARDWARE">HARDWARE</li> <li title="VIRTUAL_GUEST">VIRTUAL_GUEST</li> </ul>|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>

