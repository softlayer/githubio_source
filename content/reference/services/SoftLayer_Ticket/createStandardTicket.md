---
title: "createStandardTicket"
description: "Create a standard support ticket. Use a standard support ticket if you need to work out a problem related to SoftLayer's hardware, network, or services. If you require SoftLayer's assistance managing your server or content then please open an administrative ticket. 

Support tickets may only be created in the open state. The SoftLayer API defaults new ticket properties ''userEditableFlag'' to true, ''accountId'' to the id of the account that your API user belongs to, and ''statusId'' to 1001 (or 'open'). You may not assign your new to ticket to users that your API user does not have access to. 

Once your ticket is created it is placed in a queue for SoftLayer employees to work. As they update the ticket new [[SoftLayer_Ticket_Update]] entries are added to the ticket object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "createStandardTicket"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket"
---
